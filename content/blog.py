import sys
from datetime import datetime
from professional_website.models import Post

__author__ = 'jon'

posts = [
    Post(
        name = 'sockIt',
        title = 'SockIt',
        subtitle = 'An asynchronous, client-side Javascript networking plugin',
        timestamp = datetime.strptime('08/01/2011', '%m/%d/%Y'),
        content = """
            <p>
                This summer, I spent the first month of my internship working on a project reminiscent
                of <a href="http://nodejs.org/">node.js</a>, a powerful asynchronous server-side Javascript
                networking library. While node.js allows possesses tremendous ability to perform
                efficient Javascript networking, the current browser security model inhibits similar
                client-side functionality, until SockIt.
            </p>
            <p>
                SockIt, in a nutshell, is an NPAPI browser plugin that circumvents the traditional browser
                security model, allowing pages to perform low-level networking via client-side javascript.
                While it is being actively developed, it already possesses extensive TCP and UDP functionality,
                and even boasts a custom implementation of the heavily-used <a href="http://en.wikipedia.org/wiki/WebSocket">WebSockets</a>
                protocol that supports batch callbacks.
            </p>
            <p>
                Similar to node.js, its networking is performed entirely asynchronously, and it supports
                variety of cross platform browsers. It is newly open sourced, and hosted on
                <a href="http://github.com/sockit/sockit">GitHub</a>, and extensive documentation and
                tutorials are available <a href="http://sockit.github.com/">here</a>.
            </p>
            """
    ),
    Post(
        name = 'automatedUbuntuBackupAndRestore',
        title = 'Automated Ubuntu Backup and Restore',
        subtitle = 'Backup your Ubuntu system safely, efficiently, and effortlessly',
        timestamp = datetime.strptime('09/01/2011', '%m/%d/%Y'),
        content = """
            <p>
                Recently, I discovered that on Ubuntu, or any Debian-based Linux operating system, you can backup
                and restore and restore all packages, independent of the system or architectures itself.
                In fact, I sought out this solution because I wanted to switch to 64-bit Ubuntu from 32-bit,
                and didn't want to manually restore my programs and settings.
            </p>
            <p>
                To backup all installed applications, we first backup <code>sources.list</code> and
                the list of installed packages:<br/>

                <div style="margin-left: 30px;">
                    <pre class="brush: plain">
                        sudo cp /etc/apt/sources.list ./
                        dpkg --get-selections > installed-software
                    </pre><br/>
                </div>

            <p>
                To restore these packages on a clean build, we simply need to perform the following:
            </p>

            <div style="margin-left: 30px;">
                <pre class="brush: plain">
                    sudo cat files/sources.list > /etc/apt/sources.list
                    sudo apt-get update
                    sudo apt-get install dselect
                    sudo dpkg --set-selections < installed-software
                    sudo dselect
                </pre><br/>
            </div>

            <p>
                I modified my own script to automatically install third-party applications that don't
                include PPA's for for Ubuntu, such as <a href="http://www.jetbrains.com/idea/">IntelliJ IDEA</a> and
                the <a href="http://developer.android.com/sdk/index.html">Android SDK</a>, and perform
                other automated configuration, such as configuring Java alternatives, and setting the default
                shell to <a href="http://www.zsh.org/">Zsh</a>.
            </p>
            <p>
                The true benefit of using this method is that backups can be used for different Ubuntu architectures
                and versions, and backups require minimal space.
            </p>
            """
    )
]

# Sync these projects with the backend database
for post in posts:
    try:
        post.save()
    except Exception:
        try:

            # Retrieve the project object already in the database
            existingProject = Post.objects.get(name=post.name)

            # Update all fields of this project
            existingProject.title = post.title
            existingProject.subtitle = post.subtitle
            existingProject.timestamp = post.timestamp
            existingProject.content = post.content
            existingProject.save()

        except Exception:
            print "Skipping '%s': %s" % (post.name, str(sys.exc_info()[1]))