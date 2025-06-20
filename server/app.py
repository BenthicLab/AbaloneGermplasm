# python=3.8.x
from flask import (
    Flask,
    current_app,
    jsonify,
    make_response,
    request,
    send_from_directory,
    session,
)
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from sqlalchemy.exc import IntegrityError
from flask_wtf import CSRFProtect
from urllib.parse import urljoin
import os
import re

# import uuid

from models import Taxonomies
from models import User

app = Flask(__name__)
app.secret_key = "taxonomy"
# CSRFProtect(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///taxonomies.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
# db.init_app(app)

# CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, supports_credentials=True)


@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""
    return "Hello Taxonomy!"


@app.cli.command()
# `flask --help` and `flask create`
def create():
    db.drop_all()
    db.create_all()
    Taxonomies.init_db()


class TaxonomiesApi(MethodView):
    def get(self, taxonomy_latinname):
        if not taxonomy_latinname:
            taxonomies: [Taxonomies] = Taxonomies.query.all()
            results = [
                {
                    "id": taxonomy.id,
                    "phylum": taxonomy.phylum,
                    "phylum_detail": taxonomy.phylum_detail,
                    "phylum_image": taxonomy.phylum_image,
                    "phylum_cites": taxonomy.phylum_cites,
                    "classes": taxonomy.classes,
                    "classes_detail": taxonomy.classes_detail,
                    "classes_image": taxonomy.classes_image,
                    "classes_cites": taxonomy.classes_cites,
                    "order": taxonomy.order,
                    "order_detail": taxonomy.order_detail,
                    "order_image": taxonomy.order_image,
                    "order_cites": taxonomy.order_cites,
                    "family": taxonomy.family,
                    "family_detail": taxonomy.family_detail,
                    "family_image": taxonomy.family_image,
                    "family_cites": taxonomy.family_cites,
                    "genus": taxonomy.genus,
                    "genus_detail": taxonomy.genus_detail,
                    "genus_image": taxonomy.genus_image,
                    "genus_cites": taxonomy.genus_cites,
                    "latinname": taxonomy.latinname,
                    "author": taxonomy.author,
                    "collector": taxonomy.collector,
                    "translator": taxonomy.translator,
                    "image": taxonomy.image,
                    "common_name": taxonomy.common_name,
                    "synonyms": taxonomy.synonyms,
                    "description": taxonomy.description,
                    "characteristics": taxonomy.characteristics,
                    "habit": taxonomy.habit,
                    "distribution": taxonomy.distribution,
                    "ref_original": taxonomy.ref_original,
                    "ref_additional": taxonomy.ref_additional,
                    "ref_redescription": taxonomy.ref_redescription,
                    "iucn": taxonomy.iucn,
                    "cites": taxonomy.cites,
                    "protection": taxonomy.protection,
                    "threats": taxonomy.threats,
                    "dna_sp1_species": taxonomy.dna_sp1_species,
                    "dna_sp1_voucher": taxonomy.dna_sp1_voucher,
                    "dna_sp1_type": taxonomy.dna_sp1_type,
                    "dna_sp1_deposited": taxonomy.dna_sp1_deposited,
                    "dna_sp1_location": taxonomy.dna_sp1_location,
                    "dna_sp1_coordinates": taxonomy.dna_sp1_coordinates,
                    "dna_sp1_isolation": taxonomy.dna_sp1_isolation,
                    "dna_sp1_date": taxonomy.dna_sp1_date,
                    "dna_sp1_collector": taxonomy.dna_sp1_collector,
                    "dna_sp1_identifier": taxonomy.dna_sp1_identifier,
                    "dna_sp1_email": taxonomy.dna_sp1_email,
                    "dna_sp1_coi_nuc": taxonomy.dna_sp1_coi_nuc,
                    "dna_sp1_coi_aa": taxonomy.dna_sp1_coi_aa,
                    "dna_sp1_coi_codon": taxonomy.dna_sp1_coi_codon,
                    "dna_sp1_coi_info": taxonomy.dna_sp1_coi_info,
                    "dna_sp1_16s_nuc": taxonomy.dna_sp1_16s_nuc,
                    "dna_sp1_16s_info": taxonomy.dna_sp1_16s_info,
                    "dna_sp1_18s_nuc": taxonomy.dna_sp1_18s_nuc,
                    "dna_sp1_18s_info": taxonomy.dna_sp1_18s_info,
                    "dna_sp1_28s_nuc": taxonomy.dna_sp1_28s_nuc,
                    "dna_sp1_28s_info": taxonomy.dna_sp1_28s_info,
                    "dna_sp1_h3_nuc": taxonomy.dna_sp1_h3_nuc,
                    "dna_sp1_h3_info": taxonomy.dna_sp1_h3_info,
                    "dna_sp1_fasta": taxonomy.dna_sp1_fasta,
                    "dna_sp2_species": taxonomy.dna_sp2_species,
                    "dna_sp2_voucher": taxonomy.dna_sp2_voucher,
                    "dna_sp2_type": taxonomy.dna_sp2_type,
                    "dna_sp2_deposited": taxonomy.dna_sp2_deposited,
                    "dna_sp2_location": taxonomy.dna_sp2_location,
                    "dna_sp2_coordinates": taxonomy.dna_sp2_coordinates,
                    "dna_sp2_isolation": taxonomy.dna_sp2_isolation,
                    "dna_sp2_date": taxonomy.dna_sp2_date,
                    "dna_sp2_collector": taxonomy.dna_sp2_collector,
                    "dna_sp2_identifier": taxonomy.dna_sp2_identifier,
                    "dna_sp2_email": taxonomy.dna_sp2_email,
                    "dna_sp2_coi_nuc": taxonomy.dna_sp2_coi_nuc,
                    "dna_sp2_coi_aa": taxonomy.dna_sp2_coi_aa,
                    "dna_sp2_coi_codon": taxonomy.dna_sp2_coi_codon,
                    "dna_sp2_coi_info": taxonomy.dna_sp2_coi_info,
                    "dna_sp2_16s_nuc": taxonomy.dna_sp2_16s_nuc,
                    "dna_sp2_16s_info": taxonomy.dna_sp2_16s_info,
                    "dna_sp2_18s_nuc": taxonomy.dna_sp2_18s_nuc,
                    "dna_sp2_18s_info": taxonomy.dna_sp2_18s_info,
                    "dna_sp2_28s_nuc": taxonomy.dna_sp2_28s_nuc,
                    "dna_sp2_28s_info": taxonomy.dna_sp2_28s_info,
                    "dna_sp2_h3_nuc": taxonomy.dna_sp2_h3_nuc,
                    "dna_sp2_h3_info": taxonomy.dna_sp2_h3_info,
                    "dna_sp2_fasta": taxonomy.dna_sp2_fasta,
                    "dna_sp3_species": taxonomy.dna_sp3_species,
                    "dna_sp3_voucher": taxonomy.dna_sp3_voucher,
                    "dna_sp3_type": taxonomy.dna_sp3_type,
                    "dna_sp3_deposited": taxonomy.dna_sp3_deposited,
                    "dna_sp3_location": taxonomy.dna_sp3_location,
                    "dna_sp3_coordinates": taxonomy.dna_sp3_coordinates,
                    "dna_sp3_isolation": taxonomy.dna_sp3_isolation,
                    "dna_sp3_date": taxonomy.dna_sp3_date,
                    "dna_sp3_collector": taxonomy.dna_sp3_collector,
                    "dna_sp3_identifier": taxonomy.dna_sp3_identifier,
                    "dna_sp3_email": taxonomy.dna_sp3_email,
                    "dna_sp3_coi_nuc": taxonomy.dna_sp3_coi_nuc,
                    "dna_sp3_coi_aa": taxonomy.dna_sp3_coi_aa,
                    "dna_sp3_coi_codon": taxonomy.dna_sp3_coi_codon,
                    "dna_sp3_coi_info": taxonomy.dna_sp3_coi_info,
                    "dna_sp3_16s_nuc": taxonomy.dna_sp3_16s_nuc,
                    "dna_sp3_16s_info": taxonomy.dna_sp3_16s_info,
                    "dna_sp3_18s_nuc": taxonomy.dna_sp3_18s_nuc,
                    "dna_sp3_18s_info": taxonomy.dna_sp3_18s_info,
                    "dna_sp3_28s_nuc": taxonomy.dna_sp3_28s_nuc,
                    "dna_sp3_28s_info": taxonomy.dna_sp3_28s_info,
                    "dna_sp3_h3_nuc": taxonomy.dna_sp3_h3_nuc,
                    "dna_sp3_h3_info": taxonomy.dna_sp3_h3_info,
                    "dna_sp3_fasta": taxonomy.dna_sp3_fasta,
                    "mit_species": taxonomy.mit_species,
                    "mit_voucher": taxonomy.mit_voucher,
                    "mit_type": taxonomy.mit_type,
                    "mit_deposited": taxonomy.mit_deposited,
                    "mit_location": taxonomy.mit_location,
                    "mit_coordinates": taxonomy.mit_coordinates,
                    "mit_isolation": taxonomy.mit_isolation,
                    "mit_depth": taxonomy.mit_depth,
                    "mit_date": taxonomy.mit_date,
                    "mit_collector": taxonomy.mit_collector,
                    "mit_identifier": taxonomy.mit_identifier,
                    "mit_info": taxonomy.mit_info,
                    "mit_seq": taxonomy.mit_seq,
                    "mit_diagram": taxonomy.mit_diagram,
                    "mit_cds": taxonomy.mit_cds,
                    "mit_fasta": taxonomy.mit_fasta,
                    "mit_gbf": taxonomy.mit_gbf,
                    "mit_pdf": taxonomy.mit_pdf,
                }
                for taxonomy in taxonomies
            ]
            return {"status": "success", "message": "success", "results": results}
        taxonomy: Taxonomies = Taxonomies.query.filter(
            Taxonomies.latinname == taxonomy_latinname
        ).first()
        return {
            "status": "success",
            "message": "success",
            "results": {
                "id": taxonomy.id,
                "phylum": taxonomy.phylum,
                "phylum_detail": taxonomy.phylum_detail,
                "phylum_image": taxonomy.phylum_image,
                "phylum_cites": taxonomy.phylum_cites,
                "classes": taxonomy.classes,
                "classes_detail": taxonomy.classes_detail,
                "classes_image": taxonomy.classes_image,
                "classes_cites": taxonomy.classes_cites,
                "order": taxonomy.order,
                "order_detail": taxonomy.order_detail,
                "order_image": taxonomy.order_image,
                "order_cites": taxonomy.order_cites,
                "family": taxonomy.family,
                "family_detail": taxonomy.family_detail,
                "family_image": taxonomy.family_image,
                "family_cites": taxonomy.family_cites,
                "genus": taxonomy.genus,
                "genus_detail": taxonomy.genus_detail,
                "genus_image": taxonomy.genus_image,
                "genus_cites": taxonomy.genus_cites,
                "latinname": taxonomy.latinname,
                "author": taxonomy.author,
                "collector": taxonomy.collector,
                "translator": taxonomy.translator,
                "image": taxonomy.image,
                "common_name": taxonomy.common_name,
                "synonyms": taxonomy.synonyms,
                "description": taxonomy.description,
                "characteristics": taxonomy.characteristics,
                "habit": taxonomy.habit,
                "distribution": taxonomy.distribution,
                "ref_original": taxonomy.ref_original,
                "ref_additional": taxonomy.ref_additional,
                "ref_redescription": taxonomy.ref_redescription,
                "iucn": taxonomy.iucn,
                "cites": taxonomy.cites,
                "protection": taxonomy.protection,
                "threats": taxonomy.threats,
                "dna_sp1_species": taxonomy.dna_sp1_species,
                "dna_sp1_voucher": taxonomy.dna_sp1_voucher,
                "dna_sp1_type": taxonomy.dna_sp1_type,
                "dna_sp1_deposited": taxonomy.dna_sp1_deposited,
                "dna_sp1_location": taxonomy.dna_sp1_location,
                "dna_sp1_coordinates": taxonomy.dna_sp1_coordinates,
                "dna_sp1_isolation": taxonomy.dna_sp1_isolation,
                "dna_sp1_date": taxonomy.dna_sp1_date,
                "dna_sp1_collector": taxonomy.dna_sp1_collector,
                "dna_sp1_identifier": taxonomy.dna_sp1_identifier,
                "dna_sp1_email": taxonomy.dna_sp1_email,
                "dna_sp1_coi_nuc": taxonomy.dna_sp1_coi_nuc,
                "dna_sp1_coi_aa": taxonomy.dna_sp1_coi_aa,
                "dna_sp1_coi_codon": taxonomy.dna_sp1_coi_codon,
                "dna_sp1_coi_info": taxonomy.dna_sp1_coi_info,
                "dna_sp1_16s_nuc": taxonomy.dna_sp1_16s_nuc,
                "dna_sp1_16s_info": taxonomy.dna_sp1_16s_info,
                "dna_sp1_18s_nuc": taxonomy.dna_sp1_18s_nuc,
                "dna_sp1_18s_info": taxonomy.dna_sp1_18s_info,
                "dna_sp1_28s_nuc": taxonomy.dna_sp1_28s_nuc,
                "dna_sp1_28s_info": taxonomy.dna_sp1_28s_info,
                "dna_sp1_h3_nuc": taxonomy.dna_sp1_h3_nuc,
                "dna_sp1_h3_info": taxonomy.dna_sp1_h3_info,
                "dna_sp1_fasta": taxonomy.dna_sp1_fasta,
                "dna_sp2_species": taxonomy.dna_sp2_species,
                "dna_sp2_voucher": taxonomy.dna_sp2_voucher,
                "dna_sp2_type": taxonomy.dna_sp2_type,
                "dna_sp2_deposited": taxonomy.dna_sp2_deposited,
                "dna_sp2_location": taxonomy.dna_sp2_location,
                "dna_sp2_coordinates": taxonomy.dna_sp2_coordinates,
                "dna_sp2_isolation": taxonomy.dna_sp2_isolation,
                "dna_sp2_date": taxonomy.dna_sp2_date,
                "dna_sp2_collector": taxonomy.dna_sp2_collector,
                "dna_sp2_identifier": taxonomy.dna_sp2_identifier,
                "dna_sp2_email": taxonomy.dna_sp2_email,
                "dna_sp2_coi_nuc": taxonomy.dna_sp2_coi_nuc,
                "dna_sp2_coi_aa": taxonomy.dna_sp2_coi_aa,
                "dna_sp2_coi_codon": taxonomy.dna_sp2_coi_codon,
                "dna_sp2_coi_info": taxonomy.dna_sp2_coi_info,
                "dna_sp2_16s_nuc": taxonomy.dna_sp2_16s_nuc,
                "dna_sp2_16s_info": taxonomy.dna_sp2_16s_info,
                "dna_sp2_18s_nuc": taxonomy.dna_sp2_18s_nuc,
                "dna_sp2_18s_info": taxonomy.dna_sp2_18s_info,
                "dna_sp2_28s_nuc": taxonomy.dna_sp2_28s_nuc,
                "dna_sp2_28s_info": taxonomy.dna_sp2_28s_info,
                "dna_sp2_h3_nuc": taxonomy.dna_sp2_h3_nuc,
                "dna_sp2_h3_info": taxonomy.dna_sp2_h3_info,
                "dna_sp2_fasta": taxonomy.dna_sp2_fasta,
                "dna_sp3_species": taxonomy.dna_sp3_species,
                "dna_sp3_voucher": taxonomy.dna_sp3_voucher,
                "dna_sp3_type": taxonomy.dna_sp3_type,
                "dna_sp3_deposited": taxonomy.dna_sp3_deposited,
                "dna_sp3_location": taxonomy.dna_sp3_location,
                "dna_sp3_coordinates": taxonomy.dna_sp3_coordinates,
                "dna_sp3_isolation": taxonomy.dna_sp3_isolation,
                "dna_sp3_date": taxonomy.dna_sp3_date,
                "dna_sp3_collector": taxonomy.dna_sp3_collector,
                "dna_sp3_identifier": taxonomy.dna_sp3_identifier,
                "dna_sp3_email": taxonomy.dna_sp3_email,
                "dna_sp3_coi_nuc": taxonomy.dna_sp3_coi_nuc,
                "dna_sp3_coi_aa": taxonomy.dna_sp3_coi_aa,
                "dna_sp3_coi_codon": taxonomy.dna_sp3_coi_codon,
                "dna_sp3_coi_info": taxonomy.dna_sp3_coi_info,
                "dna_sp3_16s_nuc": taxonomy.dna_sp3_16s_nuc,
                "dna_sp3_16s_info": taxonomy.dna_sp3_16s_info,
                "dna_sp3_18s_nuc": taxonomy.dna_sp3_18s_nuc,
                "dna_sp3_18s_info": taxonomy.dna_sp3_18s_info,
                "dna_sp3_28s_nuc": taxonomy.dna_sp3_28s_nuc,
                "dna_sp3_28s_info": taxonomy.dna_sp3_28s_info,
                "dna_sp3_h3_nuc": taxonomy.dna_sp3_h3_nuc,
                "dna_sp3_h3_info": taxonomy.dna_sp3_h3_info,
                "dna_sp3_fasta": taxonomy.dna_sp3_fasta,
                "mit_species": taxonomy.mit_species,
                "mit_voucher": taxonomy.mit_voucher,
                "mit_type": taxonomy.mit_type,
                "mit_deposited": taxonomy.mit_deposited,
                "mit_location": taxonomy.mit_location,
                "mit_coordinates": taxonomy.mit_coordinates,
                "mit_isolation": taxonomy.mit_isolation,
                "mit_depth": taxonomy.mit_depth,
                "mit_date": taxonomy.mit_date,
                "mit_collector": taxonomy.mit_collector,
                "mit_identifier": taxonomy.mit_identifier,
                "mit_info": taxonomy.mit_info,
                "mit_seq": taxonomy.mit_seq,
                "mit_diagram": taxonomy.mit_diagram,
                "mit_cds": taxonomy.mit_cds,
                "mit_fasta": taxonomy.mit_fasta,
                "mit_gbf": taxonomy.mit_gbf,
                "mit_pdf": taxonomy.mit_pdf,
            },
        }

    def post(self):
        taxonomy = Taxonomies()
        taxonomy.phylum = request.json.get("phylum")
        taxonomy.phylum_detail = request.json.get("phylum_detail")
        taxonomy.phylum_image = request.json.get("phylum_image")
        taxonomy.phylum_cites = request.json.get("phylum_cites")
        taxonomy.classes = request.json.get("classes")
        taxonomy.classes_detail = request.json.get("classes_detail")
        taxonomy.classes_image = request.json.get("classes_image")
        taxonomy.classes_cites = request.json.get("classes_cites")
        taxonomy.order = request.json.get("order")
        taxonomy.order_detail = request.json.get("order_detail")
        taxonomy.order_image = request.json.get("order_image")
        taxonomy.order_cites = request.json.get("order_cites")
        taxonomy.family = request.json.get("family")
        taxonomy.family_detail = request.json.get("family_detail")
        taxonomy.family_image = request.json.get("family_image")
        taxonomy.family_cites = request.json.get("family_cites")
        taxonomy.genus = request.json.get("genus")
        taxonomy.genus_detail = request.json.get("genus_detail")
        taxonomy.genus_image = request.json.get("genus_image")
        taxonomy.genus_cites = request.json.get("genus_cites")
        taxonomy.latinname = request.json.get("latinname")
        taxonomy.author = request.json.get("author")
        taxonomy.collector = request.json.get("collector")
        taxonomy.translator = request.json.get("translator")
        taxonomy.image = request.json.get("image")
        taxonomy.common_name = request.json.get("common_name")
        taxonomy.synonyms = request.json.get("synonyms")
        taxonomy.description = request.json.get("description")
        taxonomy.characteristics = request.json.get("characteristics")
        taxonomy.habit = request.json.get("habit")
        taxonomy.distribution = request.json.get("distribution")
        taxonomy.ref_original = request.json.get("ref_original")
        taxonomy.ref_additional = request.json.get("ref_additional")
        taxonomy.ref_redescription = request.json.get("ref_redescription")
        taxonomy.iucn = request.json.get("iucn")
        taxonomy.cites = request.json.get("cites")
        taxonomy.protection = request.json.get("protection")
        taxonomy.threats = request.json.get("threats")
        taxonomy.dna_sp1_species = request.json.get("dna_sp1_species")
        taxonomy.dna_sp1_voucher = request.json.get("dna_sp1_voucher")
        taxonomy.dna_sp1_type = request.json.get("dna_sp1_type")
        taxonomy.dna_sp1_deposited = request.json.get("dna_sp1_deposited")
        taxonomy.dna_sp1_location = request.json.get("dna_sp1_location")
        taxonomy.dna_sp1_coordinates = request.json.get("dna_sp1_coordinates")
        taxonomy.dna_sp1_isolation = request.json.get("dna_sp1_isolation")
        taxonomy.dna_sp1_date = request.json.get("dna_sp1_date")
        taxonomy.dna_sp1_collector = request.json.get("dna_sp1_collector")
        taxonomy.dna_sp1_identifier = request.json.get("dna_sp1_identifier")
        taxonomy.dna_sp1_email = request.json.get("dna_sp1_email")
        taxonomy.dna_sp1_coi_nuc = request.json.get("dna_sp1_coi_nuc")
        taxonomy.dna_sp1_coi_aa = request.json.get("dna_sp1_coi_aa")
        taxonomy.dna_sp1_coi_codon = request.json.get("dna_sp1_coi_codon")
        taxonomy.dna_sp1_coi_info = request.json.get("dna_sp1_coi_info")
        taxonomy.dna_sp1_16s_nuc = request.json.get("dna_sp1_16s_nuc")
        taxonomy.dna_sp1_16s_info = request.json.get("dna_sp1_16s_info")
        taxonomy.dna_sp1_18s_nuc = request.json.get("dna_sp1_18s_nuc")
        taxonomy.dna_sp1_18s_info = request.json.get("dna_sp1_18s_info")
        taxonomy.dna_sp1_28s_nuc = request.json.get("dna_sp1_28s_nuc")
        taxonomy.dna_sp1_28s_info = request.json.get("dna_sp1_28s_info")
        taxonomy.dna_sp1_h3_nuc = request.json.get("dna_sp1_h3_nuc")
        taxonomy.dna_sp1_h3_info = request.json.get("dna_sp1_h3_info")
        taxonomy.dna_sp1_fasta = request.json.get("dna_sp1_fasta")
        taxonomy.dna_sp2_species = request.json.get("dna_sp2_species")
        taxonomy.dna_sp2_voucher = request.json.get("dna_sp2_voucher")
        taxonomy.dna_sp2_type = request.json.get("dna_sp2_type")
        taxonomy.dna_sp2_deposited = request.json.get("dna_sp2_deposited")
        taxonomy.dna_sp2_location = request.json.get("dna_sp2_location")
        taxonomy.dna_sp2_coordinates = request.json.get("dna_sp2_coordinates")
        taxonomy.dna_sp2_isolation = request.json.get("dna_sp2_isolation")
        taxonomy.dna_sp2_date = request.json.get("dna_sp2_date")
        taxonomy.dna_sp2_collector = request.json.get("dna_sp2_collector")
        taxonomy.dna_sp2_identifier = request.json.get("dna_sp2_identifier")
        taxonomy.dna_sp2_email = request.json.get("dna_sp2_email")
        taxonomy.dna_sp2_coi_nuc = request.json.get("dna_sp2_coi_nuc")
        taxonomy.dna_sp2_coi_aa = request.json.get("dna_sp2_coi_aa")
        taxonomy.dna_sp2_coi_codon = request.json.get("dna_sp2_coi_codon")
        taxonomy.dna_sp2_coi_info = request.json.get("dna_sp2_coi_info")
        taxonomy.dna_sp2_16s_nuc = request.json.get("dna_sp2_16s_nuc")
        taxonomy.dna_sp2_16s_info = request.json.get("dna_sp2_16s_info")
        taxonomy.dna_sp2_18s_nuc = request.json.get("dna_sp2_18s_nuc")
        taxonomy.dna_sp2_18s_info = request.json.get("dna_sp2_18s_info")
        taxonomy.dna_sp2_28s_nuc = request.json.get("dna_sp2_28s_nuc")
        taxonomy.dna_sp2_28s_info = request.json.get("dna_sp2_28s_info")
        taxonomy.dna_sp2_h3_nuc = request.json.get("dna_sp2_h3_nuc")
        taxonomy.dna_sp2_h3_info = request.json.get("dna_sp2_h3_info")
        taxonomy.dna_sp2_fasta = request.json.get("dna_sp2_fasta")
        taxonomy.dna_sp3_species = request.json.get("dna_sp3_species")
        taxonomy.dna_sp3_voucher = request.json.get("dna_sp3_voucher")
        taxonomy.dna_sp3_type = request.json.get("dna_sp3_type")
        taxonomy.dna_sp3_deposited = request.json.get("dna_sp3_deposited")
        taxonomy.dna_sp3_location = request.json.get("dna_sp3_location")
        taxonomy.dna_sp3_coordinates = request.json.get("dna_sp3_coordinates")
        taxonomy.dna_sp3_isolation = request.json.get("dna_sp3_isolation")
        taxonomy.dna_sp3_date = request.json.get("dna_sp3_date")
        taxonomy.dna_sp3_collector = request.json.get("dna_sp3_collector")
        taxonomy.dna_sp3_identifier = request.json.get("dna_sp3_identifier")
        taxonomy.dna_sp3_email = request.json.get("dna_sp3_email")
        taxonomy.dna_sp3_coi_nuc = request.json.get("dna_sp3_coi_nuc")
        taxonomy.dna_sp3_coi_aa = request.json.get("dna_sp3_coi_aa")
        taxonomy.dna_sp3_coi_codon = request.json.get("dna_sp3_coi_codon")
        taxonomy.dna_sp3_coi_info = request.json.get("dna_sp3_coi_info")
        taxonomy.dna_sp3_16s_nuc = request.json.get("dna_sp3_16s_nuc")
        taxonomy.dna_sp3_16s_info = request.json.get("dna_sp3_16s_info")
        taxonomy.dna_sp3_18s_nuc = request.json.get("dna_sp3_18s_nuc")
        taxonomy.dna_sp3_18s_info = request.json.get("dna_sp3_18s_info")
        taxonomy.dna_sp3_28s_nuc = request.json.get("dna_sp3_28s_nuc")
        taxonomy.dna_sp3_28s_info = request.json.get("dna_sp3_28s_info")
        taxonomy.dna_sp3_h3_nuc = request.json.get("dna_sp3_h3_nuc")
        taxonomy.dna_sp3_h3_info = request.json.get("dna_sp3_h3_info")
        taxonomy.dna_sp3_fasta = request.json.get("dna_sp3_fasta")
        taxonomy.mit_species = request.json.get("mit_species")
        taxonomy.mit_voucher = request.json.get("mit_voucher")
        taxonomy.mit_type = request.json.get("mit_type")
        taxonomy.mit_deposited = request.json.get("mit_deposited")
        taxonomy.mit_location = request.json.get("mit_location")
        taxonomy.mit_coordinates = request.json.get("mit_coordinates")
        taxonomy.mit_isolation = request.json.get("mit_isolation")
        taxonomy.mit_depth = request.json.get("mit_depth")
        taxonomy.mit_date = request.json.get("mit_date")
        taxonomy.mit_collector = request.json.get("mit_collector")
        taxonomy.mit_identifier = request.json.get("mit_identifier")
        taxonomy.mit_info = request.json.get("mit_info")
        taxonomy.mit_seq = request.json.get("mit_seq")
        taxonomy.mit_diagram = request.json.get("mit_diagram")
        taxonomy.mit_cds = request.json.get("mit_cds")
        taxonomy.mit_fasta = request.json.get("mit_fasta")
        taxonomy.mit_gbf = request.json.get("mit_gbf")
        taxonomy.mit_pdf = request.json.get("mit_pdf")
        db.session.add(taxonomy)
        db.session.commit()
        return {"status": "success", "message": "success"}

    def delete(self, taxonomy_latinname):
        taxonomy = (
            db.session.query(Taxonomies)
            .filter(Taxonomies.latinname == taxonomy_latinname)
            .first()
        )
        db.session.delete(taxonomy)
        db.session.commit()
        return {"status": "success", "message": "success"}

    def put(self, taxonomy_latinname):
        # taxonomy: Taxonomies = Taxonomies.query.filter(Taxonomies.latinname == taxonomy_latinname).first() # return copy item
        taxonomy: Taxonomies = (
            db.session.query(Taxonomies)
            .filter(Taxonomies.latinname == taxonomy_latinname)
            .first()
        )  # return real item
        taxonomy.phylum = request.json.get("phylum")
        taxonomy.phylum_detail = request.json.get("phylum_detail")
        taxonomy.phylum_image = request.json.get("phylum_image")
        taxonomy.phylum_cites = request.json.get("phylum_cites")
        taxonomy.classes = request.json.get("classes")
        taxonomy.classes_detail = request.json.get("classes_detail")
        taxonomy.classes_image = request.json.get("classes_image")
        taxonomy.classes_cites = request.json.get("classes_cites")
        taxonomy.order = request.json.get("order")
        taxonomy.order_detail = request.json.get("order_detail")
        taxonomy.order_image = request.json.get("order_image")
        taxonomy.order_cites = request.json.get("order_cites")
        taxonomy.family = request.json.get("family")
        taxonomy.family_detail = request.json.get("family_detail")
        taxonomy.family_image = request.json.get("family_image")
        taxonomy.family_cites = request.json.get("family_cites")
        taxonomy.genus = request.json.get("genus")
        taxonomy.genus_detail = request.json.get("genus_detail")
        taxonomy.genus_image = request.json.get("genus_image")
        taxonomy.genus_cites = request.json.get("genus_cites")
        taxonomy.latinname = request.json.get("latinname")
        taxonomy.author = request.json.get("author")
        taxonomy.collector = request.json.get("collector")
        taxonomy.translator = request.json.get("translator")
        taxonomy.image = request.json.get("image")
        taxonomy.common_name = request.json.get("common_name")
        taxonomy.synonyms = request.json.get("synonyms")
        taxonomy.description = request.json.get("description")
        taxonomy.characteristics = request.json.get("characteristics")
        taxonomy.habit = request.json.get("habit")
        taxonomy.distribution = request.json.get("distribution")
        taxonomy.ref_original = request.json.get("ref_original")
        taxonomy.ref_additional = request.json.get("ref_additional")
        taxonomy.ref_redescription = request.json.get("ref_redescription")
        taxonomy.iucn = request.json.get("iucn")
        taxonomy.cites = request.json.get("cites")
        taxonomy.protection = request.json.get("protection")
        taxonomy.threats = request.json.get("threats")
        taxonomy.dna_sp1_species = request.json.get("dna_sp1_species")
        taxonomy.dna_sp1_voucher = request.json.get("dna_sp1_voucher")
        taxonomy.dna_sp1_type = request.json.get("dna_sp1_type")
        taxonomy.dna_sp1_deposited = request.json.get("dna_sp1_deposited")
        taxonomy.dna_sp1_location = request.json.get("dna_sp1_location")
        taxonomy.dna_sp1_coordinates = request.json.get("dna_sp1_coordinates")
        taxonomy.dna_sp1_isolation = request.json.get("dna_sp1_isolation")
        taxonomy.dna_sp1_date = request.json.get("dna_sp1_date")
        taxonomy.dna_sp1_collector = request.json.get("dna_sp1_collector")
        taxonomy.dna_sp1_identifier = request.json.get("dna_sp1_identifier")
        taxonomy.dna_sp1_email = request.json.get("dna_sp1_email")
        taxonomy.dna_sp1_coi_nuc = request.json.get("dna_sp1_coi_nuc")
        taxonomy.dna_sp1_coi_aa = request.json.get("dna_sp1_coi_aa")
        taxonomy.dna_sp1_coi_codon = request.json.get("dna_sp1_coi_codon")
        taxonomy.dna_sp1_coi_info = request.json.get("dna_sp1_coi_info")
        taxonomy.dna_sp1_16s_nuc = request.json.get("dna_sp1_16s_nuc")
        taxonomy.dna_sp1_16s_info = request.json.get("dna_sp1_16s_info")
        taxonomy.dna_sp1_18s_nuc = request.json.get("dna_sp1_18s_nuc")
        taxonomy.dna_sp1_18s_info = request.json.get("dna_sp1_18s_info")
        taxonomy.dna_sp1_28s_nuc = request.json.get("dna_sp1_28s_nuc")
        taxonomy.dna_sp1_28s_info = request.json.get("dna_sp1_28s_info")
        taxonomy.dna_sp1_h3_nuc = request.json.get("dna_sp1_h3_nuc")
        taxonomy.dna_sp1_h3_info = request.json.get("dna_sp1_h3_info")
        taxonomy.dna_sp1_fasta = request.json.get("dna_sp1_fasta")
        taxonomy.dna_sp2_species = request.json.get("dna_sp2_species")
        taxonomy.dna_sp2_voucher = request.json.get("dna_sp2_voucher")
        taxonomy.dna_sp2_type = request.json.get("dna_sp2_type")
        taxonomy.dna_sp2_deposited = request.json.get("dna_sp2_deposited")
        taxonomy.dna_sp2_location = request.json.get("dna_sp2_location")
        taxonomy.dna_sp2_coordinates = request.json.get("dna_sp2_coordinates")
        taxonomy.dna_sp2_isolation = request.json.get("dna_sp2_isolation")
        taxonomy.dna_sp2_date = request.json.get("dna_sp2_date")
        taxonomy.dna_sp2_collector = request.json.get("dna_sp2_collector")
        taxonomy.dna_sp2_identifier = request.json.get("dna_sp2_identifier")
        taxonomy.dna_sp2_email = request.json.get("dna_sp2_email")
        taxonomy.dna_sp2_coi_nuc = request.json.get("dna_sp2_coi_nuc")
        taxonomy.dna_sp2_coi_aa = request.json.get("dna_sp2_coi_aa")
        taxonomy.dna_sp2_coi_codon = request.json.get("dna_sp2_coi_codon")
        taxonomy.dna_sp2_coi_info = request.json.get("dna_sp2_coi_info")
        taxonomy.dna_sp2_16s_nuc = request.json.get("dna_sp2_16s_nuc")
        taxonomy.dna_sp2_16s_info = request.json.get("dna_sp2_16s_info")
        taxonomy.dna_sp2_18s_nuc = request.json.get("dna_sp2_18s_nuc")
        taxonomy.dna_sp2_18s_info = request.json.get("dna_sp2_18s_info")
        taxonomy.dna_sp2_28s_nuc = request.json.get("dna_sp2_28s_nuc")
        taxonomy.dna_sp2_28s_info = request.json.get("dna_sp2_28s_info")
        taxonomy.dna_sp2_h3_nuc = request.json.get("dna_sp2_h3_nuc")
        taxonomy.dna_sp2_h3_info = request.json.get("dna_sp2_h3_info")
        taxonomy.dna_sp2_fasta = request.json.get("dna_sp2_fasta")
        taxonomy.dna_sp3_species = request.json.get("dna_sp3_species")
        taxonomy.dna_sp3_voucher = request.json.get("dna_sp3_voucher")
        taxonomy.dna_sp3_type = request.json.get("dna_sp3_type")
        taxonomy.dna_sp3_deposited = request.json.get("dna_sp3_deposited")
        taxonomy.dna_sp3_location = request.json.get("dna_sp3_location")
        taxonomy.dna_sp3_coordinates = request.json.get("dna_sp3_coordinates")
        taxonomy.dna_sp3_isolation = request.json.get("dna_sp3_isolation")
        taxonomy.dna_sp3_date = request.json.get("dna_sp3_date")
        taxonomy.dna_sp3_collector = request.json.get("dna_sp3_collector")
        taxonomy.dna_sp3_identifier = request.json.get("dna_sp3_identifier")
        taxonomy.dna_sp3_email = request.json.get("dna_sp3_email")
        taxonomy.dna_sp3_coi_nuc = request.json.get("dna_sp3_coi_nuc")
        taxonomy.dna_sp3_coi_aa = request.json.get("dna_sp3_coi_aa")
        taxonomy.dna_sp3_coi_codon = request.json.get("dna_sp3_coi_codon")
        taxonomy.dna_sp3_coi_info = request.json.get("dna_sp3_coi_info")
        taxonomy.dna_sp3_16s_nuc = request.json.get("dna_sp3_16s_nuc")
        taxonomy.dna_sp3_16s_info = request.json.get("dna_sp3_16s_info")
        taxonomy.dna_sp3_18s_nuc = request.json.get("dna_sp3_18s_nuc")
        taxonomy.dna_sp3_18s_info = request.json.get("dna_sp3_18s_info")
        taxonomy.dna_sp3_28s_nuc = request.json.get("dna_sp3_28s_nuc")
        taxonomy.dna_sp3_28s_info = request.json.get("dna_sp3_28s_info")
        taxonomy.dna_sp3_h3_nuc = request.json.get("dna_sp3_h3_nuc")
        taxonomy.dna_sp3_h3_info = request.json.get("dna_sp3_h3_info")
        taxonomy.dna_sp3_fasta = request.json.get("dna_sp3_fasta")
        taxonomy.mit_species = request.json.get("mit_species")
        taxonomy.mit_voucher = request.json.get("mit_voucher")
        taxonomy.mit_type = request.json.get("mit_type")
        taxonomy.mit_deposited = request.json.get("mit_deposited")
        taxonomy.mit_location = request.json.get("mit_location")
        taxonomy.mit_coordinates = request.json.get("mit_coordinates")
        taxonomy.mit_isolation = request.json.get("mit_isolation")
        taxonomy.mit_depth = request.json.get("mit_depth")
        taxonomy.mit_date = request.json.get("mit_date")
        taxonomy.mit_collector = request.json.get("mit_collector")
        taxonomy.mit_identifier = request.json.get("mit_identifier")
        taxonomy.mit_info = request.json.get("mit_info")
        taxonomy.mit_seq = request.json.get("mit_seq")
        taxonomy.mit_diagram = request.json.get("mit_diagram")
        taxonomy.mit_cds = request.json.get("mit_cds")
        taxonomy.mit_fasta = request.json.get("mit_fasta")
        taxonomy.mit_gbf = request.json.get("mit_gbf")
        taxonomy.mit_pdf = request.json.get("mit_pdf")
        db.session.commit()
        return {"status": "success", "message": "success"}


