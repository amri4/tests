
# Discord.py Templates

This folder contains various templates and examples for common Discord.py patterns and features.

## Available Templates

### 1. **basic_command.py**
Simple text commands using the `@bot.command()` decorator.
- Basic greeting command
- Ping/latency command
- Echo command that repeats user input

### 2. **slash_command.py**
Modern Discord slash commands (application commands) for Discord.py 2.0+.
- Creating slash commands with `@bot.tree.command()`
- Using parameters and descriptions
- User information slash command
- Dice roll command

### 3. **cogs_command.py**
Organizing commands into Cogs for better code structure and modularity.
- ModerationCog: Kick, ban, and mute commands
- FunCog: Joke and 8ball commands
- Loading cogs into the bot

### 4. **event_handlers.py**
Various Discord.py events for responding to Discord activity.
- `on_ready()`: Bot connection event
- `on_message()`: Message events
- `on_message_edit()` / `on_message_delete()`: Message modification
- `on_member_join()` / `on_member_remove()`: Member events
- `on_reaction_add()` / `on_reaction_remove()`: Reaction events
- `on_guild_role_create()` / `on_guild_role_delete()`: Role events
- `on_guild_channel_create()` / `on_guild_channel_delete()`: Channel events
- `on_guild_join()` / `on_guild_remove()`: Guild events

### 5. **embeds.py**
Creating rich embedded messages with Discord Embeds.
- Basic embed creation
- Advanced embeds with multiple fields
- User information embeds
- Colored embeds
- Thumbnails and images
- Author and footer information

### 6. **buttons_and_select.py**
Interactive UI components (requires Discord.py 2.0+).
- Simple button views
- Multi-button voting system
- Select menu with options
- Role selection menus
- Button callbacks and interactions

### 7. **context_menu.py**
Right-click context menu commands (requires Discord.py 2.0+).
- User context menus (right-click on user)
- Message context menus (right-click on message)
- User info display
- Message quoting
- Report functionality

### 8. **permissions_and_checks.py**
Permission-based command restrictions and checks.
- `@commands.has_permissions()`: Permission checks
- `@commands.has_role()`: Role-based access
- `@commands.has_any_role()`: Multiple role options
- Custom check decorators
- `@commands.is_nsfw()`: NSFW channel requirement
- `@commands.guild_only()` / `@commands.dm_only()`: Channel type restrictions
- Error handling for permission failures

### 9. **database_integration.py**
Integrating SQLite database with Discord.py bot.
- Database initialization and setup
- User tracking and statistics
- Guild-specific settings
- Message counting and leaderboards
- Custom user statistics commands

---

## Key Discord.py Concepts and References

### Core Classes and Objects

- **`discord.Client`**: Base class for interacting with Discord API
- **`discord.ext.commands.Bot`**: Bot subclass with command functionality
- **`discord.Guild`**: Represents a Discord server
- **`discord.Member`**: Represents a server member
- **`discord.User`**: Represents a Discord user
- **`discord.Message`**: Represents a Discord message
- **`discord.Channel`**: Base class for channels
- **`discord.TextChannel`**: Text channel representation
- **`discord.Role`**: Represents a server role
- **`discord.Embed`**: Rich embedded message object

### Decorators and Utilities

- **`@bot.event`**: Register event handlers for bot events
- **`@bot.command()`**: Create text commands
- **`@bot.tree.command()`**: Create slash commands (2.0+)
- **`@bot.tree.context_menu()`**: Create context menu commands (2.0+)
- **`@commands.has_permissions()`**: Check user permissions
- **`@commands.has_role()`**: Require specific role
- **`@commands.has_any_role()`**: Require any of multiple roles
- **`@commands.is_nsfw()`**: NSFW channel requirement
- **`@commands.guild_only()`**: Only work in servers
- **`@commands.dm_only()`**: Only work in DMs
- **`@commands.cooldown()`**: Rate limiting

### Common Events

- **`on_ready()`**: Bot successfully connected to Discord
- **`on_message(message)`**: New message sent
- **`on_message_edit(before, after)`**: Message edited
- **`on_message_delete(message)`**: Message deleted
- **`on_member_join(member)`**: Member joined server
- **`on_member_remove(member)`**: Member left server
- **`on_member_update(before, after)`**: Member profile updated
- **`on_reaction_add(reaction, user)`**: Reaction added
- **`on_reaction_remove(reaction, user)`**: Reaction removed
- **`on_guild_role_create(role)`**: Role created
- **`on_guild_channel_create(channel)`**: Channel created
- **`on_guild_join(guild)`**: Bot joined server
- **`on_error(event, *args, **kwargs)`**: Error occurred

### UI Components (Discord.py 2.0+)

- **`discord.ui.Button`**: Interactive button component
- **`discord.ui.Select`**: Select menu component
- **`discord.ui.View`**: Container for interactive components
- **`discord.ui.Modal`**: Form modal for user input
- **`discord.Interaction`**: Represents button/menu interaction

### Common Attributes and Methods

#### Message/Context Attributes
- **`ctx.author`**: User who sent message
- **`ctx.guild`**: Server the command was used in
- **`ctx.channel`**: Channel where command was used
- **`ctx.message`**: The message object

#### User/Member Methods
- **`member.ban()`**: Ban user from server
- **`member.kick()`**: Kick user from server
- **`member.add_roles(*roles)`**: Add roles to member
- **`member.remove_roles(*roles)`**: Remove roles from member
- **`user.avatar.url`**: User's avatar URL

#### Channel Methods
- **`channel.send()`**: Send message to channel
- **`channel.purge()`**: Delete messages in bulk
- **`channel.set_permissions()`**: Set channel permissions

#### Message Methods
- **`message.react()`**: Add emoji reaction
- **`message.delete()`**: Delete the message
- **`message.edit()`**: Edit message content

### Intents

Intents enable specific events and data:
- **`discord.Intents.default()`**: Basic intents
- **`message_content`**: Access message text content
- **`members`**: Member-related events
- **`guilds`**: Guild-related events
- **`reactions`**: Reaction events
- **`presences`**: User presence updates

### Response Methods

- **`await ctx.send()`**: Send message in command channel
- **`await interaction.response.send_message()`**: Respond to interaction
- **`await interaction.response.defer()`**: Defer response
- **`await bot.wait_for()`**: Wait for specific event
- **`await member.send()`**: Send DM to user

### Error Handling

- **`@bot.event async def on_command_error(ctx, error)`**: Handle command errors
- **`commands.MissingPermissions`**: User missing permissions
- **`commands.MissingRole`**: User missing required role
- **`commands.NotOwner`**: User is not bot owner
- **`commands.NSFWChannelRequired`**: Command requires NSFW channel
- **`commands.NoPrivateMessage`**: Command cannot be used in DMs

### Best Practices

1. **Use Intents properly** to reduce memory and enable necessary events
2. **Handle errors gracefully** with try-except and error event handlers
3. **Use Cogs** to organize commands into modules
4. **Implement permission checks** for sensitive commands
5. **Rate limit commands** with `@commands.cooldown()` when needed
6. **Use embeds** for better formatted responses
7. **Store data responsibly** using databases for persistence
8. **Respond to interactions quickly** to avoid timeout
9. **Validate user input** before processing
10. **Document commands** with docstrings and help text

---

## Getting Started

1. Install discord.py: `pip install discord.py`
2. Choose a template that fits your needs
3. Copy the code and modify as needed
4. Add your bot token: `bot.run('YOUR_TOKEN_HERE')`
5. Run your bot!

## Resources

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Discord API Documentation](https://discord.com/developers/docs)
