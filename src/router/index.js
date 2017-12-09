import Vue from 'vue';
import Router from 'vue-router';

/* Import the components here */
// import HelloWorld from '@/components/HelloWorld';
import Login from '@/components/Login';
import RankList from '@/components/RankList';
import MainPage from '@/components/MainPage';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Login
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/main',
      name: 'main',
      component: MainPage
    },
    {
      path: '/ranklist',
      name: 'ranklist',
      component: RankList
    }
  ]
});
