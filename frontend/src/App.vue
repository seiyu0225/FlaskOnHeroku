<template>
  <v-app>
    <v-container class=" lighten-5 mb-6">
        <form>
          <v-text-field
            v-model="name"
            label="Name"
            required
          ></v-text-field>
          <v-btn
            elevation="2"
            @click="InputName"
            color="primary"
          >Get posted notes</v-btn>
        </form>
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
            post
          </v-btn>
        </form>
        <v-card
          class="mx-auto"
          max-width="400"
        >
          <v-card-title>Posted Notes</v-card-title>
          <v-card-sub-title class="grey--text">Show notes that have already been posted</v-card-sub-title>
          <v-card-text>
            <div v-for="PostedText in PostedNotesList" v-bind:key="PostedText.index">
              <div class="body-1 mb-1">{{PostedText.text}}</div>
            </div>
          </v-card-text>
        </v-card>
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
          this.PostedNotesList.push(
            {
              index : 1,
              text : this.NewText
            }
          )
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