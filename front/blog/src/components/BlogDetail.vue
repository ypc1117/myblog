<template>
  <div style="background-color:#FFF">
    <div style="padding:20px 20px 20px 20px;border:1px solid #DCDFE6">
      <span style="text-align:center;display:block;">{{ title }}</span><br>
      <span>{{ content }}</span>
      <i class="el-icon-info"><br></i><br>
    </div>
    <div style="height:20px;background-color:#FFFFFF"></div>
    <el-form :model="blog_comment" :rules="rules" ref="blog_comment" size="small" style="padding:20px 20px 20px 20px;border:1px solid #DCDFE6">
      <el-form-item>
        <span>Comment</span>
      </el-form-item>
      <el-form-item prop="comment">
        <el-input type="textarea" :rows=4 placeholder="Please input your blog comment" v-model="blog_comment.comment"></el-input>
      </el-form-item>
      <el-form-item prop="nickname">
        <el-input v-model="blog_comment.nickname" size="large" style="width:40%">
	  <template slot="prepend"><span style="float:left;width:60px;">*nickname</span></template>
	</el-input>
      </el-form-item>
      <el-form-item prop="email">
        <el-input v-model="blog_comment.email" size="large" style="width:40%">
	  <template slot="prepend"><span style="float:left;width:60px;">*email</span></template>
	</el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" v-model="submit" @click="submit()">submit</el-button>
      </el-form-item>
    </el-form>
    <div style="height:20px;background-color:#FFFFFF"></div>
      <div style="padding:20px 20px 20px 20px;border:1px solid #DCDFE6">
        <span>目前评论共有{{ getCommentSizes()}}条</span>
      </div>
    <div style="height:20px;background-color:#FFFFFF"></div>
      <div v-for="comment in comments" :key="comment.id" style="padding:20px 20px 20px 20px;border:1px solid #DCDFE6">
        <div style="display:flex;flex-wrap:nowrap;align:center">
	  <img src="../assets/images/programmer.png" style="width:70px;height:70px;" >
	  <div>
	    <span style="display:inline-block;color:#909399;margin:3px 30px 2px 30px;">{{comment.nickname}}</span><br>
	    <span style="display:inline-block;color:#909399;margin:3px 30px 2px 30px;">{{comment.created_time}}</span><br>
	    <span style="display:inline-block;color:#909399;margin:3px 30px 2px 30px;">{{comment.comment}}</span><br>
	  </div>
	</div>
	<div style="height:20px;background-color:#FFFFFF"></div>
       </div>
    </div>
</template>

<script>
    export default{  
      name: "Blog",
      props: ["blog_id", "title", "content", "comments"],
      data: function(){
        return {
          "blog_comment": {
            "nickname": "",
            "email": "",
            "comment":""
          },
          rules: {
            nickname: [
	      {required: true, message: "the nickname of comment can not be none", trigger: "blur"},
	      {min: 1, max: 20, message: "lengths only equal 20 chars at most"}
	    ],
            email: [
	      {required: true, message: "the nickname of comment can not be none", trigger: "blur"},
	      {min: 1, max: 20, message: "lengths only equal 20 chars at most", trigger: "blur"},
	      {type: "email", message:"input vaild email address", trigger:"blur"}
	    ],
            comment: [
              {required: true, message: "the comment of comment can not be none", trigger: "blur"},
              {min: 1, max: 400, message: "lengths only equal 400 chars at most"}
            ]
          }
        }
      },
      methods: {
        submit(){
	  this.$refs['blog_comment'].validate((valid) =>{
                if(valid){
		    var blog_id = this.blog_id
	            var nickname = this.blog_comment.nickname;
		    var comment = this.blog_comment.comment;
		    var email = this.blog_comment.email;
		    var form_data = {
			"blog_id": blog_id,
			"nickname": nickname,
		        "email": email,
			"comment": comment
		    };
                    this.$http.post(
	                "http://192.168.1.105:8080/blog/comment", form_data, {emulateJSON:true}
		    ).then(function(res){
			console.log("submit successfully!!!!");
                        console.log(res.body);
                    },function(res){
                        console.log(res.status);
                    });
	            this.$alert("submit successfully", "submit", {
		        confirmButtonText: '',
			type: 'success',
			callback: action =>{},
		    });
                    window.location.href = 'http://127.0.0.1:8081/#/blog/show';
		}
		else{
		    console.log("error submit!!!");
		}
          });
        },
        getCommentSizes: function(){
          return this.comments.length;
        }
      }
    };

</script>
