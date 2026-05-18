import discord
from discord.ext import commands
from typing import Optional, List, Union

# =========================================
# MESSAGING
# =========================================

async def send_message(channel, content: str, embed: Optional[discord.Embed] = None):
    """Send a message to a channel"""
    return await channel.send(content=content, embed=embed)

async def send_embed(channel, title: str, description: str, color: discord.Color = discord.Color.blue()):
    """Send an embedded message to a channel"""
    embed = discord.Embed(title=title, description=description, color=color)
    return await channel.send(embed=embed)

async def send_dm(user, content: str, embed: Optional[discord.Embed] = None):
    """Send a direct message to a user"""
    return await user.send(content=content, embed=embed)

async def edit_message(message, content: str = None, embed: Optional[discord.Embed] = None):
    """Edit an existing message"""
    return await message.edit(content=content, embed=embed)

async def delete_message(message):
    """Delete a message"""
    return await message.delete()

async def add_reaction(message, emoji: str):
    """Add a reaction to a message"""
    return await message.add_reaction(emoji)

async def remove_reaction(message, emoji: str, user):
    """Remove a reaction from a message"""
    return await message.remove_reaction(emoji, user)

async def clear_reactions(message):
    """Clear all reactions from a message"""
    return await message.clear_reactions()

# =========================================
# MEMBER MANAGEMENT
# =========================================

async def kick_member(member, reason: str = None):
    """Kick a member from the guild"""
    return await member.kick(reason=reason)

async def ban_member(member, reason: str = None, delete_message_days: int = 0):
    """Ban a member from the guild"""
    return await member.ban(reason=reason, delete_message_seconds=delete_message_days*86400)

async def unban_member(guild, user):
    """Unban a user from the guild"""
    return await guild.unban(user)

async def add_roles(member, *roles):
    """Add one or more roles to a member"""
    return await member.add_roles(*roles)

async def remove_roles(member, *roles):
    """Remove one or more roles from a member"""
    return await member.remove_roles(*roles)

async def mute_member(member, duration_seconds: int = None):
    """Mute a member (timeout)"""
    timeout = discord.utils.utcnow() + discord.utils.datetime.timedelta(seconds=duration_seconds) if duration_seconds else None
    return await member.timeout(timeout)

async def unmute_member(member):
    """Unmute a member (remove timeout)"""
    return await member.timeout(None)

def has_role(member, role_name: str) -> bool:
    """Check if a member has a specific role"""
    return any(role.name.lower() == role_name.lower() for role in member.roles)

def has_permission(member, permission: str) -> bool:
    """Check if a member has a specific permission"""
    return getattr(member.guild_permissions, permission, False)

# =========================================
# ROLE MANAGEMENT
# =========================================

async def create_role(guild, name: str, color: discord.Color = discord.Color.default(), reason: str = None):
    """Create a new role in the guild"""
    return await guild.create_role(name=name, color=color, reason=reason)

async def delete_role(role, reason: str = None):
    """Delete a role from the guild"""
    return await role.delete(reason=reason)

async def edit_role(role, name: str = None, color: discord.Color = None, permissions: discord.Permissions = None):
    """Edit a role's properties"""
    return await role.edit(name=name, color=color, permissions=permissions)

def get_role(guild, role_name: str) -> Optional[discord.Role]:
    """Get a role by name"""
    return discord.utils.get(guild.roles, name=role_name)

def get_role_by_id(guild, role_id: int) -> Optional[discord.Role]:
    """Get a role by ID"""
    return guild.get_role(role_id)

# =========================================
# CHANNEL MANAGEMENT
# =========================================

async def create_text_channel(guild, name: str, category: discord.CategoryChannel = None, reason: str = None):
    """Create a text channel"""
    return await guild.create_text_channel(name=name, category=category, reason=reason)

async def create_voice_channel(guild, name: str, category: discord.CategoryChannel = None, reason: str = None):
    """Create a voice channel"""
    return await guild.create_voice_channel(name=name, category=category, reason=reason)