taxonomy_view = TaxonomiesApi.as_view("taxonomy_api")
# `flask routes`
app.add_url_rule(
    "/taxonomy/",
    defaults={"taxonomy_latinname": None},
    view_func=taxonomy_view,
    methods=[
        "GET",
    ],
)
app.add_url_rule(
    "/taxonomy",
    view_func=taxonomy_view,
    methods=[
        "POST",
    ],
)
app.add_url_rule(
    "/taxonomy/<string:taxonomy_latinname>",
    view_func=taxonomy_view,
    methods=["GET", "PUT", "DELETE"],
)


@app.route(
    "/taxonomy/phylum/<string:taxonomy_phylum>",
    methods=[
        "GET",
    ],
)
def get_phylum(taxonomy_phylum):
    taxonomy: Taxonomies = Taxonomies.query.filter(
        Taxonomies.phylum == taxonomy_phylum
    ).first()
    return {
        "status": "success",
        "message": "success",
        "results": {
            "id": taxonomy.id,
            "phylum": taxonomy.phylum,
            "phylum_detail": taxonomy.phylum_detail,
            "phylum_image": taxonomy.phylum_image,
            "phylum_cites": taxonomy.phylum_cites,
            "classes": taxonomy.classes,
            "classes_detail": taxonomy.classes_detail,
            "classes_image": taxonomy.classes_image,
            "classes_cites": taxonomy.classes_cites,
            "order": taxonomy.order,
            "order_detail": taxonomy.order_detail,
            "order_image": taxonomy.order_image,
            "order_cites": taxonomy.order_cites,
            "family": taxonomy.family,
            "family_detail": taxonomy.family_detail,
            "family_image": taxonomy.family_image,
            "family_cites": taxonomy.family_cites,
            "genus": taxonomy.genus,
            "genus_detail": taxonomy.genus_detail,
            "genus_image": taxonomy.genus_image,
            "genus_cites": taxonomy.genus_cites,
            "latinname": taxonomy.latinname,
            "author": taxonomy.author,
            "collector": taxonomy.collector,
            "translator": taxonomy.translator,
            "image": taxonomy.image,
            "common_name": taxonomy.common_name,
            "synonyms": taxonomy.synonyms,
            "description": taxonomy.description,
            "characteristics": taxonomy.characteristics,
            "habit": taxonomy.habit,
            "distribution": taxonomy.distribution,
            "ref_original": taxonomy.ref_original,
            "ref_additional": taxonomy.ref_additional,
            "ref_redescription": taxonomy.ref_redescription,
            "iucn": taxonomy.iucn,
            "cites": taxonomy.cites,
            "protection": taxonomy.protection,
            "threats": taxonomy.threats,
            "dna_sp1_species": taxonomy.dna_sp1_species,
            "dna_sp1_voucher": taxonomy.dna_sp1_voucher,
            "dna_sp1_type": taxonomy.dna_sp1_type,
            "dna_sp1_deposited": taxonomy.dna_sp1_deposited,
            "dna_sp1_location": taxonomy.dna_sp1_location,
            "dna_sp1_coordinates": taxonomy.dna_sp1_coordinates,
            "dna_sp1_isolation": taxonomy.dna_sp1_isolation,
            "dna_sp1_date": taxonomy.dna_sp1_date,
            "dna_sp1_collector": taxonomy.dna_sp1_collector,
            "dna_sp1_identifier": taxonomy.dna_sp1_identifier,
            "dna_sp1_email": taxonomy.dna_sp1_email,
            "dna_sp1_coi_nuc": taxonomy.dna_sp1_coi_nuc,
            "dna_sp1_coi_aa": taxonomy.dna_sp1_coi_aa,
            "dna_sp1_coi_codon": taxonomy.dna_sp1_coi_codon,
            "dna_sp1_coi_info": taxonomy.dna_sp1_coi_info,
            "dna_sp1_16s_nuc": taxonomy.dna_sp1_16s_nuc,
            "dna_sp1_16s_info": taxonomy.dna_sp1_16s_info,
            "dna_sp1_18s_nuc": taxonomy.dna_sp1_18s_nuc,
            "dna_sp1_18s_info": taxonomy.dna_sp1_18s_info,
            "dna_sp1_28s_nuc": taxonomy.dna_sp1_28s_nuc,
            "dna_sp1_28s_info": taxonomy.dna_sp1_28s_info,
            "dna_sp1_h3_nuc": taxonomy.dna_sp1_h3_nuc,
            "dna_sp1_h3_info": taxonomy.dna_sp1_h3_info,
            "dna_sp1_fasta": taxonomy.dna_sp1_fasta,
            "dna_sp2_species": taxonomy.dna_sp2_species,
            "dna_sp2_voucher": taxonomy.dna_sp2_voucher,
            "dna_sp2_type": taxonomy.dna_sp2_type,
            "dna_sp2_deposited": taxonomy.dna_sp2_deposited,
            "dna_sp2_location": taxonomy.dna_sp2_location,
            "dna_sp2_coordinates": taxonomy.dna_sp2_coordinates,
            "dna_sp2_isolation": taxonomy.dna_sp2_isolation,
            "dna_sp2_date": taxonomy.dna_sp2_date,
            "dna_sp2_collector": taxonomy.dna_sp2_collector,
            "dna_sp2_identifier": taxonomy.dna_sp2_identifier,
            "dna_sp2_email": taxonomy.dna_sp2_email,
            "dna_sp2_coi_nuc": taxonomy.dna_sp2_coi_nuc,
            "dna_sp2_coi_aa": taxonomy.dna_sp2_coi_aa,
            "dna_sp2_coi_codon": taxonomy.dna_sp2_coi_codon,
            "dna_sp2_coi_info": taxonomy.dna_sp2_coi_info,
            "dna_sp2_16s_nuc": taxonomy.dna_sp2_16s_nuc,
            "dna_sp2_16s_info": taxonomy.dna_sp2_16s_info,
            "dna_sp2_18s_nuc": taxonomy.dna_sp2_18s_nuc,
            "dna_sp2_18s_info": taxonomy.dna_sp2_18s_info,
            "dna_sp2_28s_nuc": taxonomy.dna_sp2_28s_nuc,
            "dna_sp2_28s_info": taxonomy.dna_sp2_28s_info,
            "dna_sp2_h3_nuc": taxonomy.dna_sp2_h3_nuc,
            "dna_sp2_h3_info": taxonomy.dna_sp2_h3_info,
            "dna_sp2_fasta": taxonomy.dna_sp2_fasta,
            "dna_sp3_species": taxonomy.dna_sp3_species,
            "dna_sp3_voucher": taxonomy.dna_sp3_voucher,
            "dna_sp3_type": taxonomy.dna_sp3_type,
            "dna_sp3_deposited": taxonomy.dna_sp3_deposited,
            "dna_sp3_location": taxonomy.dna_sp3_location,
            "dna_sp3_coordinates": taxonomy.dna_sp3_coordinates,
            "dna_sp3_isolation": taxonomy.dna_sp3_isolation,
            "dna_sp3_date": taxonomy.dna_sp3_date,
            "dna_sp3_collector": taxonomy.dna_sp3_collector,
            "dna_sp3_identifier": taxonomy.dna_sp3_identifier,
            "dna_sp3_email": taxonomy.dna_sp3_email,
            "dna_sp3_coi_nuc": taxonomy.dna_sp3_coi_nuc,
            "dna_sp3_coi_aa": taxonomy.dna_sp3_coi_aa,
            "dna_sp3_coi_codon": taxonomy.dna_sp3_coi_codon,
            "dna_sp3_coi_info": taxonomy.dna_sp3_coi_info,
            "dna_sp3_16s_nuc": taxonomy.dna_sp3_16s_nuc,
            "dna_sp3_16s_info": taxonomy.dna_sp3_16s_info,
            "dna_sp3_18s_nuc": taxonomy.dna_sp3_18s_nuc,
            "dna_sp3_18s_info": taxonomy.dna_sp3_18s_info,
            "dna_sp3_28s_nuc": taxonomy.dna_sp3_28s_nuc,
            "dna_sp3_28s_info": taxonomy.dna_sp3_28s_info,
            "dna_sp3_h3_nuc": taxonomy.dna_sp3_h3_nuc,
            "dna_sp3_h3_info": taxonomy.dna_sp3_h3_info,
            "dna_sp3_fasta": taxonomy.dna_sp3_fasta,
            "mit_species": taxonomy.mit_species,
            "mit_voucher": taxonomy.mit_voucher,
            "mit_type": taxonomy.mit_type,
            "mit_deposited": taxonomy.mit_deposited,
            "mit_location": taxonomy.mit_location,
            "mit_coordinates": taxonomy.mit_coordinates,
            "mit_isolation": taxonomy.mit_isolation,
            "mit_depth": taxonomy.mit_depth,
            "mit_date": taxonomy.mit_date,
            "mit_collector": taxonomy.mit_collector,
            "mit_identifier": taxonomy.mit_identifier,
            "mit_info": taxonomy.mit_info,
            "mit_seq": taxonomy.mit_seq,
            "mit_diagram": taxonomy.mit_diagram,
            "mit_cds": taxonomy.mit_cds,
            "mit_fasta": taxonomy.mit_fasta,
            "mit_gbf": taxonomy.mit_gbf,
            "mit_pdf": taxonomy.mit_pdf,
        },
    }


