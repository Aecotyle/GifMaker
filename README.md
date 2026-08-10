1684736 tmoazzam Fri Jul 24 07:40:50 2026       30:03 Ss   /usr/lib/systemd/systemd --user
1684749 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ssl  /usr/bin/pipewire
1684750 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ssl  /usr/bin/pipewire -c filter-chain.conf
1684751 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ssl  /snap/snapd-desktop-integration/396/usr/bin/user-session-helper /snap/snapd-desktop-integration/396/usr/bin/snapd-desktop-integration
1684752 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ssl  /usr/bin/wireplumber
1684753 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ssl  /usr/bin/pipewire-pulse
1684772 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ss   /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
1684826 tmoazzam Fri Jul 24 07:40:51 2026       30:02 Ssl  /usr/libexec/xdg-document-portal


root@spark-da4d:~/vllm_env_dir/vllm_env# for pid in 1684736 1684749 1684750 1684751 1684752 1684753 1684772 1684826
do
    echo "===== PID $pid ====="
    cat /proc/$pid/cmdline | tr '\0' ' '
    echo
done
===== PID 1684736 =====
/usr/lib/systemd/systemd --user 
===== PID 1684749 =====
/usr/bin/pipewire 
===== PID 1684750 =====
/usr/bin/pipewire -c filter-chain.conf 
===== PID 1684751 =====
/snap/snapd-desktop-integration/396/usr/bin/user-session-helper /snap/snapd-desktop-integration/396/usr/bin/snapd-desktop-integration 
===== PID 1684752 =====
/usr/bin/wireplumber 
===== PID 1684753 =====
/usr/bin/pipewire-pulse 
===== PID 1684772 =====
/usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only 
===== PID 1684826 =====
/usr/libexec/xdg-document-portal 
root@spark-da4d:~/vllm_env_dir/vllm_env# lsof -p 1684749
lsof: WARNING: can't stat() fuse.portal file system /run/user/126/doc
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.portal file system /run/user/1000/doc
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.portal file system /run/user/1001/doc
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.portal file system /run/user/1003/doc
      Output information may be incomplete.
