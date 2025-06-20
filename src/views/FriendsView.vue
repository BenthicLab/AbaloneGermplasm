<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";

import { ElNotification } from "element-plus";
import { setCookie, getCookie, delCookie } from "../assets/js/cookie.js";

export default {
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      visible: false,
      email: "",
      // imageList: [
      //   {
      //     url: require("../assets/image/whale.jpg"),
      //   },
      //   {
      //     url: require("../assets/image/whale.jpg"),
      //   },
      //   {
      //     url: require("../assets/image/whale.jpg"),
      //   },
      // ],
    };
  },
  mounted() {
    ElNotification({
      title: "Friends websites",
      message: "Friends websites, database and servers!",
      type: "success",
      duration: 3000,
      position: "bottom-left",
    });

    // this.email = getCookie("username");
    // if (this.email == "") {
    //   this.$router.push("/login");
    // }
  },
};
</script>

<template>
  <div>
    <el-container>
      <el-header>
        <AppHeader />
      </el-header>
      <el-main>
        <br />
        <br />
        <br />

        <h2>Taxonomy Databases:</h2>
        <el-divider content-position="left">Featured taxonomy databases</el-divider>
        <div style="width: 100%">
          <el-row :gutter="50">
            <el-col :span="24" :sm="12" :lg="12">
              <div style="font-size: 1.2em; line-height: 1.5em; text-align: justify;">
                <h1 class="hightlight-blue">
                  WoRMS: World Register of Marine Species
                </h1>
                <el-link href="https://www.marinespecies.org/index.php" target="_blank" class="hightlight-blue">
                  https://www.marinespecies.org/
                </el-link>
                <p>
                  <span class="hightlight-blue">
                    World Register of Marine Species (WoRMS)
                  </span>
                  The aim of a World Register of Marine Species (WoRMS) is to
                  provide an authoritative and comprehensive list of names of
                  marine organisms, including information on synonymy. While the
                  highest priority goes to valid names, other names in use are
                  included so that this register can serve as a guide to interpret
                  taxonomic literature.
                  <span class="hightlight-blue">
                    The content of WoRMS is controlled by taxonomic and thematic
                    experts, not by database managers.
                  </span>
                  WoRMS has an editorial management system where each taxonomic
                  group is represented by an expert who has the authority over the
                  content, and is responsible for controlling the quality of the
                  information. Each of these main taxonomic editors can invite
                  several specialists of smaller groups within their area of
                  responsibility to join them.
                  <span class="hightlight-blue">
                    This register of marine species grew out of the European
                    Register of Marine Species (ERMS),
                  </span>
                  and its combination with several other species registers
                  maintained at the Flanders Marine Institute (VLIZ).
                </p>
              </div>
            </el-col>
            <el-col :span="24" :sm="12" :lg="12">
              <img src="../assets/image/WoRMS.png" style="
                width: 100%;
                aspect-ratio: true;
                object-fit: cover;
                border-radius: 10px;
                box-shadow: 0px 0px 20px #eeeeee;
              " />
            </el-col>
          </el-row>
        </div>
        <br />
        <br />
        <br />

        <div style="width: 100%">
          <el-row :gutter="50">
            <el-col :span="24" :sm="12" :lg="12">
              <img src="../assets/image/NCBI-Taxonomy.png" style="
                width: 100%;
                aspect-ratio: true;
                object-fit: cover;
                border-radius: 10px;
                box-shadow: 0px 0px 20px #eeeeee;
              " />
            </el-col>
            <el-col :span="24" :sm="12" :lg="12">
              <div style="font-size: 1.2em; line-height: 1.5em; text-align: justify;">
                <h1 class="hightlight-green">
                  NCBI Taxonomy
                </h1>
                <el-link href="https://www.ncbi.nlm.nih.gov/taxonomy" class="hightlight-green">
                  https://www.ncbi.nlm.nih.gov/taxonomy
                </el-link>
                <br />
                <br />
                <span class="hightlight-green">
                  The National Center for Biotechnology Information (NCBI)
                  Taxonomy
                </span>
                includes organism names and classifications for every sequence in
                the nucleotide and protein sequence databases of the International
                Nucleotide Sequence Database Collaboration (INSDC).
                <span class="hightlight-green">
                  An early version of the NCBI Taxonomy in 1991
                </span>
                was included in the first version of Entrez, the search and
                retrieval system for NCBI’s linked databases.
                <span class="hightlight-green">
                  In 1996 the first version of NCBI Taxonomy Web Browser
                </span>
                was presented to the public and the INSDC decided on its annual
                meeting to utilize the NCBI Taxonomy as the only source for
                taxonomic classification to maintain consistency among databases.
              </div>
            </el-col>
          </el-row>
        </div>
        <br />
        <br />
        <br />

        <div style="width: 100%">
          <el-row :gutter="50">
            <el-col :span="24" :sm="12" :lg="12">
              <div style="font-size: 1.2em; line-height: 1.5em; text-align: justify;">
                <h1 class="hightlight-blue">
                  MolluscDB: Molluscan genomics Database
                </h1>
                <el-link href="https://www.marinespecies.org/index.php" target="_blank" class="hightlight-blue">
                  http://mgbase.qnlm.ac
                </el-link>
                <p>
                  <span class="hightlight-blue">
                    An integrated functional and evolutionary genomics database for the hyper-diverse animal phylum
                    Mollusca
                  </span>
                  Mollusca represents the second largest animal phylum but remains poorly explored from a genomic
                  perspective.
                  <span class="hightlight-blue">
                    MolluskDB compiles and integrates current molluscan genomic/transcriptomic resources and provides
                    convenient
                    tools for multi-level integrative and comparative genomic analyses.
                  </span>
                  MolluscDB enables a systematic view of genomic information from various aspects, such as genome
                  assembly statistics,
                  genome phylogenies, fossil records, gene information, expression profiles, etc.
                  <span class="hightlight-blue">
                    MolluscDB offers valuable customized datasets or resources,
                  </span>
                  such as gene coexpression networks across various developmental stages and adult tissues/organs,
                  core gene repertoires inferred for major molluscan lineages, and macrosynteny analysis for chromosomal
                  evolution.
                </p>
              </div>
            </el-col>
            <el-col :span="24" :sm="12" :lg="12">
              <img src="../assets/image/MolluskDB.jpg" style="
                width: 100%;
                aspect-ratio: true;
                object-fit: cover;
                border-radius: 10px;
                box-shadow: 0px 0px 20px #eeeeee;
              " />
            </el-col>
          </el-row>
        </div>
        <br />
        <br />
        <br />

        <div style="width: 100%">
          <el-row :gutter="50">
            <el-col :span="24" :sm="12" :lg="12">
              <img src="../assets/image/BOLDSYSTEMS.png" style="
                width: 100%;
                aspect-ratio: true;
                object-fit: cover;
                border-radius: 10px;
                box-shadow: 0px 0px 20px #eeeeee;
              " />
            </el-col>
            <el-col :span="24" :sm="12" :lg="12">
              <div style="font-size: 1.2em; line-height: 1.5em; text-align: justify;">
                <h1 class="hightlight-green">
                  BOLD SYSTEMS: Barcode of Life Data Systems
                </h1>
                <el-link href="https://www.ncbi.nlm.nih.gov/taxonomy" class="hightlight-green">
                  https://www.boldsystems.org
                </el-link>
                <br />
                <br />
                <span class="hightlight-green">
                  The Barcode of Life Data Systems (BOLD)
                </span>
                is an informatics workbench aiding the acquisition, storage, analysis, and publication of DNA barcode
                records.
                <span class="hightlight-green">
                  By assembling molecular, morphological, and distributional data, it bridges a traditional
                  bioinformatics chasm.
                </span>
                BOLD is freely available to any researcher with interests in DNA barcoding. By providing specialized
                services,
                it aids the assembly of records that meet the standards needed to gain BARCODE designation in the global
                sequence databases.
                <span class="hightlight-green">
                  Because of its web-based delivery and flexible data security model, it is also well positioned to
                  support projects that involve broad research alliances.
                </span>
                Ratnasingham, S. & Hebert, P. D. N. (2007). BOLD: The Barcode of Life Data System
                (www.barcodinglife.org).
                Molecular Ecology Notes 7, 355-364. DOI: 10.1111/j.1471-8286.2006.01678.x
              </div>
            </el-col>
          </el-row>
        </div>
        <br />
        <br />
        <br />
      </el-main>
      <el-footer>
        <AppFooter />
      </el-footer>
    </el-container>
    <el-backtop :right="50" :bottom="100" />
  </div>
</template>

<style scoped>
.hightlight-blue {
  color: #0000ff88;
  font-weight: bold;
  text-shadow: 1px 1px 5px #0000ff88;
}

.hightlight-green {
  color: #00800088;
  font-weight: bold;
  text-shadow: 1px 1px 5px #00800088;
}
</style>