@app.route(
    "/taxonomy/class/<string:taxonomy_class>",
    methods=[
        "GET",
    ],
)
def get_class(taxonomy_class):
    taxonomy: Taxonomies = Taxonomies.query.filter(
        Taxonomies.classes == taxonomy_class
    ).first()
    return {
        "status": "success",
        "message": "success",
        "results": {
            "id": taxonomy.id,
            "phylum": taxonomy.phylum,
            "phylum_detail": taxonomy.phylum_detail,
            "phylum_image": taxonomy.phylum_image,
            "phylum_cites": taxonomy.phylum_cites,
            "classes": taxonomy.classes,
            "classes_detail": taxonomy.classes_detail,
            "classes_image": taxonomy.classes_image,
            "classes_cites": taxonomy.classes_cites,
            "order": taxonomy.order,
            "order_detail": taxonomy.order_detail,
            "order_image": taxonomy.order_image,
            "order_cites": taxonomy.order_cites,
            "family": taxonomy.family,
            "family_detail": taxonomy.family_detail,
            "family_image": taxonomy.family_image,
            "family_cites": taxonomy.family_cites,
            "genus": taxonomy.genus,
            "genus_detail": taxonomy.genus_detail,
            "genus_image": taxonomy.genus_image,
            "genus_cites": taxonomy.genus_cites,
            "latinname": taxonomy.latinname,
            "author": taxonomy.author,
            "collector": taxonomy.collector,
            "translator": taxonomy.translator,
            "image": taxonomy.image,
            "common_name": taxonomy.common_name,
            "synonyms": taxonomy.synonyms,
            "description": taxonomy.description,
            "characteristics": taxonomy.characteristics,
            "habit": taxonomy.habit,
            "distribution": taxonomy.distribution,
            "ref_original": taxonomy.ref_original,
            "ref_additional": taxonomy.ref_additional,
            "ref_redescription": taxonomy.ref_redescription,
            "iucn": taxonomy.iucn,
            "cites": taxonomy.cites,
            "protection": taxonomy.protection,
            "threats": taxonomy.threats,
            "dna_sp1_species": taxonomy.dna_sp1_species,
            "dna_sp1_voucher": taxonomy.dna_sp1_voucher,
            "dna_sp1_type": taxonomy.dna_sp1_type,
            "dna_sp1_deposited": taxonomy.dna_sp1_deposited,
            "dna_sp1_location": taxonomy.dna_sp1_location,
            "dna_sp1_coordinates": taxonomy.dna_sp1_coordinates,
            "dna_sp1_isolation": taxonomy.dna_sp1_isolation,
            "dna_sp1_date": taxonomy.dna_sp1_date,
            "dna_sp1_collector": taxonomy.dna_sp1_collector,
            "dna_sp1_identifier": taxonomy.dna_sp1_identifier,
            "dna_sp1_email": taxonomy.dna_sp1_email,
            "dna_sp1_coi_nuc": taxonomy.dna_sp1_coi_nuc,
            "dna_sp1_coi_aa": taxonomy.dna_sp1_coi_aa,
            "dna_sp1_coi_codon": taxonomy.dna_sp1_coi_codon,
            "dna_sp1_coi_info": taxonomy.dna_sp1_coi_info,
            "dna_sp1_16s_nuc": taxonomy.dna_sp1_16s_nuc,
            "dna_sp1_16s_info": taxonomy.dna_sp1_16s_info,
            "dna_sp1_18s_nuc": taxonomy.dna_sp1_18s_nuc,
            "dna_sp1_18s_info": taxonomy.dna_sp1_18s_info,
            "dna_sp1_28s_nuc": taxonomy.dna_sp1_28s_nuc,
            "dna_sp1_28s_info": taxonomy.dna_sp1_28s_info,
            "dna_sp1_h3_nuc": taxonomy.dna_sp1_h3_nuc,
            "dna_sp1_h3_info": taxonomy.dna_sp1_h3_info,
            "dna_sp1_fasta": taxonomy.dna_sp1_fasta,
            "dna_sp2_species": taxonomy.dna_sp2_species,
            "dna_sp2_voucher": taxonomy.dna_sp2_voucher,
            "dna_sp2_type": taxonomy.dna_sp2_type,
            "dna_sp2_deposited": taxonomy.dna_sp2_deposited,
            "dna_sp2_location": taxonomy.dna_sp2_location,
            "dna_sp2_coordinates": taxonomy.dna_sp2_coordinates,
            "dna_sp2_isolation": taxonomy.dna_sp2_isolation,
            "dna_sp2_date": taxonomy.dna_sp2_date,
            "dna_sp2_collector": taxonomy.dna_sp2_collector,
            "dna_sp2_identifier": taxonomy.dna_sp2_identifier,
            "dna_sp2_email": taxonomy.dna_sp2_email,
            "dna_sp2_coi_nuc": taxonomy.dna_sp2_coi_nuc,
            "dna_sp2_coi_aa": taxonomy.dna_sp2_coi_aa,
            "dna_sp2_coi_codon": taxonomy.dna_sp2_coi_codon,
            "dna_sp2_coi_info": taxonomy.dna_sp2_coi_info,
            "dna_sp2_16s_nuc": taxonomy.dna_sp2_16s_nuc,
            "dna_sp2_16s_info": taxonomy.dna_sp2_16s_info,
            "dna_sp2_18s_nuc": taxonomy.dna_sp2_18s_nuc,
            "dna_sp2_18s_info": taxonomy.dna_sp2_18s_info,
            "dna_sp2_28s_nuc": taxonomy.dna_sp2_28s_nuc,
            "dna_sp2_28s_info": taxonomy.dna_sp2_28s_info,
            "dna_sp2_h3_nuc": taxonomy.dna_sp2_h3_nuc,
            "dna_sp2_h3_info": taxonomy.dna_sp2_h3_info,
            "dna_sp2_fasta": taxonomy.dna_sp2_fasta,
            "dna_sp3_species": taxonomy.dna_sp3_species,
            "dna_sp3_voucher": taxonomy.dna_sp3_voucher,
            "dna_sp3_type": taxonomy.dna_sp3_type,
            "dna_sp3_deposited": taxonomy.dna_sp3_deposited,
            "dna_sp3_location": taxonomy.dna_sp3_location,
            "dna_sp3_coordinates": taxonomy.dna_sp3_coordinates,
            "dna_sp3_isolation": taxonomy.dna_sp3_isolation,
            "dna_sp3_date": taxonomy.dna_sp3_date,
            "dna_sp3_collector": taxonomy.dna_sp3_collector,
            "dna_sp3_identifier": taxonomy.dna_sp3_identifier,
            "dna_sp3_email": taxonomy.dna_sp3_email,
            "dna_sp3_coi_nuc": taxonomy.dna_sp3_coi_nuc,
            "dna_sp3_coi_aa": taxonomy.dna_sp3_coi_aa,
            "dna_sp3_coi_codon": taxonomy.dna_sp3_coi_codon,
            "dna_sp3_coi_info": taxonomy.dna_sp3_coi_info,
            "dna_sp3_16s_nuc": taxonomy.dna_sp3_16s_nuc,
            "dna_sp3_16s_info": taxonomy.dna_sp3_16s_info,
            "dna_sp3_18s_nuc": taxonomy.dna_sp3_18s_nuc,
            "dna_sp3_18s_info": taxonomy.dna_sp3_18s_info,
            "dna_sp3_28s_nuc": taxonomy.dna_sp3_28s_nuc,
            "dna_sp3_28s_info": taxonomy.dna_sp3_28s_info,
            "dna_sp3_h3_nuc": taxonomy.dna_sp3_h3_nuc,
            "dna_sp3_h3_info": taxonomy.dna_sp3_h3_info,
            "dna_sp3_fasta": taxonomy.dna_sp3_fasta,
            "mit_species": taxonomy.mit_species,
            "mit_voucher": taxonomy.mit_voucher,
            "mit_type": taxonomy.mit_type,
            "mit_deposited": taxonomy.mit_deposited,
            "mit_location": taxonomy.mit_location,
            "mit_coordinates": taxonomy.mit_coordinates,
            "mit_isolation": taxonomy.mit_isolation,
            "mit_depth": taxonomy.mit_depth,
            "mit_date": taxonomy.mit_date,
            "mit_collector": taxonomy.mit_collector,
            "mit_identifier": taxonomy.mit_identifier,
            "mit_info": taxonomy.mit_info,
            "mit_seq": taxonomy.mit_seq,
            "mit_diagram": taxonomy.mit_diagram,
            "mit_cds": taxonomy.mit_cds,
            "mit_fasta": taxonomy.mit_fasta,
            "mit_gbf": taxonomy.mit_gbf,
            "mit_pdf": taxonomy.mit_pdf,
        },
    }


