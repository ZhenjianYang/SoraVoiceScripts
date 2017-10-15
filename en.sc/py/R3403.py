from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3403   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Rudi',                                 # 9
        'Wong',                                 # 10
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


    AddCharChip(
        'ED6_DT07/CH01500 ._CH',             # 00
        'ED6_DT07/CH01760 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01500P._CP',             # 00
        'ED6_DT07/CH01760P._CP',             # 01
    )

    DeclNpc(
        X                   = 613590,
        Z                   = 20,
        Y                   = -52010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 604750,
        Z                   = 0,
        Y                   = -52330,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_179",          # 01, 1
        "Function_2_1D0",          # 02, 2
        "Function_3_1597",         # 03, 3
        "Function_4_1598",         # 04, 4
        "Function_5_1995",         # 05, 5
        "Function_6_1BA8",         # 06, 6
        "Function_7_1BD8",         # 07, 7
        "Function_8_1C08",         # 08, 8
        "Function_9_1C38",         # 09, 9
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_109")
    SetChrFlags(0x8, 0x80)
    Jump("loc_140")

    label("loc_109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_118")
    SetChrFlags(0x8, 0x80)
    Jump("loc_140")

    label("loc_118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_133")
    SetChrPos(0x8, 609020, -20, -62710, 135)
    Jump("loc_140")

    label("loc_133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140")
    SetChrFlags(0x8, 0x10)

    label("loc_140")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 1)), scpexpr(EXPR_END)), "loc_161")
    OP_A2(0x2082)
    Jump("loc_178")

    label("loc_161")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x150, 0x2)"), scpexpr(EXPR_END)), "loc_171")
    Event(0, 5)
    Jump("loc_175")

    label("loc_171")

    Event(0, 4)

    label("loc_175")

    OP_A2(0x2082)

    label("loc_178")

    Return()

    # Function_0_FA end

    def Function_1_179(): pass

    label("Function_1_179")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_79(0xFF, 0x2)
    OP_7A(0x8, 0x2)
    OP_C4(0x0, 0x1)
    OP_78(0x0, 0x0, 0x0)
    Jump("loc_1BD")

    label("loc_1BD")

    OP_16(0x2, 0xFA0, 0x76E58, 0xFFFD40E0, 0x23003A)
    Return()

    # Function_1_179 end

    def Function_2_1D0(): pass

    label("Function_2_1D0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E8")
    OP_A2(0x1)

    label("loc_1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as cleared 'Messenger of Love' with high ranking\x01",            # 0
            "Set as did not clear 'Messenger of Love' with high ranking\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_294"),
        (1, "loc_29A"),
        (SWITCH_DEFAULT, "loc_2A0"),
    )


    label("loc_294")

    OP_A2(0x1)
    Jump("loc_2A0")

    label("loc_29A")

    OP_A3(0x1)
    Jump("loc_2A0")

    label("loc_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_54F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_34F")

    ChrTalk(    #0
        0xFE,
        (
            "If you're looking for Faye, she took off\x01",
            "on the work ship to Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "They're going to be changing out the\x01",
            "Arseille's engine there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D0")

    label("loc_34F")


    ChrTalk(    #2
        0xFE,
        (
            "All right, then... Time to put myself\x01",
            "to work while Faye's away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Until I meet someone new, my only\x01",
            "love is my work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3D0")

    Jump("loc_54C")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4C0")

    ChrTalk(    #4
        0xFE,
        (
            "They're going to be changing out the\x01",
            "Arseille's engine at the fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "*siiigh* And I was finally going to ask\x01",
            "her if she'd officially be my girlfriend...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Curse you, Arseille, for splitting\x01",
            "me and Faye apaaart!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54C")

    label("loc_4C0")


    ChrTalk(    #7
        0xFE,
        (
            "Faye took off on the work\x01",
            "ship to Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I-I was finally going to take her aside\x01",
            "and officially ask her out, too...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_54C")

    Jump("loc_1593")

    label("loc_54F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_7CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_621")

    ChrTalk(    #9
        0xFE,
        (
            "*siiigh*\x01",
            "...But I'm not gonna get depressed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Now's the time to focus on work and\x01",
            "forget about Faye!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "...Or that's the idea, but there's no\x01",
            "way I can concentrate like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B6")

    label("loc_621")


    ChrTalk(    #12
        0xFE,
        (
            "*siiigh* Faye's been so happy and\x01",
            "energetic lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "I guess she's back with her old boyfriend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Aww... So this is love reborn, huh?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_6B6")

    Jump("loc_7CA")

    label("loc_6B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_746")

    ChrTalk(    #15
        0xFE,
        (
            "Today I'll finally tell Faye what\x01",
            "I think, honestly and up front!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Ahhhhh... Just thinking about it\x01",
            "makes my heart pound!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CA")

    label("loc_746")


    ChrTalk(    #17
        0xFE,
        (
            "A-All right, today I'm going to ask\x01",
            "her to date me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I'm a guy, you know? I want things\x01",
            "to be settled once and for all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7CA")

    Jump("loc_1593")

    label("loc_7CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_END)), "loc_924")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_84C")

    ChrTalk(    #19
        0xFE,
        (
            "She's super cute, but she acts as\x01",
            "tough as any guy when it comes to\x01",
            "her work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "I love that contrast.\x02",
    )

    CloseMessageWindow()
    Jump("loc_921")

    label("loc_84C")


    ChrTalk(    #21
        0xFE,
        (
            "So those guys who passed by\x01",
            "were bracers, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "That girl with the ribbon was\x01",
            "a real cutie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "So she hunts monsters in that\x01",
            "cute outfit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Ah, I love it! Brawn and beauty,\x01",
            "all rolled into one!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_921")

    Jump("loc_1593")

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_BD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9EA")

    ChrTalk(    #25
        0xFE,
        (
            "You don't think Faye got back together\x01",
            "with her old boyfriend, do you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "*siiiiigh* I'm such an idiot...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I knew I should've made my move\x01",
            "when I had the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8B")

    label("loc_9EA")


    ChrTalk(    #28
        0xFE,
        (
            "Faye's smile seems so much\x01",
            "brighter since the queen's birthday\x01",
            "celebrations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "You don't think she got back together\x01",
            "with her old boyfriend, do you?!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A8B")

    Jump("loc_BCD")

    label("loc_A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B14")

    ChrTalk(    #30
        0xFE,
        (
            "I mean, it's not like me and Faye\x01",
            "are official yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I-I was thinking it's about time to\x01",
            "make things clear, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCD")

    label("loc_B14")


    ChrTalk(    #32
        0xFE,
        (
            "Ahhhhh... Celebrating the queen's\x01",
            "birthday with Faye was wonderful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Just her and me...and the Arseille.\x01",
            "We stared at it aaaaaall day together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "It was sooo romantic...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BCD")

    Jump("loc_1593")

    label("loc_BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1593")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 0)), scpexpr(EXPR_END)), "loc_CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6A")

    ChrTalk(    #35
        0xFE,
        (
            "Man, between the earthquakes\x01",
            "and that guy in black?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "It just feels unlucky, y'know?\x01",
            "I hope nothin' bad is gonna happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CDC")

    label("loc_C6A")


    ChrTalk(    #37
        0xFE,
        (
            "Anyway, I dunno what's up,\x01",
            "but I'm glad I could help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "So if you'll 'scuse me,\x01",
            "back to the salt mines...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDC")

    Jump("loc_1593")

    label("loc_CDF")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 614200, 20, -53200, 0)
    SetChrPos(0xF7, 613000, 0, -53200, 0)
    SetChrPos(0x105, 614200, 0, -54440, 0)
    SetChrPos(0x104, 613000, 0, -54440, 0)
    OP_6B(2715, 0)
    OP_6D(613510, 10, -52620, 0)
    OP_0D()
    Sleep(600)

    ChrTalk(    #39
        0xFE,
        (
            "I wish these damn earthquakes\x01",
            "would stop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "And on top of those,\x01",
            "that creepy dude in black...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Somethin' bad is goin' on.\x01",
            "Mark my words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1002FA 'dude in black'?\x02\x03",

            "Did you see someone suspicious?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 180, 400)
    Sleep(400)

    ChrTalk(    #43
        0xFE,
        (
            "Oh, yeah. Some weirdo came\x01",
            "through here yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "He was standing right over there,\x01",
            "just...looking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "We don't really get a whole lot of\x01",
            "people comin' through here, you\x01",
            "see, so it made me uncomfortable.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F8B")

    ChrTalk(    #46
        0x106,
        (
            "#052FYeah, I'd say that qualifies as 'suspicious.'\x02\x03",

            "#050FYou remember any details about this guy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1000")

    label("loc_F8B")


    ChrTalk(    #47
        0x103,
        (
            "#022FWell, that certainly does qualify\x01",
            "as 'suspicious,' yes.\x02\x03",

            "Can you remember anything else\x01",
            "about this person?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1000")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #48
        0xFE,
        "Couldn't forget the dude if I tried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "Okay, first? Dude was HUGE.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "I mean, he was wearing a dark\x01",
            "suit and gloves, right? But even\x01",
            "then I could tell he was RIPPED.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "And he had those sunglasses,\x01",
            "too, so he was like a horse on\x01",
            "the freakin' escalator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1011FSun...glasses...?\x02\x03",

            "#1015F...Umm, what are those?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #53
        0xFE,
        (
            "You don't know? They're special glasses\x01",
            "that block the rays of the sun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "You'll know 'em when you see 'em.\x01",
            "The lenses are really dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1004FUh, wouldn't that mean you can't\x01",
            "see what's in front of you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Haha, nah, you can still see just\x01",
            "fine. They're handy, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Still, though, I've never seen\x01",
            "anyone around here use 'em.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_12F8")

    ChrTalk(    #58
        0x106,
        (
            "#050FYeah.\x02\x03",

            "Those should make finding\x01",
            "this guy a cinch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_134D")

    label("loc_12F8")


    ChrTalk(    #59
        0x103,
        (
            "#026FI noticed...\x02\x03",

            "#022FGlasses like those should make\x01",
            "finding this man simple.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134D")


    ChrTalk(    #60
        0x101,
        (
            "#1019FDark suit, dark gloves...and\x01",
            "even his glasses are dark?\x02\x03",

            "#1007FThis guy might as well wear a big 'SUSPECT\x01",
            "ME OF SOMETHING!' sign on his forehead.\x01",
            "In dark lettering, I guess.\x02\x03",

            "We better go tell Kilika about this...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1491")

    ChrTalk(    #61
        0x106,
        (
            "#050FYeah, good idea.\x02\x03",

            "We'll go check out the fort, too,\x01",
            "and report it all at once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E6")

    label("loc_1491")


    ChrTalk(    #62
        0x103,
        (
            "#020FYes, I agree.\x02\x03",

            "Once we investigate the fort,\x01",
            "we can report it all at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E6")

    OP_8C(0xFE, 180, 400)

    ChrTalk(    #63
        0xFE,
        (
            "So, uh, I dunno what this is all about,\x01",
            "but I hope I was able to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1006FYeah, you were a big help!\x02\x03",

            "Thanks for talking to us!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1480)
    OP_A2(0x0)
    OP_28(0x85, 0x1, 0x8)
    OP_28(0x85, 0x1, 0x10)
    ClearChrFlags(0x8, 0x10)
    EventEnd(0x0)

    label("loc_1593")

    TalkEnd(0x8)
    Return()

    # Function_2_1D0 end

    def Function_3_1597(): pass

    label("Function_3_1597")

    Return()

    # Function_3_1597 end

    def Function_4_1598(): pass

    label("Function_4_1598")

    EventBegin(0x0)
    OP_6D(619280, 500, -53640, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 622820, 1000, -55100, 270)
    SetChrPos(0x102, 623820, 1000, -55100, 270)
    SetChrPos(0xF8, 624820, 1000, -55100, 270)
    SetChrPos(0xF9, 625820, 1000, -55100, 270)
    FadeToBright(1500, 0)
    OP_43(0x101, 0x1, 0x0, 0x6)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x7)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0x8)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x9)
    WaitChrThread(0xF8, 0x1)

    ChrTalk(    #65
        0x101,
        "#1020FHoly crap!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_169F")

    ChrTalk(    #66
        0x108,
        "#072FTotal darkness, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_172D")

    label("loc_169F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16EF")

    ChrTalk(    #67
        0x106,
        (
            "#055FFriggin' A...\x01",
            "Literally can't see a thing down here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_172D")

    label("loc_16EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_172D")

    ChrTalk(    #68
        0x103,
        (
            "#022FBlast it all...\x01",
            "It's completely dark!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_172D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_179D")

    ChrTalk(    #69
        0x107,
        (
            "#065FI never realized how dark it'd get\x01",
            "down here without the lights!\x01",
            "Aaah, it's scary...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1862")

    label("loc_179D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F9")

    ChrTalk(    #70
        0x103,
        (
            "#025FYou never stop to think about\x01",
            "even our lights being orbal now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1862")

    label("loc_17F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1862")

    ChrTalk(    #71
        0x106,
        (
            "#057FYeah, well...even our lights are orbal\x01",
            "now. You don't realize it till it's gone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1862")


    ChrTalk(    #72
        0x102,
        (
            "#1043F#6PThe only hope we'd have of navigating down\x01",
            "here would be night-vision goggles.\x02\x03",

            "#1042FIf we don't have any, we should\x01",
            "check around town, in the general\x01",
            "goods store or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1007FYeah, good idea.\x02\x03",

            "#1002FOne way or another, probably best to\x01",
            "find a way to see before going forward.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_4_1598 end

    def Function_5_1995(): pass

    label("Function_5_1995")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(619280, 500, -53640, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 622820, 1000, -55100, 270)
    SetChrPos(0x102, 623820, 1000, -55100, 270)
    SetChrPos(0xF8, 624820, 1000, -55100, 270)
    SetChrPos(0xF9, 625820, 1000, -55100, 270)
    OP_43(0x101, 0x1, 0x0, 0x6)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x7)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0x8)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x9)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #74
        0x101,
        (
            "#1019FWell, with the night-vision goggles\x01",
            "on I can actually see...\x02\x03",

            "But without them, yeah, I know\x01",
            "what it feels like to be a bat now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#1035F#6PThere's virtually no light down\x01",
            "here, otherwise.\x02\x03",

            "#1042FIn the interest of not getting lost, we\x01",
            "should wear the goggles whenever\x01",
            "we pass through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1002FGot it!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_5_1995 end

    def Function_6_1BA8(): pass

    label("Function_6_1BA8")

    OP_8E(0xFE, 0x97EAA, 0x3E8, 0xFFFF28F6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9766C, 0x3E8, 0xFFFF26F8, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_6_1BA8 end

    def Function_7_1BD8(): pass

    label("Function_7_1BD8")

    OP_8E(0xFE, 0x97EAA, 0x3E8, 0xFFFF28F6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x97680, 0x3E8, 0xFFFF2A40, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_7_1BD8 end

    def Function_8_1C08(): pass

    label("Function_8_1C08")

    OP_8E(0xFE, 0x97C7A, 0x3E8, 0xFFFF284C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x979E6, 0x3E8, 0xFFFF266C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_1C08 end

    def Function_9_1C38(): pass

    label("Function_9_1C38")

    OP_8E(0xFE, 0x97EAA, 0x3E8, 0xFFFF28F6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x979BE, 0x3E8, 0xFFFF29B4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_1C38 end

    SaveToFile()

Try(main)
