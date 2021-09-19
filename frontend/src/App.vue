<template>
  <v-app>
    <v-container class="grey lighten-5 mb-6">
      <v-text-field
        v-model="name"
        label="ペンネーム"
        outlined
      ></v-text-field>
      <v-btn
        elevation="2"
        @click="InputName"
        color="primary"
      >送信</v-btn>
      <v-card
        class="mx-auto"
        max-width="400"
        tile
      >
      <div v-for="PostedText in PostedTextList" v-bind:key="PostedText.index">
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>{{PostedText.text}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </div>
    <v-textarea
        v-model="NewText"
        color="teal"
      >
        <template v-slot:label>
          <div>
            新しいメモ
          </div>
        </template>
      </v-textarea>
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
      name : '',
      PostedTextList: []
    }
  },

  methods: {
    InputName: function () {
      var myname = { name: this.name }

      axios
        .post('/api/user_name/post', myname) 
        .then(response => {
          console.log("ok");
          console.log(response.data);
          console.log(this.PostedTextList);
          this.PostedTextList = response.data;
        })
        .catch(err => {
          alert('APIサーバと接続できません')
          console.log("err :", err);
        })
    }
  }
}
</script>