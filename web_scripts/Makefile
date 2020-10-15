# user-defined variables
SOURCE_DIR=xml
OUTPUT_DIR=.
SCRIPT=bin/xml_to_html.py
HTML_TEMPLATE=templates/almSite.template.html

# find all the xml files. then make up the html names by replacing .xml->.html
XMLS=$(wildcard $(SOURCE_DIR)/*.xml)
HTMLS=$(addprefix $(OUTPUT_DIR)/,$(notdir $(XMLS:.xml=.html)))

all: $(HTMLS)

$(OUTPUT_DIR)/%.html: $(SOURCE_DIR)/%.xml $(SCRIPT)
	$(SCRIPT) $< --template $(HTML_TEMPLATE) $@
