let blogs = JSON.parse(localStorage.getItem("blogs")) || [];

function saveBlogs() {
  localStorage.setItem("blogs", JSON.stringify(blogs));
}

function displayBlogs() {
  let container = document.getElementById("blogs");
  container.innerHTML = "";

  blogs.forEach((blog, index) => {
    container.innerHTML += `
      <div class="blog">
        <h3>${blog.title}</h3>
        <p>${blog.content}</p>
        <button onclick="editBlog(${index})">Edit</button>
        <button onclick="deleteBlog(${index})">Delete</button>
      </div>
    `;
  });
}

function addBlog() {
  let title = document.getElementById("title").value;
  let content = document.getElementById("content").value;

  if (title === "" || content === "") {
    alert("Please fill all fields");
    return;
  }

  blogs.push({ title, content });
  saveBlogs();
  displayBlogs();

  document.getElementById("title").value = "";
  document.getElementById("content").value = "";
}

function deleteBlog(index) {
  blogs.splice(index, 1);
  saveBlogs();
  displayBlogs();
}

function editBlog(index) {
  let newTitle = prompt("Edit title:", blogs[index].title);
  let newContent = prompt("Edit content:", blogs[index].content);

  if (newTitle && newContent) {
    blogs[index] = { title: newTitle, content: newContent };
    saveBlogs();
    displayBlogs();
  }
}

displayBlogs();