@app.route(
    "/taxonomy/order/<string:taxonomy_order>",
    methods=[
        "GET",
    ],
)
def get_order(taxonomy_order):
    taxonomy: Taxonomies = Taxonomies.query.filter(
        Taxonomies.order == taxonomy_order
    ).first()
    return {
        "status": "success",
        "message": "success",
        "results": {
            "id": taxonomy.id,
            "phylum": taxonomy.phylum,
            "phylum_detail": taxonomy.phylum_detail,
            "phylum_image": taxonomy.phylum_image,
            "phylum_cites": taxonomy.phylum_cites,
            "classes": taxonomy.classes,
            "classes_detail": taxonomy.classes_detail,
            "classes_image": taxonomy.classes_image,
            "classes_cites": taxonomy.classes_cites,
            "order": taxonomy.order,
            "order_detail": taxonomy.order_detail,
            "order_image": taxonomy.order_image,
            "order_cites": taxonomy.order_cites,
            "family": taxonomy.family,
            "family_detail": taxonomy.family_detail,
            "family_image": taxonomy.family_image,
            "family_cites": taxonomy.family_cites,
            "genus": taxonomy.genus,
            "genus_detail": taxonomy.genus_detail,
            "genus_image": taxonomy.genus_image,
            "genus_cites": taxonomy.genus_cites,
            "latinname": taxonomy.latinname,
            "author": taxonomy.author,
            "collector": taxonomy.collector,
            "translator": taxonomy.translator,
            "image": taxonomy.image,
            "common_name": taxonomy.common_name,
            "synonyms": taxonomy.synonyms,
            "description": taxonomy.description,
            "characteristics": taxonomy.characteristics,
            "habit": taxonomy.habit,
            "distribution": taxonomy.distribution,
            "ref_original": taxonomy.ref_original,
            "ref_additional": taxonomy.ref_additional,
            "ref_redescription": taxonomy.ref_redescription,
            "iucn": taxonomy.iucn,
            "cites": taxonomy.cites,
            "protection": taxonomy.protection,
            "threats": taxonomy.threats,
            "dna_sp1_species": taxonomy.dna_sp1_species,
            "dna_sp1_voucher": taxonomy.dna_sp1_voucher,
            "dna_sp1_type": taxonomy.dna_sp1_type,
            "dna_sp1_deposited": taxonomy.dna_sp1_deposited,
            "dna_sp1_location": taxonomy.dna_sp1_location,
            "dna_sp1_coordinates": taxonomy.dna_sp1_coordinates,
            "dna_sp1_isolation": taxonomy.dna_sp1_isolation,
            "dna_sp1_date": taxonomy.dna_sp1_date,
            "dna_sp1_collector": taxonomy.dna_sp1_collector,
            "dna_sp1_identifier": taxonomy.dna_sp1_identifier,
            "dna_sp1_email": taxonomy.dna_sp1_email,
            "dna_sp1_coi_nuc": taxonomy.dna_sp1_coi_nuc,
            "dna_sp1_coi_aa": taxonomy.dna_sp1_coi_aa,
            "dna_sp1_coi_codon": taxonomy.dna_sp1_coi_codon,
            "dna_sp1_coi_info": taxonomy.dna_sp1_coi_info,
            "dna_sp1_16s_nuc": taxonomy.dna_sp1_16s_nuc,
            "dna_sp1_16s_info": taxonomy.dna_sp1_16s_info,
            "dna_sp1_18s_nuc": taxonomy.dna_sp1_18s_nuc,
            "dna_sp1_18s_info": taxonomy.dna_sp1_18s_info,
            "dna_sp1_28s_nuc": taxonomy.dna_sp1_28s_nuc,
            "dna_sp1_28s_info": taxonomy.dna_sp1_28s_info,
            "dna_sp1_h3_nuc": taxonomy.dna_sp1_h3_nuc,
            "dna_sp1_h3_info": taxonomy.dna_sp1_h3_info,
            "dna_sp1_fasta": taxonomy.dna_sp1_fasta,
            "dna_sp2_species": taxonomy.dna_sp2_species,
            "dna_sp2_voucher": taxonomy.dna_sp2_voucher,
            "dna_sp2_type": taxonomy.dna_sp2_type,
            "dna_sp2_deposited": taxonomy.dna_sp2_deposited,
            "dna_sp2_location": taxonomy.dna_sp2_location,
            "dna_sp2_coordinates": taxonomy.dna_sp2_coordinates,
            "dna_sp2_isolation": taxonomy.dna_sp2_isolation,
            "dna_sp2_date": taxonomy.dna_sp2_date,
            "dna_sp2_collector": taxonomy.dna_sp2_collector,
            "dna_sp2_identifier": taxonomy.dna_sp2_identifier,
            "dna_sp2_email": taxonomy.dna_sp2_email,
            "dna_sp2_coi_nuc": taxonomy.dna_sp2_coi_nuc,
            "dna_sp2_coi_aa": taxonomy.dna_sp2_coi_aa,
            "dna_sp2_coi_codon": taxonomy.dna_sp2_coi_codon,
            "dna_sp2_coi_info": taxonomy.dna_sp2_coi_info,
            "dna_sp2_16s_nuc": taxonomy.dna_sp2_16s_nuc,
            "dna_sp2_16s_info": taxonomy.dna_sp2_16s_info,
            "dna_sp2_18s_nuc": taxonomy.dna_sp2_18s_nuc,
            "dna_sp2_18s_info": taxonomy.dna_sp2_18s_info,
            "dna_sp2_28s_nuc": taxonomy.dna_sp2_28s_nuc,
            "dna_sp2_28s_info": taxonomy.dna_sp2_28s_info,
            "dna_sp2_h3_nuc": taxonomy.dna_sp2_h3_nuc,
            "dna_sp2_h3_info": taxonomy.dna_sp2_h3_info,
            "dna_sp2_fasta": taxonomy.dna_sp2_fasta,
            "dna_sp3_species": taxonomy.dna_sp3_species,
            "dna_sp3_voucher": taxonomy.dna_sp3_voucher,
            "dna_sp3_type": taxonomy.dna_sp3_type,
            "dna_sp3_deposited": taxonomy.dna_sp3_deposited,
            "dna_sp3_location": taxonomy.dna_sp3_location,
            "dna_sp3_coordinates": taxonomy.dna_sp3_coordinates,
            "dna_sp3_isolation": taxonomy.dna_sp3_isolation,
            "dna_sp3_date": taxonomy.dna_sp3_date,
            "dna_sp3_collector": taxonomy.dna_sp3_collector,
            "dna_sp3_identifier": taxonomy.dna_sp3_identifier,
            "dna_sp3_email": taxonomy.dna_sp3_email,
            "dna_sp3_coi_nuc": taxonomy.dna_sp3_coi_nuc,
            "dna_sp3_coi_aa": taxonomy.dna_sp3_coi_aa,
            "dna_sp3_coi_codon": taxonomy.dna_sp3_coi_codon,
            "dna_sp3_coi_info": taxonomy.dna_sp3_coi_info,
            "dna_sp3_16s_nuc": taxonomy.dna_sp3_16s_nuc,
            "dna_sp3_16s_info": taxonomy.dna_sp3_16s_info,
            "dna_sp3_18s_nuc": taxonomy.dna_sp3_18s_nuc,
            "dna_sp3_18s_info": taxonomy.dna_sp3_18s_info,
            "dna_sp3_28s_nuc": taxonomy.dna_sp3_28s_nuc,
            "dna_sp3_28s_info": taxonomy.dna_sp3_28s_info,
            "dna_sp3_h3_nuc": taxonomy.dna_sp3_h3_nuc,
            "dna_sp3_h3_info": taxonomy.dna_sp3_h3_info,
            "dna_sp3_fasta": taxonomy.dna_sp3_fasta,
            "mit_species": taxonomy.mit_species,
            "mit_voucher": taxonomy.mit_voucher,
            "mit_type": taxonomy.mit_type,
            "mit_deposited": taxonomy.mit_deposited,
            "mit_location": taxonomy.mit_location,
            "mit_coordinates": taxonomy.mit_coordinates,
            "mit_isolation": taxonomy.mit_isolation,
            "mit_depth": taxonomy.mit_depth,
            "mit_date": taxonomy.mit_date,
            "mit_collector": taxonomy.mit_collector,
            "mit_identifier": taxonomy.mit_identifier,
            "mit_info": taxonomy.mit_info,
            "mit_seq": taxonomy.mit_seq,
            "mit_diagram": taxonomy.mit_diagram,
            "mit_cds": taxonomy.mit_cds,
            "mit_fasta": taxonomy.mit_fasta,
            "mit_gbf": taxonomy.mit_gbf,
            "mit_pdf": taxonomy.mit_pdf,
        },
    }


