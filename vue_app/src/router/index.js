import Vue from 'vue'
import VueRouter from 'vue-router'
import layout_staff from '../layout/layout_staff.vue'
import layout_user from '../layout/layout_user.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'landing',
    component: layout_user,
    children:[{
      path:'/',
      component:() => import("@/views/user/landing.vue")
    }]
  },
  {
    path: '/myoffset',
    name: 'myoffset',
    component: layout_user,
    children:[{
      path:'/myoffset',
      component:() => import("@/views/user/calculate.vue")
    }]
  },
  {
    path: '/mapview',
    name: 'mapview',
    component: layout_user,
    children:[{
      path:'/mapview',
      component:() => import("@/views/user/map.vue")
    }]
  },
    {
    path: '/fundview',
    name: 'fundview',
    component: layout_user,
    children:[{
      path:'/fundview',
      component:() => import("../views/user/funding.vue")
    }]
  },
  {
    path: '/login',
    name: 'login',
    component: layout_user,
    children:[{
      path:'/login',
      component:() => import("@/views/login/login.vue")
    }]
  },
  {
    path: '/register',
    name: 'register',
    component: layout_user,
    children:[{
      path:'/register',
      component:() => import("@/views/login/register.vue")
    }]
  },
  {
    path: '/accounts',
    name: 'accounts',
    component: layout_staff,
    children:[{
      path:'/accounts',
      component:() => import("@/views/staff/accounts.vue")
    }]
  },
  {
    path: '/home',
    name: 'home',
    component: layout_staff,
    children:[{
      path:'/home',
      component:() => import("@/views/staff/homepage.vue")
    }]
  },
  {
    path: '/about',
    name: 'about',
    component: layout_staff,
    children:[{
      path:'/about',
      component:() => import("@/views/staff/aboutpage.vue")
    }]
  },
  {
    path: '/success',
    name: 'success',
    component: layout_user,
    children:[{
      path:'/success',
      component:() => import("@/views/user/success.vue")
    }]
  }
]

const router = new VueRouter({
  base: process.env.BASE_URL,
  routes
})

export default router