COMMAND      PID     USER   FD      TYPE             DEVICE SIZE/OFF     NODE NAME
pipewire 1684749 tmoazzam  cwd       DIR              259,2     4096  7475537 /home/tmoazzam
pipewire 1684749 tmoazzam  rtd       DIR              259,2     4096        2 /
pipewire 1684749 tmoazzam  txt       REG              259,2    67752  1352191 /usr/bin/pipewire
pipewire 1684749 tmoazzam  mem       REG              259,2   467560  1710839 /usr/lib/aarch64-linux-gnu/spa-0.2/audioconvert/libspa-audioconvert.so
pipewire 1684749 tmoazzam  mem       REG              259,2    67624  1710939 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-jackdbus-detect.so
pipewire 1684749 tmoazzam  mem       REG              259,2   198672  1710962 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-session-manager.so
pipewire 1684749 tmoazzam  mem       REG              259,2    67624  1710940 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-link-factory.so
pipewire 1684749 tmoazzam  mem       REG              259,2   198696  1710761 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-adapter.so
pipewire 1684749 tmoazzam  mem       REG              259,2  1445440  1311423 /usr/lib/aarch64-linux-gnu/libglib-2.0.so.0.8000.0
pipewire 1684749 tmoazzam  mem       REG              259,2    67624  1710759 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-access.so
pipewire 1684749 tmoazzam  mem       REG              259,2    67624  1710946 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-portal.so
pipewire 1684749 tmoazzam  mem       REG              259,2    67624  1710769 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-client-device.so
pipewire 1684749 tmoazzam  mem       REG              259,2   329768  1710773 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-client-node.so
pipewire 1684749 tmoazzam  mem       REG              259,2   133160  1710966 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-spa-node-factory.so
pipewire 1684749 tmoazzam  mem       REG              259,2    67624  1710964 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-spa-device-factory.so
pipewire 1684749 tmoazzam  mem       REG              259,2    67624  1710942 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-metadata.so
pipewire 1684749 tmoazzam  mem       REG              259,2    67624  1710947 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-profiler.so
pipewire 1684749 tmoazzam  mem       REG              259,2   592328  1312362 /usr/lib/aarch64-linux-gnu/libpcre2-8.so.0.11.2
pipewire 1684749 tmoazzam  mem       REG              259,2   198800  1312390 /usr/lib/aarch64-linux-gnu/libselinux.so.1
pipewire 1684749 tmoazzam  mem       REG              259,2   329792  1710948 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-protocol-native.so
pipewire 1684749 tmoazzam  mem       REG              259,2    67624  1710956 /usr/lib/aarch64-linux-gnu/pipewire-0.3/libpipewire-module-rt.so
pipewire 1684749 tmoazzam  mem       REG              259,2   395336  1312200 /usr/lib/aarch64-linux-gnu/libdbus-1.so.3.32.4
pipewire 1684749 tmoazzam  mem       REG              259,2    67624  1710928 /usr/lib/aarch64-linux-gnu/spa-0.2/support/libspa-dbus.so
pipewire 1684749 tmoazzam  mem       REG              259,2   198648  1312249 /usr/lib/aarch64-linux-gnu/libgpg-error.so.0.34.0
pipewire 1684749 tmoazzam  mem       REG              259,2   657432  1312453 /usr/lib/aarch64-linux-gnu/libzstd.so.1.5.5
pipewire 1684749 tmoazzam  mem       REG              259,2   198584  1312299 /usr/lib/aarch64-linux-gnu/liblzma.so.5.4.5
pipewire 1684749 tmoazzam  mem       REG              259,2   133136  1312298 /usr/lib/aarch64-linux-gnu/liblz4.so.1.9.4
pipewire 1684749 tmoazzam  mem       REG              259,2  1000536  1312239 /usr/lib/aarch64-linux-gnu/libgcrypt.so.20.4.3
pipewire 1684749 tmoazzam  mem       REG              259,2    67704  1312191 /usr/lib/aarch64-linux-gnu/libcap.so.2.66
pipewire 1684749 tmoazzam  mem       REG              259,2   989464  1312625 /usr/lib/aarch64-linux-gnu/libsystemd.so.0.38.0
pipewire 1684749 tmoazzam  mem       REG              259,2    67600  1710929 /usr/lib/aarch64-linux-gnu/spa-0.2/support/libspa-journal.so
pipewire 1684749 tmoazzam  mem       REG              259,2   591800  1349606 /usr/lib/aarch64-linux-gnu/libm.so.6
pipewire 1684749 tmoazzam  mem       REG              259,2   133208  1710930 /usr/lib/aarch64-linux-gnu/spa-0.2/support/libspa-support.so
pipewire 1684749 tmoazzam  mem       REG              259,2 17040384  1319504 /usr/lib/locale/locale-archive
pipewire 1684749 tmoazzam  mem       REG              259,2  1722920  1349603 /usr/lib/aarch64-linux-gnu/libc.so.6
pipewire 1684749 tmoazzam  mem       REG              259,2   920240  1352238 /usr/lib/aarch64-linux-gnu/libpipewire-0.3.so.0.1005.0
pipewire 1684749 tmoazzam  mem       REG              259,2   203968  1349600 /usr/lib/aarch64-linux-gnu/ld-linux-aarch64.so.1
pipewire 1684749 tmoazzam  DEL       REG                0,1             31559 /memfd:pipewire-memfd:flags=0x0000000f,type=2,size=2312
pipewire 1684749 tmoazzam  DEL       REG                0,1             31558 /memfd:pipewire-memfd:flags=0x0000000f,type=2,size=2312
pipewire 1684749 tmoazzam  DEL       REG                0,1             31557 /memfd:pipewire-memfd:flags=0x0000000f,type=2,size=2312
pipewire 1684749 tmoazzam  mem       REG              259,2    27028  1349592 /usr/lib/aarch64-linux-gnu/gconv/gconv-modules.cache
pipewire 1684749 tmoazzam    0r      CHR                1,3      0t0        6 /dev/null
pipewire 1684749 tmoazzam    1u     unix 0xffff05a924cd5c00      0t0 12226707 type=STREAM (CONNECTED)
pipewire 1684749 tmoazzam    2u     unix 0xffff05a924cd5c00      0t0 12226707 type=STREAM (CONNECTED)
pipewire 1684749 tmoazzam    3u     unix 0xffff05a716bff400      0t0 12230837 /run/user/1003/pipewire-0 type=STREAM (LISTEN)
pipewire 1684749 tmoazzam    4u     unix 0xffff05a716bfe000      0t0 12230839 /run/user/1003/pipewire-0-manager type=STREAM (LISTEN)
pipewire 1684749 tmoazzam    5u  a_inode               0,16        0     1076 [eventpoll:3,4,6,8,9,13,20,22,23,24,26,27,29,31,32,33,43,44]
pipewire 1684749 tmoazzam    6u  a_inode               0,16        0     1076 [eventfd:379]
pipewire 1684749 tmoazzam    7u  a_inode               0,16        0     1076 [eventfd:380]
pipewire 1684749 tmoazzam    8u  a_inode               0,16        0     1076 [signalfd]
pipewire 1684749 tmoazzam    9u  a_inode               0,16        0     1076 [signalfd]
pipewire 1684749 tmoazzam   10u  a_inode               0,16        0     1076 [eventpoll:11,34,37,40]
pipewire 1684749 tmoazzam   11u  a_inode               0,16        0     1076 [eventfd:381]
pipewire 1684749 tmoazzam   12u  a_inode               0,16        0     1076 [eventfd:382]
pipewire 1684749 tmoazzam   13u  a_inode               0,16        0     1076 [eventfd:383]
pipewire 1684749 tmoazzam   14u     unix 0xffff05a924cd0800      0t0 12226713 type=STREAM (CONNECTED)
pipewire 1684749 tmoazzam   15u  a_inode               0,16        0     1076 [eventpoll:16,18]
pipewire 1684749 tmoazzam   16u  a_inode               0,16        0     1076 [eventfd:401]
pipewire 1684749 tmoazzam   17u  a_inode               0,16        0     1076 [eventfd:403]
pipewire 1684749 tmoazzam   18u  a_inode               0,16        0     1076 [eventfd:404]
pipewire 1684749 tmoazzam   19rW     REG              0,127        0      118 /run/user/1003/pipewire-0.lock
pipewire 1684749 tmoazzam   20u  a_inode               0,16        0     1076 [eventfd:407]
pipewire 1684749 tmoazzam   21rW     REG              0,127        0      119 /run/user/1003/pipewire-0-manager.lock
pipewire 1684749 tmoazzam   22u  a_inode               0,16        0     1076 [eventfd:408]
pipewire 1684749 tmoazzam   23u  a_inode               0,16        0     1076 [eventfd:409]
pipewire 1684749 tmoazzam   24u  a_inode               0,16        0     1076 [eventfd:411]
pipewire 1684749 tmoazzam   25u     unix 0xffff05a924cd3400      0t0 12226717 type=STREAM (CONNECTED)
pipewire 1684749 tmoazzam   26u     unix 0xffff05a924cd3400      0t0 12226717 type=STREAM (CONNECTED)
pipewire 1684749 tmoazzam   27u     unix 0xffff05a924cd3400      0t0 12226717 type=STREAM (CONNECTED)
pipewire 1684749 tmoazzam   28u     unix 0xffff05a716bfa800      0t0 12230883 type=DGRAM (UNCONNECTED)
pipewire 1684749 tmoazzam   29u  a_inode               0,16        0     1076 [eventfd:412]
pipewire 1684749 tmoazzam   30u     unix 0xffff05a924cd2000      0t0 12226718 type=STREAM (CONNECTED)
pipewire 1684749 tmoazzam   31u     unix 0xffff05a924cd2000      0t0 12226718 type=STREAM (CONNECTED)
pipewire 1684749 tmoazzam   32u     unix 0xffff05a924cd2000      0t0 12226718 type=STREAM (CONNECTED)
pipewire 1684749 tmoazzam   33u     unix 0xffff05a706633c00      0t0 12230884 /run/user/1003/pipewire-0 type=STREAM (CONNECTED)
pipewire 1684749 tmoazzam   34u  a_inode               0,16        0     1076 [timerfd]
pipewire 1684749 tmoazzam   35u  a_inode               0,16        0     1076 [eventfd:415]
pipewire 1684749 tmoazzam   36u      REG                0,1     2312    31557 /memfd:pipewire-memfd:flags=0x0000000f,type=2,size=2312 (deleted)
pipewire 1684749 tmoazzam   37u  a_inode               0,16        0     1076 [timerfd]
pipewire 1684749 tmoazzam   38u  a_inode               0,16        0     1076 [eventfd:413]
pipewire 1684749 tmoazzam   39u      REG                0,1     2312    31558 /memfd:pipewire-memfd:flags=0x0000000f,type=2,size=2312 (deleted)
pipewire 1684749 tmoazzam   40u  a_inode               0,16        0     1076 [timerfd]
pipewire 1684749 tmoazzam   41u  a_inode               0,16        0     1076 [eventfd:416]
pipewire 1684749 tmoazzam   42u      REG                0,1     2312    31559 /memfd:pipewire-memfd:flags=0x0000000f,type=2,size=2312 (deleted)
pipewire 1684749 tmoazzam   43u     unix 0xffff05b02b142800      0t0 12217878 /run/user/1003/pipewire-0 type=STREAM (CONNECTED)
pipewire 1684749 tmoazzam   44u     unix 0xffff05b02b143c00      0t0 12217879 /run/user/1003/pipewire-0 type=STREAM (CONNECTED)
root@spark-da4d:~/vllm_env_dir/vllm_env# ps -o pid,user,lstart,etime,stat,cmd -p 1684736,1684749,1684750,1684751,1684752,1684753,1684772,1684826
    PID USER                      STARTED     ELAPSED STAT CMD
