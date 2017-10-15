from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0133_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0133_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_4D7",          # 01, 1
        "Function_2_A04",          # 02, 2
        "Function_3_DF3",          # 03, 3
        "Function_4_1F37",         # 04, 4
        "Function_5_2588",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    ChrTalk(    #0
        0x101,
        "#1001FHello, Mr. Paddington!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        "#020FHow are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Oh, hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Can I help you with something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1015FErr, actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Estelle explained that she was looking for the stew recipe\x01",
            "she'd heard about from Radford.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #6
        0x101,
        (
            "#1011FMr. Paddington, you're about the\x01",
            "same age as Mr. Radford, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#020FAny chance you know anything\x01",
            "about that recipe?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #8
        0xFE,
        (
            "Hmm... I seem to recall somethin'\x01",
            "like that when I was young, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Unlike Radford, I've never had much\x01",
            "attachment to food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Couldn't tell you much about it,\x01",
            "sad to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1016FAwww. Darn.\x02\x03",

            "Just our luck, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35E")

    ChrTalk(    #12
        0x106,
        "#053FA swing and a miss.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E4")

    label("loc_35E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38D")

    ChrTalk(    #13
        0x108,
        "#070FA swing and a miss.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E4")

    label("loc_38D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BC")

    ChrTalk(    #14
        0x104,
        "#031FA swing and a miss.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E4")

    label("loc_3BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E4")

    ChrTalk(    #15
        0x105,
        "#045FThat's too bad.\x02",
    )

    CloseMessageWindow()

    label("loc_3E4")


    ChrTalk(    #16
        0xFE,
        "Sorry about that, kids.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#525FThat's quite all right. We'll keep\x01",
            "asking around.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #18
        0xFE,
        (
            "Hmm... I'd start with some of the\x01",
            "ladies in town, then, if I were you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "If they're about our age, they may\x01",
            "know how to make it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_28(0x75, 0x1, 0x100)
    Return()

    # Function_0_AA end

    def Function_1_4D7(): pass

    label("Function_1_4D7")

    EventBegin(0x0)
    Call(1, 5)

    ChrTalk(    #20
        0xA,
        "#6PGoddess, I beg of you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "#6PHelp me find a way to get closer\x01",
            "to that gorgeous woman...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1015F#4P...\x02\x03",

            "Ahem! Uhh, got a sec?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        "#6PHmm?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xA)

    ChrTalk(    #24
        0xA,
        "Oh, um, hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        "Are you from the guild, by any chance?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1006F#4PYep, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#020FWe saw your post on the board.\x01",
            "Would you be Anton?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xA,
        (
            "That's me! The one and only\x01",
            "Anton from the capital!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "And though we've only just met,\x01",
            "my request is fairly urgent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "I don't think the job'll be too hard,\x01",
            "though. What do you say?\x01",
            "Are you ready to hear me out?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79F")

    ChrTalk(    #31
        0x101,
        (
            "#1000F#4PSure thing.\x02\x03",

            "So, what is it you need us to do?\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)
    Jump("loc_A01")

    label("loc_79F")


    ChrTalk(    #32
        0x101,
        (
            "#1015F#4PSorry.\x02\x03",

            "We can't do it right this second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "*siiigh* I was afraid of that. I had a\x01",
            "nasty, sinking feeling I'd be turned\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    ChrTalk(    #34
        0xA,
        (
            "No one ever listens to what I have\x01",
            "to say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "They never have...and they probably\x01",
            "never will. Not as long as I live.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x101,
        (
            "#1016F#4PThat's, uh...a little dramatic,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x103,
        (
            "#020FWe haven't turned you down,\x01",
            "per se.\x02\x03",

            "Once we have more time, we'll\x01",
            "come back. We just need you to\x01",
            "wait for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        "I'll believe it when I see it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "Until then, I'll be waiting...\x01",
            "No lofty expectations here,\x01",
            "no sirree...\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x76, 0x1, 0x8000)

    label("loc_A01")

    EventEnd(0x0)
    Return()

    # Function_1_4D7 end

    def Function_2_A04(): pass

    label("Function_2_A04")

    EventBegin(0x0)
    Call(1, 5)

    ChrTalk(    #40
        0xA,
        "#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "#6PAm I dreaming? Are you the same\x01",
            "guys from before? From the Bracer\x01",
            "Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1002F#4PSure are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        "#6PSo...you came back for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        (
            "#6PHave you finally decided to take pity\x01",
            "on my plight? To aid me when no one\x01",
            "else would in this cold, lonely world?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "...Yes.\x01",                # 0
            "Nope. Nope. Nope.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C94")

    ChrTalk(    #45
        0x101,
        "#1006F#4POf course! That's what bracers do.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xA)

    ChrTalk(    #46
        0xA,
        "#6POhhhhhhhhh!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #47
        0xA,
        (
            "D-Do you mean it? You'll really\x01",
            "help me? Seriously?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1016F#4P(I'm starting to have second\x01",
            "thoughts on this...)\x02\x03",

            "#1011FSeriously. So what kind of job is it,\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)
    Jump("loc_DF0")

    label("loc_C94")


    ChrTalk(    #49
        0x101,
        (
            "#1007F#4PYeah...sorry. We still have a lot\x01",
            "of work ahead of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        "#6PHmmm... I see, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "#6PSo it's only now that you reveal\x01",
            "your true colors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1019F#4PC'mon, what's with the guilt trip?\x02\x03",

            "#1022FWe're coming back, you know.\x01",
            "We just need a little more time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "#6PSure you do. I'll be here, waiting...\x01",
            "Friendless and alone...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF0")

    EventEnd(0x0)
    Return()

    # Function_2_A04 end

    def Function_3_DF3(): pass

    label("Function_3_DF3")


    ChrTalk(    #54
        0xA,
        "R-Right! Well, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "I'd like you to gather ingredients \x01",
            "for a certain medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        "Errr... Here's a list of what I need.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #57
        (
            "\x07\x05Monster Carapace x5\x01",
            "Savory Pinion x5\x01",
            "Prickly Seed x5\x01",
            "Pearlglass x1\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #58
        0x103,
        (
            "#025FOkay, putting aside the monster bits...\x02\x03",

            "I'm not too familiar with what a\x01",
            "Pearlglass is, but it does sound\x01",
            "familiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        "Pearlglasses are river fish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xA,
        (
            "I need their livers to make the\x01",
            "medicine I want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        (
            "They're found primarily in freshwater\x01",
            "rivers with a lot of floating water plants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1015F#4PFreshwater... Plenty of plantlife...\x02\x03",

            "#1006F...All right, got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        "Done writing it down?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        (
            "G-Great! It's all you, then.\x01",
            "Don't let me down, guys!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    ChrTalk(    #65
        0x101,
        "#1004F#4PHuh? That's it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x103,
        (
            "#022FHold on a second.\x01",
            "We've still got questions.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #67
        0xA,
        (
            "Huh? Why? What more do you need\x01",
            "to know? I gave you lots of details...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x103,
        (
            "#027FYou just said you were making\x01",
            "medicine.\x02\x03",

            "What kind of medicine is it?\x01",
            "And for what purpose?\x02\x03",

            "We need to know both its name\x01",
            "and intended use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        "Wh-Why should I have to tell you that?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D0")

    ChrTalk(    #70
        0x106,
        (
            "#050FLook, we can't afford to help criminals\x01",
            "in this business.\x02\x03",

            "For all we know, you could be asking\x01",
            "us to make something poisonous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D1")

    label("loc_12D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137C")

    ChrTalk(    #71
        0x108,
        (
            "#070FSorry, but we can't be too careful.\x01",
            "For all we know, those ingredients\x01",
            "could make a deadly poison.\x02\x03",

            "We just need to confirm that's not\x01",
            "the case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D1")

    label("loc_137C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_141E")

    ChrTalk(    #72
        0x104,
        (
            "#030FAny medicine used incorrectly can be\x01",
            "a deadly poison.\x02\x03",

            "As protectors of the peace, we cannot\x01",
            "support or condone any criminal activity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D1")

    label("loc_141E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D1")

    ChrTalk(    #73
        0x105,
        (
            "#040FAny medicine can be used to harm\x01",
            "others if used incorrectly.\x02\x03",

            "I think it'd only natural that'd we want\x01",
            "to know what you're making before\x01",
            "agreeing to help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D1")


    ChrTalk(    #74
        0x103,
        (
            "#020FYes, exactly.\x02\x03",

            "If you've nothing to hide, then it\x01",
            "shouldn't be a problem to tell us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "...I suppose that makes sense.\x01",
            "All right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "What I'm looking to make is a\x01",
            "medicine called 'Diaset's Secret.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        (
            "For a while after you take it, no\x01",
            "amount of liquor can get you drunk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        (
            "I heard about it from Father Divine,\x01",
            "so I trust that it works as described.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1011F#4PWhoa. Not even a little drunk?\x02\x03",

            "That's pretty incredible, actually.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D2")

    ChrTalk(    #80
        0x104,
        "#032FHmm. How curious. How...interesting...\x02",
    )

    CloseMessageWindow()

    label("loc_16D2")


    ChrTalk(    #81
        0x103,
        (
            "#023FHmph. What nonsense.\x02\x03",

            "Drinking without getting drunk\x01",
            "is... I mean, what's even the point\x01",
            "of drinking in the first place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1015F#4PThe way you drink's kinda messed\x01",
            "up in the first place, Schera.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E1")

    ChrTalk(    #83
        0x107,
        "#064FBut why do you need that medicine?\x02",
    )

    CloseMessageWindow()
    Jump("loc_18BE")

    label("loc_17E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1821")

    ChrTalk(    #84
        0x105,
        (
            "#040FBut why would you need such\x01",
            "a thing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BE")

    label("loc_1821")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186D")

    ChrTalk(    #85
        0x108,
        (
            "#070FWhy would you want a medicine\x01",
            "like that, anyway?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BE")

    label("loc_186D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18BE")

    ChrTalk(    #86
        0x104,
        (
            "#030FAnd for what reason could you\x01",
            "require such a concoction?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1927")

    ChrTalk(    #87
        0x106,
        (
            "#050FWhat, you stuck in some situation\x01",
            "where you're gonna be drinking a\x01",
            "whole lot?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A5B")

    label("loc_1927")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_198E")

    ChrTalk(    #88
        0x104,
        (
            "#030FIs there some upcoming party you\x01",
            "cannot gracefully extricate yourself\x01",
            "from?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A5B")

    label("loc_198E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19F6")

    ChrTalk(    #89
        0x108,
        (
            "#070FAre you stuck in a situation where\x01",
            "you're being forced to drink a whole\x01",
            "lot?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A5B")

    label("loc_19F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A5B")

    ChrTalk(    #90
        0x105,
        (
            "#040FIs something coming up that's\x01",
            "forcing you to drink more than you\x01",
            "can handle?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A5B")


    ChrTalk(    #91
        0xA,
        "Sort of...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "You might say it's a drinking party.\x01",
            "And, no, I can't back out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "So that's why I need the medicine.\x01",
            "Yeah, let's...let's go with that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3D")

    ChrTalk(    #94
        0x104,
        "#035FHa! I understand the feeling all too well.\x02",
    )

    CloseMessageWindow()

    label("loc_1B3D")


    ChrTalk(    #95
        0x101,
        (
            "#1020F#4PDo you really need to get THAT\x01",
            "drunk, though?\x02\x03",

            "#1007FCan't you just drink a little and stop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x103,
        (
            "#025FThis is ridiculous. Trying to cheat your\x01",
            "way out of a good buzz is an insult to\x01",
            "responsible drinkers everywhere!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C62")
    TurnDirection(0x106, 0x103, 400)

    ChrTalk(    #97
        0x106,
        "#551FResponsible, my ass, Schera.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D55")

    label("loc_1C62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CAE")
    TurnDirection(0x108, 0x103, 400)

    ChrTalk(    #98
        0x108,
        (
            "#073FC'mon, Schera.\x01",
            "Responsible drinking? You?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D55")

    label("loc_1CAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D55")
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(    #99
        0x104,
        (
            "#034FI can hardly believe you would\x01",
            "talk about drinking responsibly\x01",
            "with a straight face...\x02\x03",

            "(I'm sure the irony is completely\x01",
            "lost on her.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D55")


    ChrTalk(    #100
        0xA,
        "Anyway, are you satisfied now?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D91")
    OP_8C(0x106, 135, 400)
    Jump("loc_1DBE")

    label("loc_1D91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA9")
    OP_8C(0x108, 135, 400)
    Jump("loc_1DBE")

    label("loc_1DA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DBE")
    OP_8C(0x104, 135, 400)

    label("loc_1DBE")


    ChrTalk(    #101
        0x101,
        "#1002F#4PY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x103,
        (
            "#020FI suppose.\x02\x03",

            "Once we have the ingredients,\x01",
            "we'll come back here and deliver\x01",
            "them to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        "Awesome! Thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "A-And good luck. My future depends on it,\x01",
            "so please don't take this request lightly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1011F#4P...?\x02\x03",

            "#1016FCan't see how on earth your future\x01",
            "depends on this, but...sure, okay!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    OP_28(0x76, 0x4, 0x4)
    OP_28(0x76, 0x4, 0x8)
    OP_28(0x76, 0x1, 0x1)
    OP_28(0x76, 0x1, 0x2)
    OP_28(0x76, 0x1, 0x4)
    OP_8C(0xA, 180, 400)
    OP_EA(0x1, 0x6, 0x0, 0x0)
    Return()

    # Function_3_DF3 end

    def Function_4_1F37(): pass

    label("Function_4_1F37")

    EventBegin(0x0)
    Call(1, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1FE7")

    ChrTalk(    #106
        0x101,
        (
            "#1000F#4PHey, Anton.\x02\x03",

            "Got a sec?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        "#6PHmmm...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #108
        0xA,
        "Oh, wow. Back already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        (
            "...Could it be?! Did you bring the\x01",
            "ingredients for the medicine?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2087")

    label("loc_1FE7")


    ChrTalk(    #110
        0x101,
        (
            "#1018F#4PHey, Anton.\x02\x03",

            "Got a sec?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        "#6PHmmm...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #112
        0xA,
        "Oh, wow. Back already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        (
            "...Could it be?! Did you bring the\x01",
            "ingredients for the medicine?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2087")

    OP_61(0x101)

    ChrTalk(    #114
        0x101,
        (
            "#1006F#4PRight, you are! Go ahead and\x01",
            "check 'em out.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #115
        "\x07\x05Estelle showed Anton the ingredients they'd gathered.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3AB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3BA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_216C")
    OP_28(0x76, 0x1, 0x1000)
    OP_3F(0x3A4, 5)
    OP_3F(0x39F, 5)
    OP_3F(0x3AB, 5)
    OP_3F(0x3BA, 1)

    label("loc_216C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2221")

    ChrTalk(    #116
        0xA,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xA,
        "Sorry, but you're still missing some.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#1004F#4PHuh? Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xA,
        "Yeah, check your memo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xA,
        (
            "Come back once you've got them all,\x01",
            "please!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)
    Jump("loc_2585")

    label("loc_2221")


    ChrTalk(    #121
        0xA,
        "Ohhh! You did it! You've got them all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xA,
        "Thank you! Thank you, bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xA,
        (
            "Whoo-hoo!! Come on, let's go\x01",
            "get this baby made!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0x101,
        (
            "#1004F#4PUh...\x02\x03",

            "We're coming with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xA,
        (
            "Naturally! You're the ones who helped\x01",
            "make this all possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xA,
        (
            "It's only right that we taste this sweet\x01",
            "moment of truth together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1007F#4PI kinda get the sentiment, but...\x01",
            "this is just weird...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        (
            "#020FWell, whatever.\x02\x03",

            "Let's go with him and get this job\x01",
            "closed out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2454")

    ChrTalk(    #129
        0x106,
        (
            "#051FYeah, let's just get this over and \x01",
            "done with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2529")

    label("loc_2454")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24A7")

    ChrTalk(    #130
        0x104,
        (
            "#030FHow could we refuse an invitation\x01",
            "to bask in his glory?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2529")

    label("loc_24A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24E1")

    ChrTalk(    #131
        0x108,
        "#070FYeah, why not go check it out?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2529")

    label("loc_24E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2529")

    ChrTalk(    #132
        0x105,
        (
            "#040FWell, it's not like we have a reason\x01",
            "to say no.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2529")


    ChrTalk(    #133
        0xA,
        "That's what I like to hear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xA,
        "Off to Father Divine we go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x76, 0x1, 0x2000)
    NewScene("ED6_DT21/T0130   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2585")

    EventEnd(0x0)
    Return()

    # Function_4_1F37 end

    def Function_5_2588(): pass

    label("Function_5_2588")

    Fade(1000)
    OP_4A(0xA, 255)
    SetChrPos(0x101, 54300, 10300, 45000, 135)
    SetChrPos(0x103, 53830, 10300, 46000, 135)
    SetChrPos(0xF8, 53300, 10300, 45070, 135)
    SetChrPos(0xF9, 52830, 10300, 46040, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2604")
    SetChrPos(0xF9, 53300, 10300, 45070, 135)
    SetChrPos(0xF8, 52830, 10300, 46040, 135)

    label("loc_2604")

    OP_6D(54840, 10300, 44060, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    OP_0D()
    Return()

    # Function_5_2588 end

    SaveToFile()

Try(main)