@app.route(
    "/taxonomy/family/<string:taxonomy_family>",
    methods=[
        "GET",
    ],
)
def get_family(taxonomy_family):
    taxonomy: Taxonomies = Taxonomies.query.filter(
        Taxonomies.family == taxonomy_family
    ).first()
    return {
        "status": "success",
        "message": "success",
        "results": {
            "id": taxonomy.id,
            "phylum": taxonomy.phylum,
            "phylum_detail": taxonomy.phylum_detail,
            "phylum_image": taxonomy.phylum_image,
            "phylum_cites": taxonomy.phylum_cites,
            "classes": taxonomy.classes,
            "classes_detail": taxonomy.classes_detail,
            "classes_image": taxonomy.classes_image,
            "classes_cites": taxonomy.classes_cites,
            "order": taxonomy.order,
            "order_detail": taxonomy.order_detail,
            "order_image": taxonomy.order_image,
            "order_cites": taxonomy.order_cites,
            "family": taxonomy.family,
            "family_detail": taxonomy.family_detail,
            "family_image": taxonomy.family_image,
            "family_cites": taxonomy.family_cites,
            "genus": taxonomy.genus,
            "genus_detail": taxonomy.genus_detail,
            "genus_image": taxonomy.genus_image,
            "genus_cites": taxonomy.genus_cites,
            "latinname": taxonomy.latinname,
            "author": taxonomy.author,
            "collector": taxonomy.collector,
            "translator": taxonomy.translator,
            "image": taxonomy.image,
            "common_name": taxonomy.common_name,
            "synonyms": taxonomy.synonyms,
            "description": taxonomy.description,
            "characteristics": taxonomy.characteristics,
            "habit": taxonomy.habit,
            "distribution": taxonomy.distribution,
            "ref_original": taxonomy.ref_original,
            "ref_additional": taxonomy.ref_additional,
            "ref_redescription": taxonomy.ref_redescription,
            "iucn": taxonomy.iucn,
            "cites": taxonomy.cites,
            "protection": taxonomy.protection,
            "threats": taxonomy.threats,
            "dna_sp1_species": taxonomy.dna_sp1_species,
            "dna_sp1_voucher": taxonomy.dna_sp1_voucher,
            "dna_sp1_type": taxonomy.dna_sp1_type,
            "dna_sp1_deposited": taxonomy.dna_sp1_deposited,
            "dna_sp1_location": taxonomy.dna_sp1_location,
            "dna_sp1_coordinates": taxonomy.dna_sp1_coordinates,
            "dna_sp1_isolation": taxonomy.dna_sp1_isolation,
            "dna_sp1_date": taxonomy.dna_sp1_date,
            "dna_sp1_collector": taxonomy.dna_sp1_collector,
            "dna_sp1_identifier": taxonomy.dna_sp1_identifier,
            "dna_sp1_email": taxonomy.dna_sp1_email,
            "dna_sp1_coi_nuc": taxonomy.dna_sp1_coi_nuc,
            "dna_sp1_coi_aa": taxonomy.dna_sp1_coi_aa,
            "dna_sp1_coi_codon": taxonomy.dna_sp1_coi_codon,
            "dna_sp1_coi_info": taxonomy.dna_sp1_coi_info,
            "dna_sp1_16s_nuc": taxonomy.dna_sp1_16s_nuc,
            "dna_sp1_16s_info": taxonomy.dna_sp1_16s_info,
            "dna_sp1_18s_nuc": taxonomy.dna_sp1_18s_nuc,
            "dna_sp1_18s_info": taxonomy.dna_sp1_18s_info,
            "dna_sp1_28s_nuc": taxonomy.dna_sp1_28s_nuc,
            "dna_sp1_28s_info": taxonomy.dna_sp1_28s_info,
            "dna_sp1_h3_nuc": taxonomy.dna_sp1_h3_nuc,
            "dna_sp1_h3_info": taxonomy.dna_sp1_h3_info,
            "dna_sp1_fasta": taxonomy.dna_sp1_fasta,
            "dna_sp2_species": taxonomy.dna_sp2_species,
            "dna_sp2_voucher": taxonomy.dna_sp2_voucher,
            "dna_sp2_type": taxonomy.dna_sp2_type,
            "dna_sp2_deposited": taxonomy.dna_sp2_deposited,
            "dna_sp2_location": taxonomy.dna_sp2_location,
            "dna_sp2_coordinates": taxonomy.dna_sp2_coordinates,
            "dna_sp2_isolation": taxonomy.dna_sp2_isolation,
            "dna_sp2_date": taxonomy.dna_sp2_date,
            "dna_sp2_collector": taxonomy.dna_sp2_collector,
            "dna_sp2_identifier": taxonomy.dna_sp2_identifier,
            "dna_sp2_email": taxonomy.dna_sp2_email,
            "dna_sp2_coi_nuc": taxonomy.dna_sp2_coi_nuc,
            "dna_sp2_coi_aa": taxonomy.dna_sp2_coi_aa,
            "dna_sp2_coi_codon": taxonomy.dna_sp2_coi_codon,
            "dna_sp2_coi_info": taxonomy.dna_sp2_coi_info,
            "dna_sp2_16s_nuc": taxonomy.dna_sp2_16s_nuc,
            "dna_sp2_16s_info": taxonomy.dna_sp2_16s_info,
            "dna_sp2_18s_nuc": taxonomy.dna_sp2_18s_nuc,
            "dna_sp2_18s_info": taxonomy.dna_sp2_18s_info,
            "dna_sp2_28s_nuc": taxonomy.dna_sp2_28s_nuc,
            "dna_sp2_28s_info": taxonomy.dna_sp2_28s_info,
            "dna_sp2_h3_nuc": taxonomy.dna_sp2_h3_nuc,
            "dna_sp2_h3_info": taxonomy.dna_sp2_h3_info,
            "dna_sp2_fasta": taxonomy.dna_sp2_fasta,
            "dna_sp3_species": taxonomy.dna_sp3_species,
            "dna_sp3_voucher": taxonomy.dna_sp3_voucher,
            "dna_sp3_type": taxonomy.dna_sp3_type,
            "dna_sp3_deposited": taxonomy.dna_sp3_deposited,
            "dna_sp3_location": taxonomy.dna_sp3_location,
            "dna_sp3_coordinates": taxonomy.dna_sp3_coordinates,
            "dna_sp3_isolation": taxonomy.dna_sp3_isolation,
            "dna_sp3_date": taxonomy.dna_sp3_date,
            "dna_sp3_collector": taxonomy.dna_sp3_collector,
            "dna_sp3_identifier": taxonomy.dna_sp3_identifier,
            "dna_sp3_email": taxonomy.dna_sp3_email,
            "dna_sp3_coi_nuc": taxonomy.dna_sp3_coi_nuc,
            "dna_sp3_coi_aa": taxonomy.dna_sp3_coi_aa,
            "dna_sp3_coi_codon": taxonomy.dna_sp3_coi_codon,
            "dna_sp3_coi_info": taxonomy.dna_sp3_coi_info,
            "dna_sp3_16s_nuc": taxonomy.dna_sp3_16s_nuc,
            "dna_sp3_16s_info": taxonomy.dna_sp3_16s_info,
            "dna_sp3_18s_nuc": taxonomy.dna_sp3_18s_nuc,
            "dna_sp3_18s_info": taxonomy.dna_sp3_18s_info,
            "dna_sp3_28s_nuc": taxonomy.dna_sp3_28s_nuc,
            "dna_sp3_28s_info": taxonomy.dna_sp3_28s_info,
            "dna_sp3_h3_nuc": taxonomy.dna_sp3_h3_nuc,
            "dna_sp3_h3_info": taxonomy.dna_sp3_h3_info,
            "dna_sp3_fasta": taxonomy.dna_sp3_fasta,
            "mit_species": taxonomy.mit_species,
            "mit_voucher": taxonomy.mit_voucher,
            "mit_type": taxonomy.mit_type,
            "mit_deposited": taxonomy.mit_deposited,
            "mit_location": taxonomy.mit_location,
            "mit_coordinates": taxonomy.mit_coordinates,
            "mit_isolation": taxonomy.mit_isolation,
            "mit_depth": taxonomy.mit_depth,
            "mit_date": taxonomy.mit_date,
            "mit_collector": taxonomy.mit_collector,
            "mit_identifier": taxonomy.mit_identifier,
            "mit_info": taxonomy.mit_info,
            "mit_seq": taxonomy.mit_seq,
            "mit_diagram": taxonomy.mit_diagram,
            "mit_cds": taxonomy.mit_cds,
            "mit_fasta": taxonomy.mit_fasta,
            "mit_gbf": taxonomy.mit_gbf,
            "mit_pdf": taxonomy.mit_pdf,
        },
    }