1684736 tmoazzam Fri Jul 24 07:40:50 2026       30:03 Ss   /usr/lib/systemd/systemd --user
1684749 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ssl  /usr/bin/pipewire
1684750 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ssl  /usr/bin/pipewire -c filter-chain.conf
1684751 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ssl  /snap/snapd-desktop-integration/396/usr/bin/user-session-helper /snap/snapd-desktop-integration/396/usr/bin/snapd-desktop-integration
1684752 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ssl  /usr/bin/wireplumber
1684753 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ssl  /usr/bin/pipewire-pulse
1684772 tmoazzam Fri Jul 24 07:40:50 2026       30:02 Ss   /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
1684826 tmoazzam Fri Jul 24 07:40:51 2026       30:02 Ssl  /usr/libexec/xdg-document-portal
root@spark-da4d:~/vllm_env_dir/vllm_env# 
---------------------------------------------------------dgx------------------------------------------------------------------------------
root@AI-PC1:/home/famai01# cat /proc/2626283/cmdline | tr '\0' ' '
/home/famai01/.venv/bin/python3 /home/famai01/.venv/bin/vllm serve openai/gpt-oss-20b --host 0.0.0.0 --port 8000 --max-model-len 32768 --gpu-memory-utilization 0.55 --max-num-seqs 128 --enable-prefix-caching root
root@AI-PC1:/home/famai01# ps -fp 2626283
UID          PID    PPID  C STIME TTY          TIME CMD
famai01  2626283       1  1 Jul16 ?        02:30:06 /home/famai01/.venv/bin/python3 /home/famai01/.venv/bin/vllm serve openai/gpt-oss-20b --host 0.0.0.0 --port 8000 --max-model-len 32768 --gpu-memory-utilization 
root@AI-PC1:/home/famai01# 




