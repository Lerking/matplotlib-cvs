from matplotlib.matlab import *


a = arange(0,3,.02)
b = arange(0,3,.02)
c=exp(a)
d=c.tolist()
d.reverse()
d = array(d)

xlabel('Model complexity --->')
ylabel('Message length --->')
title('Minimum Message Length')

ax = subplot(111)
plot(a,c,'k--',a,d,'k:',a,c+d,'bo')
legend(('Model length', 'Data length', 'Total message length'), 1)
ax.set_ylim([-1,20])
ax.grid(0)
set(gca(), 'yticklabels', [])
set(gca(), 'xticklabels', [])

savefig('mml')
show()