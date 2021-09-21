<template>
  <v-app>
    <v-container class=" lighten-5 mb-6">
      <v-row justify="center">
        <v-col cols="10">
            <v-text-field
              v-model="Name"
              label="Name"
              required
            ></v-text-field>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="10" >
          <form>
            <v-text-field
              v-model="NewText"
              :error-messages="ValidationErrors"
              :counter="200"
              label="New Notes"
              required
            ></v-text-field>
            <v-btn
              class="mr-4"
              @click="Submit"
              color="primary"
            >
              post note
            </v-btn>
          </form>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="10">
            <v-card
              class="mx-auto"
            >
              <v-card-title>Posted Notes Of {{Name}}</v-card-title>
              <v-card-text>
                <div v-for="PostedText in PostedNotesList" v-bind:key="PostedText.index">
                  <div class="body-1 mb-1">{{PostedText.text}}</div>
                </div>
              </v-card-text>
            </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',

  data () {
    return {
      // 入力データ
      NewText: '',
      Name : '',
      PostedNotesList: []
    }
  },

  methods: {
    InputName: function () {
      var myname = { name: this.Name }

      axios
        .post('/api/user_name/post', myname) 
        .then(response => {
          console.log("ok");
          console.log(response.data);
          console.log(this.PostedTextList);
          this.PostedTextList = response.data;
        })
        .catch(err => {
          console.log("err :", err);
        })
        
    },
    Submit: function () {
      this.PostedNotesList.push(
        {
          index : 1,
          text : this.NewText
        }
      )
    }
  }
}
</script>