------------------------

TAHA MOAZZAM
AI/ML Engineer | Full-Stack Developer | Startup Founder & COO
Cybersecurity Undergraduate (Graduating 2027)
PROFESSIONAL SUMMARY
Innovative CS-background AI/ML Engineer, Full-Stack Developer, and Startup COO with strong foundations in Data Structures, Algorithms, and Big O complexity analysis. Proven expertise in architecting custom PyTorch frameworks, high-precision RAG systems, and production-grade AI voice/email agents. Skilled in leveraging enterprise GPU infrastructure (NVIDIA DGX, A100, RTX 6000) for large-scale distributed computing and diagnosing complex memory leaks in high-load software pipelines.
PROFESSIONAL EXPERIENCE
Startup Founder & Chief Operating Officer (COO)
 Leadership & Strategy: Spearheaded company vision, product architecture, and end-to-end technical execution across high-performance AI implementations.
 Operations & Analytics: Developed comprehensive tracking architectures, including custom Excel progress frameworks, to monitor system performance, operational workflows, and project timelines.
AI/ML Engineer
 Architecture & Engineering: Designed and deployed production-grade AI models, local LLM integrations, and custom autonomous agents tailored for high-throughput enterprise applications.
VeloxiaAI
 Former Developer: Contributed to core AI software architecture, custom script development, and system integrations to scale generative AI capabilities.
