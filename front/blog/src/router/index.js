import Vue from 'vue'
import Router from 'vue-router'
import BlogPostPage from '@/components/BlogPostPage'
import BlogShowPage from '@/components/BlogShowPage'
import Welcome from '@/components/Welcome'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/blog',
      name: 'Welcome',
      component: Welcome
    },
    {
      path: '/blog/upload',
      name: 'BlogPostPage',
      component: BlogPostPage 
    },
    {
      path: '/blog/show',
      name: 'BlogShowPage',
      component: BlogShowPage
    }
  ]
})
