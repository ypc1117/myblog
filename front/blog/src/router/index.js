import Vue from 'vue'
import Router from 'vue-router'
import BlogPostPage from '@/components/BlogPostPage'
import BlogShowPage from '@/components/BlogShowPage'
import Welcome from '@/components/Welcome'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Welcome',
      component: Welcome
    },
    {
      path: '/upload',
      name: 'BlogPostPage',
      component: BlogPostPage 
    },
    {
      path: '/show',
      name: 'BlogShowPage',
      component: BlogShowPage
    }
  ]
})
