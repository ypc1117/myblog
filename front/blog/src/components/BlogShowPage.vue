<template>
  <div class="block">
    <blog
      is="todo-item"
      v-for="(blog, index) in blogs"
      v-bind:key="blog.id"
      v-bind:title="blog.title"
      v-bind:content="blog.content"
      v-bind:blog_id="blog.blog_id"
      v-bind:comments="blog.comments">
    </blog>
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-size="pageSize"
      layout="total, prev, pager, next, jumper"
      :total="pageTotal">
    </el-pagination>
  </div>
</template>

<script>
  import Blog from '@/components/BlogDetail'
  const myblog = {
    name:"BlogShowPage",
    data: function(){
      return {
        currentPage: 1,
	pageSize: 1,
	pageTotal: 5,
	blogs: []
      }  
    },
    components:{
      'blog': Blog
    },
    methods: {
        show_my_blogs: function(){
	    this.$http.get("/api/show").then(function(jsondata){
	        blog_form_body = jsondata.body;
		blog_form_data = []
		console.log(blog_form_body[0]);
		for(var i=0; i<blog_form_body.length; i++){
		    blog_form_data.push({
			"blog_id": blog_form_body[i].id,
		        "title": blog_form_body[i].blog.title, 
			"content": blog_form_body[i].blog.content,
			"comments": blog_form_body[i].comments
		    });
		}
		this.pageTotal = blog_form_body.length;
		this.total_blogs = blog_form_data;
		this.blogs = [this.total_blogs[this.currentPage-1]];
	      },function(res){
	        console.log(res);
		alert("Error: "+ res);
	      });
        },
	handleCurrentChange: function(val){
	    this.currentPage = val;
	    this.blogs = [this.total_blogs[val-1]];
	},
	handleSizeChange: function(val){
	    this.pageSize = val;
	}
      }
    };
    export default myblog;
    console.log(myblog);
    myblog.methods.show_my_blogs();
</script>
<style>
  .el-textarea__inner::placeholder {
    color: #909399;
  }
</style>
