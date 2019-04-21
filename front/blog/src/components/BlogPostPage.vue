<template>
  <div id="app" style="padding:20px 20px 20px 20px;border:1px solid #DCDFE6">
    <el-form :model="blog_form" :rules="rules" ref="blog_form" label-width="120px" size="mini">
      <el-form-item label="Title" prop="title">
        <el-input  v-model="blog_form.title"></el-input>
      </el-form-item>
      <el-form-item label="Contents" prop="content">
        <el-input  type="textarea" placeholder="Please input your blog content" v-model="blog_form.content"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" v-model="submit" @click="submit('blog_form')">submit</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  export default {
    name: 'BlogShowPage',
    data: function(){
      return {
        blog_form: {
          'title': '',
          'content': ''
	},
        rules:  {
	  title:[
            { required: true, message: 'the title of blog can not be none', trigger: 'blur'},
	    { min: 1, max: 20, message: 'lengths only equal 20 chars at most', trigger: 'blur'}
	  ],
	  content:[
            { required: true, message: 'the content of blog can not be none', trigger: 'blur'},
            { min: 1, max: 500, message: 'lengths only equal 500 chars at most', trigger: 'blur'}
	  ],
        }
      }
    },
    methods: {
        submit(formName) {
	    console.log(this.$refs[formName])
            this.$refs[formName].validate((valid) =>{
                if(valid){
		    console.log(this.blog_form.title)
		    console.log(this.blog_form.content)
		    var form_data = {
			    "title": this.blog_form.title,
		            "content": this.blog_form.content
		    };
                    this.$http.post(
	              "http://127.0.0.1:8080/blog/upload", form_data, {emulateJSON:true}
		    ).then(function(res){
                        console.log(res.body);    
                    },function(res){
                        console.log(res.status);
                    });
	            this.$alert("submit successfully", "submit", {
		        confirmButtonText: '',
			type: 'success',
			callback: action =>{},
		    });
		}else{
		    console.log('error submit!!');
		    return false
		}
             });
        }
     }
  }
</script>