async def delete_channel(channel, reason: str = None):
    """Delete a channel"""
    return await channel.delete(reason=reason)

async def edit_channel(channel, name: str = None, topic: str = None, slowmode_delay: int = None):
    """Edit a channel's properties"""
    return await channel.edit(name=name, topic=topic, slowmode_delay=slowmode_delay)

def get_channel(guild, channel_name: str) -> Optional[discord.TextChannel]:
    """Get a channel by name"""
    return discord.utils.get(guild.channels, name=channel_name)

def get_channel_by_id(guild, channel_id: int) -> Optional[discord.TextChannel]:
    """Get a channel by ID"""
    return guild.get_channel(channel_id)

async def purge_channel(channel, limit: int = 100, check=None):
    """Delete multiple messages from a channel"""
    return await channel.purge(limit=limit, check=check)

# =========================================
# USER & MEMBER INFORMATION
# =========================================

def get_member(guild, member_name: str) -> Optional[discord.Member]:
    """Get a member by name"""
    return discord.utils.get(guild.members, name=member_name)

def get_member_by_id(guild, member_id: int) -> Optional[discord.Member]:
    """Get a member by ID"""
    return guild.get_member(member_id)

def is_bot_owner(user_id: int, bot_owner_id: int) -> bool:
    """Check if user is the bot owner"""
    return user_id == bot_owner_id

def get_member_info(member) -> dict:
    """Get comprehensive member information"""
    return {
        "id": member.id,
        "name": member.name,
        "display_name": member.display_name,
        "avatar": member.avatar.url if member.avatar else None,
        "roles": [role.name for role in member.roles],
        "joined_at": member.joined_at,
        "created_at": member.created_at,
        "is_bot": member.bot,
        "top_role": member.top_role.name,
        "guild": member.guild.name,
    }

# =========================================
# EMBED UTILITIES
# =========================================

def create_embed(title: str = None, description: str = None, color: discord.Color = discord.Color.blue(), url: str = None) -> discord.Embed:
    """Create a basic embed"""
    return discord.Embed(title=title, description=description, color=color, url=url)

def add_field_to_embed(embed: discord.Embed, name: str, value: str, inline: bool = False) -> discord.Embed:
    """Add a field to an embed"""
    embed.add_field(name=name, value=value, inline=inline)
    return embed

def set_embed_thumbnail(embed: discord.Embed, url: str) -> discord.Embed:
    """Set embed thumbnail"""
    embed.set_thumbnail(url=url)
    return embed

def set_embed_image(embed: discord.Embed, url: str) -> discord.Embed:
    """Set embed image"""
    embed.set_image(url=url)
    return embed

def set_embed_author(embed: discord.Embed, name: str, icon_url: str = None, url: str = None) -> discord.Embed:
    """Set embed author"""
    embed.set_author(name=name, icon_url=icon_url, url=url)
    return embed

def set_embed_footer(embed: discord.Embed, text: str, icon_url: str = None) -> discord.Embed:
    """Set embed footer"""
    embed.set_footer(text=text, icon_url=icon_url)
    return embed

def create_user_embed(member: discord.Member) -> discord.Embed:
    """Create an embed displaying user information"""
    embed = discord.Embed(
        title=f"User Info - {member.display_name}",
        description=member.mention,
        color=member.color
    )
    embed.set_thumbnail(url=member.avatar.url if member.avatar else None)
    embed.add_field(name="User ID", value=member.id, inline=True)
    embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Roles", value=", ".join([r.mention for r in member.roles[1:]]) or "None", inline=False)
    embed.add_field(name="Is Bot", value=member.bot, inline=True)
    return embed

# =========================================
# PERMISSION UTILITIES
# =========================================

def create_permissions(send_messages: bool = True, manage_messages: bool = False, manage_roles: bool = False, 
                      manage_channels: bool = False, administrator: bool = False) -> discord.Permissions:
    """Create a Permissions object"""
    return discord.Permissions(
        send_messages=send_messages,
        manage_messages=manage_messages,
        manage_roles=manage_roles,
        manage_channels=manage_channels,
        administrator=administrator
    )

