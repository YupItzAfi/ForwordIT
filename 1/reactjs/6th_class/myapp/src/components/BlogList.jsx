const BlogList = (props) => {

    const blogs = props.blogs;
    const title = props.title;

    return (
        <div className="blog-list">
            <h1>{title}</h1>
            <div>{blogs.map((b) => (
                <div className='blog-preview' key={b.id}>
                    <h2>{b.title}</h2>
                    <p><small>{b.author}</small></p>
                    <p>{b.body}</p>
                </div>
            ))}</div>
        </div>
    )
}

export default BlogList;