# GitHubAPIVisualisation

Software Engineering Github API visualisation
Due 22nd December


For this project I focused on provididng measurements of all the activity in a user's github account.
It gets a bit messy when the account has extremely large levels of activity but seems to be find for smaller amounts
My Visualisation consists of two graphs.

The first is a graph showing every single commit that has ever occurred in a users account.
You can scroll to narrow down the dates or to expand them. You can also use it to see the commits between two specific points in time
It's based on the commits made each day but it is also possible to alter the python code to make it based on commits in an hour

The second graph shows every single repository in the the users account and every single user that has commit to those 
repositories. The size of the the user nodes will scale up depending on the amount of contributions they made.
The size of the nodes is calculated using logarithmic scaling just to stop the issue of one node being several thousand times
larger than a node where a user only made 1 or 2 commits.

Both graphs are interactive. In the first one you can determine the time period of commits you want to see by scrolling or manipulating the window at the bottom
of the graph. In the second graph, you can click categories legend at the top of the graph to make the repository node and all associated users disappear. This allows you 
to look at select repositories at a time.

I used data taking from trending repositories on Github but I hid the  user names and repository names and replaced them with numbers.
