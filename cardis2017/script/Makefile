BASE_DIR	= $(shell pwd)
OUT		= ..
GENMENU 	= ./generateMenu.py
SITEMAP		= sitemap.aux
SITELAYOUT	= layout.json
TEMPLATE	= template.html
PAGES		= $(patsubst %.page, $(OUT)/%.html, $(wildcard *.page))

all: $(PAGES)

.PHONY: clean ultraclean

%.nav: $(SITELAYOUT)
	@$(GENMENU) 0 $(SITELAYOUT) $* >> $@

%.menu: $(SITELAYOUT)
	@$(GENMENU) 1 $(SITELAYOUT) $* >> $@

$(SITEMAP): $(SITELAYOUT)
	@$(GENMENU) 2 $(SITELAYOUT) > $@

$(OUT)/%.html: %.page %.menu %.nav $(SITEMAP) $(TEMPLATE)
	@echo "Generating $@..."
	@sed    -e "/__CONTENT__/r $*.page"    -e "/__CONTENT__/d" \
		-e "/__MENU__/r $*.menu"       -e "/__MENU__/d" \
		-e "/__NAVBAR__/r $*.nav"      -e "/__NAVBAR__/d" \
		-e "/__SITEMAP__/r $(SITEMAP)" -e "/__SITEMAP__/d" \
		$(TEMPLATE) > $@

ultraclean: clean
	rm -f $(OUT)/*.html

clean:
	rm -f $(SITEMAP)