@app.route(
    "/taxonomy/genus/<string:taxonomy_genus>",
    methods=[
        "GET",
    ],
)
def get_genus(taxonomy_genus):
    taxonomy: Taxonomies = Taxonomies.query.filter(
        Taxonomies.genus == taxonomy_genus
    ).first()
    return {
        "status": "success",
        "message": "success",
        "results": {
            "id": taxonomy.id,
            "phylum": taxonomy.phylum,
            "phylum_detail": taxonomy.phylum_detail,
            "phylum_image": taxonomy.phylum_image,
            "phylum_cites": taxonomy.phylum_cites,
            "classes": taxonomy.classes,
            "classes_detail": taxonomy.classes_detail,
            "classes_image": taxonomy.classes_image,
            "classes_cites": taxonomy.classes_cites,
            "order": taxonomy.order,
            "order_detail": taxonomy.order_detail,
            "order_image": taxonomy.order_image,
            "order_cites": taxonomy.order_cites,
            "family": taxonomy.family,
            "family_detail": taxonomy.family_detail,
            "family_image": taxonomy.family_image,
            "family_cites": taxonomy.family_cites,
            "genus": taxonomy.genus,
            "genus_detail": taxonomy.genus_detail,
            "genus_image": taxonomy.genus_image,
            "genus_cites": taxonomy.genus_cites,
            "latinname": taxonomy.latinname,
            "author": taxonomy.author,
            "collector": taxonomy.collector,
            "translator": taxonomy.translator,
            "image": taxonomy.image,
            "common_name": taxonomy.common_name,
            "synonyms": taxonomy.synonyms,
            "description": taxonomy.description,
            "characteristics": taxonomy.characteristics,
            "habit": taxonomy.habit,
            "distribution": taxonomy.distribution,
            "ref_original": taxonomy.ref_original,
            "ref_additional": taxonomy.ref_additional,
            "ref_redescription": taxonomy.ref_redescription,
            "iucn": taxonomy.iucn,
            "cites": taxonomy.cites,
            "protection": taxonomy.protection,
            "threats": taxonomy.threats,
            "dna_sp1_species": taxonomy.dna_sp1_species,
            "dna_sp1_voucher": taxonomy.dna_sp1_voucher,
            "dna_sp1_type": taxonomy.dna_sp1_type,
            "dna_sp1_deposited": taxonomy.dna_sp1_deposited,
            "dna_sp1_location": taxonomy.dna_sp1_location,
            "dna_sp1_coordinates": taxonomy.dna_sp1_coordinates,
            "dna_sp1_isolation": taxonomy.dna_sp1_isolation,
            "dna_sp1_date": taxonomy.dna_sp1_date,
            "dna_sp1_collector": taxonomy.dna_sp1_collector,
            "dna_sp1_identifier": taxonomy.dna_sp1_identifier,
            "dna_sp1_email": taxonomy.dna_sp1_email,
            "dna_sp1_coi_nuc": taxonomy.dna_sp1_coi_nuc,
            "dna_sp1_coi_aa": taxonomy.dna_sp1_coi_aa,
            "dna_sp1_coi_codon": taxonomy.dna_sp1_coi_codon,
            "dna_sp1_coi_info": taxonomy.dna_sp1_coi_info,
            "dna_sp1_16s_nuc": taxonomy.dna_sp1_16s_nuc,
            "dna_sp1_16s_info": taxonomy.dna_sp1_16s_info,
            "dna_sp1_18s_nuc": taxonomy.dna_sp1_18s_nuc,
            "dna_sp1_18s_info": taxonomy.dna_sp1_18s_info,
            "dna_sp1_28s_nuc": taxonomy.dna_sp1_28s_nuc,
            "dna_sp1_28s_info": taxonomy.dna_sp1_28s_info,
            "dna_sp1_h3_nuc": taxonomy.dna_sp1_h3_nuc,
            "dna_sp1_h3_info": taxonomy.dna_sp1_h3_info,
            "dna_sp1_fasta": taxonomy.dna_sp1_fasta,
            "dna_sp2_species": taxonomy.dna_sp2_species,
            "dna_sp2_voucher": taxonomy.dna_sp2_voucher,
            "dna_sp2_type": taxonomy.dna_sp2_type,
            "dna_sp2_deposited": taxonomy.dna_sp2_deposited,
            "dna_sp2_location": taxonomy.dna_sp2_location,
            "dna_sp2_coordinates": taxonomy.dna_sp2_coordinates,
            "dna_sp2_isolation": taxonomy.dna_sp2_isolation,
            "dna_sp2_date": taxonomy.dna_sp2_date,
            "dna_sp2_collector": taxonomy.dna_sp2_collector,
            "dna_sp2_identifier": taxonomy.dna_sp2_identifier,
            "dna_sp2_email": taxonomy.dna_sp2_email,
            "dna_sp2_coi_nuc": taxonomy.dna_sp2_coi_nuc,
            "dna_sp2_coi_aa": taxonomy.dna_sp2_coi_aa,
            "dna_sp2_coi_codon": taxonomy.dna_sp2_coi_codon,
            "dna_sp2_coi_info": taxonomy.dna_sp2_coi_info,
            "dna_sp2_16s_nuc": taxonomy.dna_sp2_16s_nuc,
            "dna_sp2_16s_info": taxonomy.dna_sp2_16s_info,
            "dna_sp2_18s_nuc": taxonomy.dna_sp2_18s_nuc,
            "dna_sp2_18s_info": taxonomy.dna_sp2_18s_info,
            "dna_sp2_28s_nuc": taxonomy.dna_sp2_28s_nuc,
            "dna_sp2_28s_info": taxonomy.dna_sp2_28s_info,
            "dna_sp2_h3_nuc": taxonomy.dna_sp2_h3_nuc,
            "dna_sp2_h3_info": taxonomy.dna_sp2_h3_info,
            "dna_sp2_fasta": taxonomy.dna_sp2_fasta,
            "dna_sp3_species": taxonomy.dna_sp3_species,
            "dna_sp3_voucher": taxonomy.dna_sp3_voucher,
            "dna_sp3_type": taxonomy.dna_sp3_type,
            "dna_sp3_deposited": taxonomy.dna_sp3_deposited,
            "dna_sp3_location": taxonomy.dna_sp3_location,
            "dna_sp3_coordinates": taxonomy.dna_sp3_coordinates,
            "dna_sp3_isolation": taxonomy.dna_sp3_isolation,
            "dna_sp3_date": taxonomy.dna_sp3_date,
            "dna_sp3_collector": taxonomy.dna_sp3_collector,
            "dna_sp3_identifier": taxonomy.dna_sp3_identifier,
            "dna_sp3_email": taxonomy.dna_sp3_email,
            "dna_sp3_coi_nuc": taxonomy.dna_sp3_coi_nuc,
            "dna_sp3_coi_aa": taxonomy.dna_sp3_coi_aa,
            "dna_sp3_coi_codon": taxonomy.dna_sp3_coi_codon,
            "dna_sp3_coi_info": taxonomy.dna_sp3_coi_info,
            "dna_sp3_16s_nuc": taxonomy.dna_sp3_16s_nuc,
            "dna_sp3_16s_info": taxonomy.dna_sp3_16s_info,
            "dna_sp3_18s_nuc": taxonomy.dna_sp3_18s_nuc,
            "dna_sp3_18s_info": taxonomy.dna_sp3_18s_info,
            "dna_sp3_28s_nuc": taxonomy.dna_sp3_28s_nuc,
            "dna_sp3_28s_info": taxonomy.dna_sp3_28s_info,
            "dna_sp3_h3_nuc": taxonomy.dna_sp3_h3_nuc,
            "dna_sp3_h3_info": taxonomy.dna_sp3_h3_info,
            "dna_sp3_fasta": taxonomy.dna_sp3_fasta,
            "mit_species": taxonomy.mit_species,
            "mit_voucher": taxonomy.mit_voucher,
            "mit_type": taxonomy.mit_type,
            "mit_deposited": taxonomy.mit_deposited,
            "mit_location": taxonomy.mit_location,
            "mit_coordinates": taxonomy.mit_coordinates,
            "mit_isolation": taxonomy.mit_isolation,
            "mit_depth": taxonomy.mit_depth,
            "mit_date": taxonomy.mit_date,
            "mit_collector": taxonomy.mit_collector,
            "mit_identifier": taxonomy.mit_identifier,
            "mit_info": taxonomy.mit_info,
            "mit_seq": taxonomy.mit_seq,
            "mit_diagram": taxonomy.mit_diagram,
            "mit_cds": taxonomy.mit_cds,
            "mit_fasta": taxonomy.mit_fasta,
            "mit_gbf": taxonomy.mit_gbf,
            "mit_pdf": taxonomy.mit_pdf,
        },
    }