FAM Revtech / FNA Global
 Management Trainee Officer (MTO) / Technical Team Member: Managed cross-functional operational workflows, integrated live databases with CRM systems, and optimized enterprise tech infrastructure.
CORE TECHNICAL SKILLS
 CS Foundations & Algorithms: Data Structures & Algorithms (DSA), Big O Complexity Analysis, Space/Time Optimization, Memory Management.
 AI, ML & NLP: PyTorch (Custom Builds), RAG Systems, Rule Matching, LLM Validation, Fine-tuning, Local LLM Deployment (LM Studio, LLaMA), Deepfake Detection, Autonomous Voice & Email Agents.
 High-Performance Computing: NVIDIA DGX Clusters, NVIDIA A100, RTX 6000 PRO, RTX 5090 (32GB), Apache Spark, Thermal/Hardware Optimization (ThrottleStop, Peltier Systems).
 Backend & Systems Development: Python, FastAPI, RESTful APIs, Webhooks Automation, Database & CRM Integration, Telecommunications/Call Forwarding Infrastructure.
 Frontend & Web Development: HTML/CSS/JavaScript, Three.js (3D Interactive Storytelling), UI/UX Architecture.
 Optimization & Debugging: Memory Leak Remediation, Profiling & Resource Clogging Optimization, Real-time System Analytics.
KEY PROJECTS & TECHNICAL ACHIEVEMENTS
 Custom PyTorch Engine for DGX & Spark: Engineered and built a customized version of the PyTorch framework specifically optimized for distributed computing environments on NVIDIA DGX clusters and Apache Spark.
 High-Precision RAG Systems: Developed advanced Retrieval-Augmented Generation (RAG) models featuring strict LLM validations and rule matching; curated specialized prediction datasets achieving over 85% Precision, Recall, and F1 Scores.
 Autonomous AI Voice & Email Calling Agent: Built and deployed a production-grade voice agent using Vapi and cloud hosting, connected directly to an automated emailing agent to seamlessly trigger real-time email workflows during or post-calls. Configured physical SIM integration via cloud call forwarding.
 Automated AI Storyteller & Pipeline Optimization: Architected an end-to-end tool generating AI images, dynamic scripting, and 60-second narrative videos. Diagnosed and permanently fixed complex memory clogging/leak issues during high-load processing.
 Deepfake Detection System: Designed a specialized computer vision and AI model capable of identifying manipulated media and deepfakes, aligning advanced AI with Cybersecurity principles.
 Automated Medical Billing System: Developed core modules for automated medical billing workflows integrated with ICD (International Classification of Diseases) and CPT (Current Procedural Terminology) codes.
 Interactive 3D Web Experience: Built an immersive, storytelling web application using Three.js integrated with a responsive frontend and FastAPI backend.
 Software Applications & Utilities: Developed practical applications including the 'Move Ease' lodging app, 'Bus Tokeniser', and a custom GIF Maker utility tool.
EDUCATION
Bachelor’s Degree in Cybersecurity (CS Background)
 Expected Completion: 2027
 Core CS & Security Domains: Data Structures & Algorithms, Network Behavior Analysis, Digital Forensics, Shell Scripting, Systems Security.
