from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Category, Post, Tag, PostTag
from django.utils.text import slugify
from django.utils import timezone


class Command(BaseCommand):
    help = 'Populate database with sample blog data'

    def handle(self, *args, **options):
        # Get or create admin user
        admin_user, created = User.objects.get_or_create(
            username='felixcole',
            defaults={
                'email': 'admin@blogportfolio.com',
                'is_staff': True,
                'is_superuser': True,
            }
        )

        # Create categories
        categories_data = [
            {'name': 'Business Solutions', 'description': 'Innovative business strategies and consulting'},
            {'name': 'Technology', 'description': 'Latest technology trends and insights'},
            {'name': 'Design', 'description': 'Creative design and branding solutions'},
            {'name': 'Marketing', 'description': 'Digital marketing and growth strategies'},
        ]

        categories = {}
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'slug': slugify(cat_data['name']),
                    'description': cat_data['description']
                }
            )
            categories[cat_data['name']] = cat

        # Create tags
        tags_data = ['Corporate', 'Strategy', 'Innovation', 'Digital', 'Growth', 'Success', 'Design', 'Marketing', 'Technology']
        tags = {}
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(
                name=tag_name,
                defaults={'slug': slugify(tag_name)}
            )
            tags[tag_name] = tag

        # Create sample posts
        posts_data = [
            {
                'title': 'Transforming Digital Landscapes: A Strategic Approach',
                'category': 'Business Solutions',
                'excerpt': 'Discover how modern businesses are revolutionizing their digital presence through innovative strategies and cutting-edge technologies.',
                'content': '''In today's rapidly evolving digital environment, organizations must adapt to stay competitive. This comprehensive guide explores the latest strategies for digital transformation, including:

• Cloud Migration and Infrastructure Modernization
• Data-Driven Decision Making
• Customer Experience Optimization
• Process Automation and AI Integration

Success requires a holistic approach that combines technology with strategic planning and organizational change management.

Our case studies show that companies implementing these strategies see 40-60% improvements in operational efficiency and 25-35% increases in customer satisfaction within the first year.

Whether you're just beginning your digital journey or looking to accelerate your transformation, our team of experts is ready to guide you through every step.''',
                'tags': ['Corporate', 'Strategy', 'Innovation']
            },
            {
                'title': 'The Future of Corporate Design: Trends for 2024',
                'category': 'Design',
                'excerpt': 'Explore the latest design trends shaping corporate identities and brand experiences in the modern marketplace.',
                'content': '''Design is more than aesthetics—it\'s a strategic tool that communicates your brand\'s values and mission. In 2024, we\'re seeing several exciting trends emerge:

**Minimalist Elegance**
Less is more. Clean, bold typography and generous whitespace create impactful designs that stand out.

**Sustainable Design**
Eco-conscious brands are leading the way with sustainable materials and ethical practices reflected in their visual identity.

**Interactive Experiences**
Dynamic, interactive design elements create engaging user experiences that build deeper connections with audiences.

**Cultural Authenticity**
Brands are celebrating diversity and authenticity, moving away from one-size-fits-all approaches.

Companies that embrace these trends see stronger brand recognition, increased customer loyalty, and improved market positioning.''',
                'tags': ['Design', 'Innovation', 'Growth']
            },
            {
                'title': 'Data-Driven Marketing: Maximizing Your ROI',
                'category': 'Marketing',
                'excerpt': 'Learn how to leverage data analytics to create targeted marketing campaigns that deliver measurable results.',
                'content': '''The modern marketing landscape demands precision and accountability. Here\'s how leading companies are using data to drive success:

**Personalization at Scale**
Advanced analytics enable personalized customer journeys that significantly improve conversion rates and customer lifetime value.

**Predictive Analytics**
AI-powered tools help predict customer behavior, allowing you to stay ahead of market trends.

**Multi-Channel Attribution**
Understanding which channels drive the most value helps optimize your marketing spend and maximize ROI.

**Real-Time Optimization**
Continuous A/B testing and optimization ensure your campaigns perform at their peak.

Companies that implement data-driven marketing strategies see:
- 20-40% improvement in conversion rates
- 25-30% reduction in customer acquisition costs
- 15-25% increase in customer lifetime value

The key is choosing the right tools and having a team that understands both data and marketing strategy.''',
                'tags': ['Marketing', 'Digital', 'Success']
            },
            {
                'title': 'Enterprise Technology Solutions: Beyond the Basics',
                'category': 'Technology',
                'excerpt': 'Discover advanced technology solutions that provide competitive advantages for enterprise organizations.',
                'content': '''Modern enterprises face unprecedented technological challenges and opportunities. Here\'s what leading organizations are doing:

**Cloud-Native Architecture**
Migrating to cloud-native technologies provides scalability, reliability, and cost efficiency that on-premise solutions can\'t match.

**Cybersecurity Excellence**
With threats evolving daily, comprehensive security strategies are non-negotiable for protecting valuable business assets.

**API-First Development**
Building systems around APIs enables flexibility, integration capabilities, and faster time to market.

**DevOps and Continuous Integration**
Modern development practices reduce time-to-market by 50-70% while maintaining quality standards.

**AI and Machine Learning**
These technologies are no longer optional—they\'re essential for competitive advantage in most industries.

The organizations succeeding in this landscape invest in both technology and talent, recognizing that the best tools are only as good as the teams wielding them.''',
                'tags': ['Technology', 'Innovation', 'Digital']
            },
            {
                'title': 'Building High-Performance Teams: The Corporate Advantage',
                'category': 'Business Solutions',
                'excerpt': 'Strategies for creating and nurturing teams that drive innovation and deliver exceptional results.',
                'content': '''In today\'s competitive landscape, your team is your greatest asset. Here\'s how to build teams that perform at their peak:

**Recruitment Excellence**
Hire for potential and cultural fit, not just experience. The best teams have diverse perspectives and complementary skills.

**Continuous Learning**
Invest in professional development. Companies that prioritize learning see 34% higher productivity and better talent retention.

**Psychological Safety**
Teams that feel safe to take risks, make mistakes, and voice ideas without fear perform 22% better.

**Clear Communication**
Transparent, open communication builds trust and alignment across the organization.

**Recognition and Growth**
Celebrate wins, provide constructive feedback, and create clear paths for career development.

**Work-Life Balance**
Sustainable performance requires supporting employee wellbeing and preventing burnout.

Teams built on these principles consistently outperform their peers, delivering exceptional results for the organization.''',
                'tags': ['Corporate', 'Strategy', 'Success']
            },
            {
                'title': 'Sustainability in Corporate Practice: More Than a Trend',
                'category': 'Business Solutions',
                'excerpt': 'How leading companies are integrating sustainability into their core business strategy for long-term success.',
                'content': '''Sustainability is no longer a marketing gimmick—it\'s a business imperative. Here\'s why leading companies are making it central to their strategy:

**Risk Mitigation**
Sustainable practices reduce exposure to regulatory, operational, and market risks.

**Cost Savings**
Efficiency improvements from sustainable practices often pay for themselves through reduced waste and energy costs.

**Brand Value**
70% of consumers prefer brands that demonstrate environmental and social responsibility.

**Talent Attraction**
Purpose-driven companies attract and retain top talent more effectively.

**Innovation Catalyst**
Sustainability goals drive innovation, leading to new products, services, and business models.

**Investor Confidence**
ESG performance increasingly influences investment decisions and access to capital.

The path to sustainability isn\'t just about reducing harm—it\'s about creating value. Organizations that embrace sustainable practices are positioning themselves for long-term success in an increasingly conscious marketplace.''',
                'tags': ['Corporate', 'Growth', 'Innovation']
            },
        ]

        # Create posts
        for post_data in posts_data:
            category = categories[post_data['category']]
            slug = slugify(post_data['title'])
            
            post, created = Post.objects.get_or_create(
                slug=slug,
                defaults={
                    'title': post_data['title'],
                    'author': admin_user,
                    'category': category,
                    'excerpt': post_data['excerpt'],
                    'content': post_data['content'],
                    'status': 'published',
                    'published_at': timezone.now(),
                }
            )

            # Add tags to post
            for tag_name in post_data.get('tags', []):
                tag = tags[tag_name]
                PostTag.objects.get_or_create(post=post, tag=tag)

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created post: {post.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Post already exists: {post.title}'))

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))