ALLOWED_EXTENSIONS = {
    "pdf",
    "png",
    "jpg",
    "jpeg",
    "gif",
    "TIFF",
    "TIF",
    "cds",
    "fasta",
    "gbf",
}
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10M


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# def random_filename(filename):
#     ext = os.path.splitext(filename)[-1]
#     return uuid.uuid4().hex + ext


@app.route(
    "/taxonomy/image_upload",
    methods=[
        "POST",
    ],
)
def image_upload():
    file = request.files.get("file")

    if file and allowed_file(file.filename):
        # filename = random_filename(file.filename)
        filename = file.filename
        filepath = os.path.join("store/image", filename).replace("\\", "/")
        file.save(os.path.join(app.root_path, filepath))

        file_url = urljoin(request.host_url, filepath)

        return file_url
    return "not allow ext"


@app.route("/store/image/<path:filename>")
def image_get(filename):
    return send_from_directory("store/image", filename)


@app.route(
    "/taxonomy/file_upload",
    methods=[
        "POST",
    ],
)
def file_upload():
    file = request.files.get("file")

    if file and allowed_file(file.filename):
        # filename = random_filename(file.filename)
        filename = file.filename
        filepath = os.path.join("store/file", filename).replace("\\", "/")
        file.save(os.path.join(app.root_path, filepath))

        file_url = urljoin(request.host_url, filepath)

        return file_url
    return "not allow ext"


