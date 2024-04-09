"""
=====================================================================================
Accounts management Page

CRUD operations for user/staff accounts.
"""

__author__ = "rxu37@sheffield.ac.uk"
<template>
  <v-container fluid class="fill-height">
      <v-layout justify-center>
          <v-flex fill-height>
              <v-row class="fill-height">
                  <v-col>
                    <v-card height="100%" width="100%">
                        <v-card-title>User Accounts</v-card-title>
                          <template>
                              <v-data-table
                                  :headers="user_headers"
                                  :items="user_accounts"
                                  :search="search_user"
                                  class="elevation-1"
                              >
                              <template v-slot:top>
                              <v-toolbar
                                  flat
                              >
                              <v-dialog
                                  v-model="user_dialog"
                                  max-width="500px"
                              >
                              <template v-slot:activator="{ on, attrs }">
                                  <v-btn
                                      color="dark"
                                      small
                                      dark
                                      tile
                                      class="mb-2"
                                      v-bind="attrs"
                                      v-on="on"
                                  >
                                      New Account
                                  </v-btn>
                              </template>
                              <v-card>
                                  <v-card-title>
                                      <span class="text-h5">{{ formTitle }}</span>
                                  </v-card-title>
                                  <v-card-text>
                                      <v-container>
                                          <v-row>
                                              <v-col
                                                  cols="12"
                                                  sm="6"
                                                  md="4"
                                              >
                                                  <v-text-field
                                                      v-model="user_editedItem.name"
                                                      label="Username"
                                                      :disabled = "user_editedIndex != -1"
                                                  ></v-text-field>
                                              </v-col>
                                              <v-col
                                                  cols="12"
                                                  sm="6"
                                                  md="4"
                                              >
                                                  <v-text-field
                                                      v-model="user_editedItem.password"
                                                      label="Password"
                                                      :disabled = "user_editedIndex != -1"
                                                  ></v-text-field>
                                              </v-col>
                                              <v-col
                                                  cols="12"
                                                  sm="6"
                                                  md="4"
                                              >
                                                  <v-text-field
                                                      v-model="user_editedItem.email"
                                                      label="E-mail"
                                                      :disabled = "user_editedIndex != -1"
                                                  ></v-text-field>
                                              </v-col>
                                              <v-col
                                                  cols="12"
                                                  sm="6"
                                                  md="4"
                                              >
                                                  <v-text-field
                                                      v-model="user_editedItem.n_name"
                                                      label="New Username"
                                                      v-if="user_editedIndex != -1"
                                                  ></v-text-field>
                                              </v-col>
                                          </v-row>
                                      </v-container>
                                  </v-card-text>
                                  <v-card-actions>
                                      <v-spacer></v-spacer>
                                      <v-btn
                                          color="blue darken-1"
                                          text
                                          @click="user_close"
                                      >
                                          Cancel
                                      </v-btn>
                                      <v-btn
                                          color="blue darken-1"
                                          text
                                          @click="user_save"
                                      >
                                          Save
                                      </v-btn>
                                  </v-card-actions>
                              </v-card>
                              </v-dialog>
                              <v-dialog v-model="user_dialogDelete" max-width="500px">
                                  <v-card>
                                      <v-card-title class="text-h5">Are you sure you want to delete this account?</v-card-title>
                                      <v-card-actions>
                                          <v-spacer></v-spacer>
                                          <v-btn color="blue darken-1" text @click="user_closeDelete">Cancel</v-btn>
                                          <v-btn color="blue darken-1" text @click="user_deleteItemConfirm">Yes</v-btn>
                                          <v-spacer></v-spacer>
                                      </v-card-actions>
                                  </v-card>
                              </v-dialog>
                              <v-spacer></v-spacer>
                              <v-text-field
                                  v-model="search_user"
                                  append-icon="mdi-magnify"
                                  label="Search"
                                  single-line
                                  hide-details
                              ></v-text-field>
                              </v-toolbar>
                              </template>
                              <template v-slot:item.actions="{ item }">
                                  <v-icon
                                  small
                                  class="mr-2"
                                  @click="user_editItem(item)"
                                  >
                                      mdi-pencil
                                  </v-icon>
                                  <v-icon
                                      small
                                      @click="user_deleteItem(item)"
                                  >
                                      mdi-delete
                                  </v-icon>
                              </template>
                              <template v-slot:no-data>
                                  Nothing here......
                              </template>
                              </v-data-table>
                          </template>
                      </v-card>
                  </v-col>
                  <v-col>
                    <v-card height="100%" width="100%" v-if="!staff_authorize()">
                        <v-card-title>Staff Accounts</v-card-title>
                        <v-row class="pt-16 mt-16">
                          <v-col>
                            <v-row>
                              <v-spacer></v-spacer>
                                <v-icon x-large color="red darken-4">
                                  mdi-account-alert-outline
                                </v-icon>
                              <v-spacer></v-spacer>
                            </v-row>
                            <v-row>
                              <v-spacer></v-spacer>
                              <h2>UNAUTHORIZED</h2>
                              <v-spacer></v-spacer>
                            </v-row>
                          </v-col>
                        </v-row>
                      </v-card>
                      <v-card height="100%" width="100%" v-if="staff_authorize()">
                          <v-card-title>Staff Accounts</v-card-title>
                          <template>
                              <v-data-table
                                  :headers="staff_headers"
                                  :items="staff_accounts"
                                  :search="search_staff"
                                  class="elevation-1"
                              >
                              <template v-slot:top>
                              <v-toolbar
                                  flat
                              >
                              <v-dialog
                                  v-model="staff_dialog"
                                  max-width="500px"
                              >
                              <template v-slot:activator="{ on, attrs }">
                                  <v-btn
                                      color="dark"
                                      small
                                      dark
                                      tile
                                      class="mb-2"
                                      v-bind="attrs"
                                      v-on="on"
                                  >
                                      New Account
                                  </v-btn>
                              </template>
                              <v-card>
                                  <v-card-title>
                                      <span class="text-h5">{{ formTitle }}</span>
                                  </v-card-title>
                                  <v-card-text>
                                      <v-container>
                                          <v-row>
                                              <v-col
                                                  cols="12"
                                                  sm="4"
                                                  md="4"
                                              >
                                                  <v-text-field
                                                      v-model="staff_editedItem.name"
                                                      label="Username"
                                                      :disabled = "staff_editedIndex != -1"
                                                      v-if="staff_upgradeStatus == -1"
                                                  ></v-text-field>
                                              </v-col>
                                              <v-col
                                                  cols="12"
                                                  sm="6"
                                                  md="4"
                                              >
                                                  <v-text-field
                                                      v-model="staff_editedItem.password"
                                                      label="Password"
                                                      :disabled = "staff_editedIndex != -1"
                                                      v-if="staff_upgradeStatus == -1"
                                                  ></v-text-field>
                                              </v-col>
                                              <v-col
                                                  cols="12"
                                                  sm="6"
                                                  md="4"
                                              >
                                                  <v-text-field
                                                      v-model="staff_editedItem.email"
                                                      label="E-mail"
                                                      :disabled = "staff_editedIndex != -1"
                                                      v-if="staff_upgradeStatus == -1"
                                                  ></v-text-field>
                                              </v-col>
                                              <v-col
                                                  cols="12"
                                                  sm="6"
                                                  md="4"
                                              >
                                                  <v-select
                                                    v-model="staff_editedItem.level"
                                                    :items="levels"
                                                    label="Level"
                                                    :disabled = "staff_editedIndex != -1"
                                                  ></v-select>
                                              </v-col>
                                              <v-col
                                                  cols="12"
                                                  sm="6"
                                                  md="4"
                                              >
                                                  <v-text-field
                                                      v-model="staff_editedItem.n_name"
                                                      label="New Username"
                                                      v-if="(staff_editedIndex != -1)||(staff_upgradeStatus == -1&&staff_editedIndex != -1)"
                                                  ></v-text-field>
                                              </v-col>
                                          </v-row>
                                      </v-container>
                                  </v-card-text>
                                  <v-card-actions>
                                      <v-spacer></v-spacer>
                                      <v-btn
                                          color="blue darken-1"
                                          text
                                          @click="staff_close"
                                      >
                                          Cancel
                                      </v-btn>
                                      <v-btn
                                          color="blue darken-1"
                                          text
                                          @click="staff_save"
                                      >
                                          Save
                                      </v-btn>
                                  </v-card-actions>
                              </v-card>
                              </v-dialog>
                              <v-dialog v-model="staff_dialogDelete" max-width="500px">
                                  <v-card>
                                      <v-card-title class="text-h5">Are you sure you want to delete this account?</v-card-title>
                                      <v-card-actions>
                                          <v-spacer></v-spacer>
                                          <v-btn color="blue darken-1" text @click="staff_closeDelete">Cancel</v-btn>
                                          <v-btn color="blue darken-1" text @click="staff_deleteItemConfirm">Yes</v-btn>
                                          <v-spacer></v-spacer>
                                      </v-card-actions>
                                  </v-card>
                              </v-dialog>
                              <v-spacer></v-spacer>
                              <v-text-field
                                  v-model="search_staff"
                                  append-icon="mdi-magnify"
                                  label="Search"
                                  single-line
                                  hide-details
                              ></v-text-field>
                              </v-toolbar>
                              </template>
                              <template v-slot:item.actions="{ item }">
                                <v-icon
                                  small
                                  class="mr-2"
                                  @click="staff_upgrade(item)"
                                  >
                                      mdi-account
                                  </v-icon>
                                  <v-icon
                                  small
                                  class="mr-2"
                                  @click="staff_editItem(item)"
                                  >
                                      mdi-pencil
                                  </v-icon>
                                  <v-icon
                                      small
                                      @click="staff_deleteItem(item)"
                                  >
                                      mdi-delete
                                  </v-icon>
                              </template>
                              <template v-slot:no-data>
                                  Nothing here......
                              </template>
                              </v-data-table>
                          </template>
                      </v-card>
                  </v-col>
              </v-row>
          </v-flex>
      </v-layout>
  </v-container>