async def set_channel_permissions(channel, target: Union[discord.Role, discord.Member], permissions: discord.Permissions):
    """Set permissions for a role or member in a channel"""
    return await channel.set_permissions(target, overwrite=permissions)

async def remove_channel_permissions(channel, target: Union[discord.Role, discord.Member]):
    """Remove permissions for a role or member in a channel"""
    return await channel.delete_permissions(target)

# =========================================
# GUILD UTILITIES
# =========================================

def get_guild_info(guild: discord.Guild) -> dict:
    """Get comprehensive guild information"""
    return {
        "id": guild.id,
        "name": guild.name,
        "owner": guild.owner.name if guild.owner else None,
        "members": guild.member_count,
        "channels": len(guild.channels),
        "roles": len(guild.roles),
        "created_at": guild.created_at,
        "icon": guild.icon.url if guild.icon else None,
        "region": str(guild.region) if hasattr(guild, 'region') else "N/A",
    }

async def get_guild_by_name(bot, guild_name: str) -> Optional[discord.Guild]:
    """Get a guild by name"""
    for guild in bot.guilds:
        if guild.name.lower() == guild_name.lower():
            return guild
    return None

# =========================================
# COLOR UTILITIES
# =========================================

def get_color(color_name: str) -> discord.Color:
    """Get a color by name"""
    colors = {
        "red": discord.Color.red(),
        "blue": discord.Color.blue(),
        "green": discord.Color.green(),
        "yellow": discord.Color.yellow(),
        "purple": discord.Color.purple(),
        "pink": discord.Color.magenta(),
        "orange": discord.Color.orange(),
        "white": discord.Color.from_rgb(255, 255, 255),
        "black": discord.Color.from_rgb(0, 0, 0),
        "gold": discord.Color.gold(),
        "teal": discord.Color.teal(),
        "navy": discord.Color.navy(),
    }
    return colors.get(color_name.lower(), discord.Color.blue())

def rgb_to_color(r: int, g: int, b: int) -> discord.Color:
    """Convert RGB values to a Discord color"""
    return discord.Color.from_rgb(r, g, b)

# =========================================
# WAIT FOR UTILITIES
# =========================================

async def wait_for_reaction(bot, message, user: discord.User = None, timeout: int = 60):
    """Wait for a reaction on a message"""
    try:
        def check(reaction, user_reacted):
            if user:
                return reaction.message.id == message.id and user_reacted == user
            return reaction.message.id == message.id
        
        reaction, reacted_user = await bot.wait_for('reaction_add', timeout=timeout, check=check)
        return reaction, reacted_user
    except:
        return None, None

async def wait_for_message(bot, user: discord.User, channel: discord.TextChannel = None, timeout: int = 60):
    """Wait for a message from a user"""
    try:
        def check(msg):
            if channel:
                return msg.author == user and msg.channel == channel
            return msg.author == user
        
        message = await bot.wait_for('message', timeout=timeout, check=check)
        return message
    except:
        return None

# =========================================
# LOGGING UTILITIES
# =========================================

async def log_action(channel: discord.TextChannel, action: str, user: discord.User, details: str = ""):
    """Log an action to a logging channel"""
    embed = discord.Embed(
        title=f"Action Logged: {action}",
        description=f"User: {user.mention}\n{details}",
        color=discord.Color.blue()
    )
    embed.set_footer(text=f"Timestamp: {discord.utils.utcnow()}")
    await channel.send(embed=embed)

# =========================================
# ERROR HANDLING
# =========================================

def format_error(error: Exception) -> str:
    """Format an error message"""
    return f"```\n{type(error).__name__}: {str(error)}\n```"

async def send_error(channel: discord.TextChannel, error: Exception, context: str = ""):
    """Send an error message to a channel"""
    embed = discord.Embed(
        title="❌ Error Occurred",
        description=f"**Error Type:** {type(error).__name__}\n**Message:** {str(error)}\n**Context:** {context}",
        color=discord.Color.red()
    )
    await channel.send(embed=embed)