@app.route("/store/file/<path:filename>")
def file_get(filename):
    return send_from_directory("store/file", filename)


@app.route(
    "/signup",
    methods=[
        "POST",
    ],
)
def signup():
    email = request.json.get("email")
    password = request.json.get("password")
    confirm = request.json.get("confirm")

    if not all([email, password, confirm]):
        return "AllError"
    # if not re.match(r'1[34578]\d{9}', mobile):
    #   return ""
    if not re.search(r"\@", email):
        return "EmailError"
    if len(password) < 6:
        return "PasswordError"
    if password != confirm:
        return "ConfirmError"

    # try:
    #   user = User.query.filter_by(email = email).first()
    # except Exception as e:
    #   current_app.logger.error(e)
    # else:
    #   if user is not None:
    #     return 'ExistError'

    user = User(email=email, username=email)
    # user.generate_password_hash(password) # 1.function
    user.hash_password = password  # 2.property
    try:
        db.session.add(user)
        db.session.commit()
        return "SignupSuccess"
    except IntegrityError as e:
        db.session.rollback()
        current_app.logger.error(e)
        return "ExistError"
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return "DatabaseError"

    # session['email'] = email
    # session['username'] = email


@app.route(
    "/login",
    methods=[
        "POST",
    ],
)
def login():
    email = request.json.get("email")
    password = request.json.get("password")

    if not all([email, password]):
        return "AllError"
    if not re.search(r"\@", email):
        return "EmailError"

    try:
        user = User.query.filter_by(email=email).first()
    except Exception as e:
        current_app.logger.error(e)
        return "QueryError"

    if user is None or not user.check_password_hash(password):
        return "ExistError"
    elif user.email == "admin@admin.com" and user.check_password_hash(password):
        return "AdminSuccess"
    else:
        return "UserSuccess"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