</template>

<script>
import { insertUser } from '../../plugins/api'
import { insertStaff } from '../../plugins/api'
import { upgradeStaff } from '../../plugins/api'
import { editUser } from '../../plugins/api'
import { deleteUser } from '../../plugins/api'
import { getAllStaff } from '../../plugins/api'
import { getAllUser } from '../../plugins/api'
export default {
  data: () => ({
    search_staff:'',
    staff_dialog: false,
    staff_dialogDelete: false,
    levels:['LEVEL-1','LEVEL-2','ADMIN'],
    //staff table headers
    staff_headers: [
      {
        text: 'Username',
        align: 'start',
        sortable: false,
        value: 'name',
      },
      { text: 'Password', value: 'password' },
      { text: 'E-mail', value: 'email' },
      { text: 'Level', value: 'level' },
      { text: 'Actions', value: 'actions', sortable: false },
    ],

    //staff table data
    staff_accounts: [],

    //index in staff table
    staff_editedIndex: -1,
    staff_upgradeStatus: -1,
    staff_editedItem: {
      n_name: '',
      name: '',
      password: '',
      email: '@',
      level: 'LEVEL-1',
    },
    staff_defaultItem: {
      n_name: '',
      name: '',
      password: '',
      email: '@',
      level: 'LEVEL-1',
    },
    search_user:'',
    user_dialog: false,
    user_dialogDelete: false,
    //user table headers
    user_headers: [
      {
        text: 'Username',
        align: 'start',
        sortable: false,
        value: 'name',
      },
      { text: 'Password', value: 'password' },
      { text: 'E-mail', value: 'email' },
      { text: 'Actions', value: 'actions', sortable: false },
    ],

    //user table data
    user_accounts: [],

    //index in user table
    user_editedIndex: -1,
    user_editedItem: {
      n_name: '',
      name: '',
      password: '',
      email: '@',
    },
    user_defaultItem: {
      n_name: '',
      name: '',
      password: '',
      email: '@',
    },
  }),

  computed: {
    formTitle () {
      //generate title of the v-card 
      return this.staff_editedIndex === -1&&this.staff_upgradeStatus === -1 ? 'New Account' : 'Edit Account'
    },
  },

  watch: {
    staff_dialog (val) {
      val || this.staff_close()
    },
    staff_dialogDelete (val) {
      val || this.staff_closeDelete()
    },
    user_dialog (val) {
      val || this.user_close()
    },
    user_dialogDelete (val) {
      val || this.user_closeDelete()
    },
  },

  created () {
    this.initialize()
  },

  methods: {
    initialize () {

      //grab data from backend, fill the tables
      getAllUser({}).then( res=> {
        this.user_accounts = res.data
      })
      getAllStaff({}).then( res=> {
        this.staff_accounts = res.data
      })
    },

    //only admin is able to manage staff accounts
    staff_authorize () {
      if(sessionStorage.getItem("role")=='ADMIN')
      return true
      else return false
    },

    //change staff levels
    staff_upgrade (item) {
      this.staff_upgradeStatus = this.staff_accounts.indexOf(item)
      this.staff_editedItem.level = this.staff_accounts[this.staff_upgradeStatus].level
      this.staff_dialog = true
    },

    //change staff username
    staff_editItem (item) {
      this.staff_editedIndex = this.staff_accounts.indexOf(item)
      this.staff_editedItem = Object.assign({}, item)
      this.staff_editedItem.n_name = this.staff_editedItem.name
      this.staff_dialog = true
    },

    //delete staff
    staff_deleteItem (item) {
      this.staff_editedIndex = this.staff_accounts.indexOf(item)
      this.staff_editedItem = Object.assign({}, item)
      this.staff_dialogDelete = true
    },

    staff_deleteItemConfirm () {
      deleteUser({
        "username": this.staff_accounts[this.staff_editedIndex].name
      }).then(
        this.staff_accounts.splice(this.staff_editedIndex, 1),
        this.staff_closeDelete()
      )
    },

    staff_close () {
      this.staff_dialog = false
      this.$nextTick(() => {
        this.staff_upgradeStatus = -1,
        this.staff_editedItem = Object.assign({}, this.staff_defaultItem)
        this.staff_editedIndex = -1
      })
    },

    staff_closeDelete () {
      this.staff_dialogDelete = false
      this.$nextTick(() => {
        this.staff_upgradeStatus = -1,
        this.staff_editedItem = Object.assign({}, this.staff_defaultItem)
        this.staff_editedIndex = -1
      })
    },

    //save insert/edit/upgrade changes
    staff_save () {
      if (this.staff_editedIndex > -1) {
          editUser({
            "new_username": this.staff_editedItem.n_name,
            "email": this.staff_editedItem.email,
            "username": this.staff_editedItem.name
          }).then(
            this.staff_upgradeStatus = -1,
            this.staff_editedItem.name = this.staff_editedItem.n_name,
            Object.assign(this.staff_accounts[this.staff_editedIndex], this.staff_editedItem)
          )
        
      } else if (this.staff_upgradeStatus != -1) {
        upgradeStaff({
            "roles": this.staff_editedItem.level,
            "username": this.staff_accounts[this.staff_upgradeStatus].name
          }).then(
            this.staff_accounts[this.staff_upgradeStatus].level = this.staff_editedItem.level,
            this.staff_upgradeStatus = -1
          )
      } else {
        insertStaff({
          "password": this.staff_editedItem.password,
          "username": this.staff_editedItem.name,
          "email": this.staff_editedItem.email
        }).then(
          this.staff_upgradeStatus = -1,
          this.staff_accounts.push(this.staff_editedItem)
        )
      }
      this.staff_close()
    },

    //change username
    user_editItem (item) {
      this.user_editedIndex = this.user_accounts.indexOf(item)
      this.user_editedItem = Object.assign({}, item)
      this.user_editedItem.n_name = this.user_editedItem.name
      this.user_dialog = true
    },

    //delete user
    user_deleteItem (item) {
      this.user_editedIndex = this.user_accounts.indexOf(item)
      this.user_editedItem = Object.assign({}, item)
      this.user_dialogDelete = true
    },

    user_deleteItemConfirm () {
      deleteUser({
        "username": this.user_accounts[this.user_editedIndex].name
      }).then(
        this.user_accounts.splice(this.user_editedIndex, 1),
        this.user_closeDelete()
      )
    },

    user_close () {
      this.user_dialog = false
      this.$nextTick(() => {
        this.user_editedItem = Object.assign({}, this.user_defaultItem)
        this.user_editedIndex = -1
      })
    },

    user_closeDelete () {
      this.user_dialogDelete = false
      this.$nextTick(() => {
        this.user_editedItem = Object.assign({}, this.user_defaultItem)
        this.user_editedIndex = -1
      })
    },

    //save insert/edit changes
    user_save () {
      if (this.user_editedIndex > -1) {
        editUser({
          "new_username": this.user_editedItem.n_name,
          "email": this.user_editedItem.email,
          "username": this.user_editedItem.name
        }).then(
          this.user_editedItem.name = this.user_editedItem.n_name,
          Object.assign(this.user_accounts[this.user_editedIndex], this.user_editedItem)
        )
      } else {
        insertUser({
          "password": this.user_editedItem.password,
          "username": this.user_editedItem.name,
          "email": this.user_editedItem.email
        }).then(
          this.user_accounts.push(this.user_editedItem)
        )
      }
      this.user_close()
    },
  },
}
</script>