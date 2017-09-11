from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0133   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0133.x',
        MapIndex            = 10,
        MapDefaultBGM       = "ed60010",
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Paddington',                           # 9
        'Ellie',                                # 10
        'Armand',                               # 11
    )

    DeclEntryPoint(
        Unknown_00              = 6000,
        Unknown_04              = 0,
        Unknown_08              = 184000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 10,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01250 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01140 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01250P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01140P._CP',             # 02
    )

    DeclNpc(
        X                   = 3275,
        Z                   = 0,
        Y                   = 2522,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 54174,
        Z                   = 10300,
        Y                   = 44126,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 54904,
        Z                   = 10300,
        Y                   = 44125,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -300,
        TriggerZ            = 0,
        TriggerY            = 4140,
        TriggerRange        = 800,
        ActorX              = -300,
        ActorZ              = 1000,
        ActorY              = 4140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53450,
        TriggerZ            = 10300,
        TriggerY            = 47970,
        TriggerRange        = 800,
        ActorX              = 53450,
        ActorZ              = 10000,
        ActorY              = 47970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_1E2",          # 01, 1
        "Function_2_204",          # 02, 2
        "Function_3_205",          # 03, 3
        "Function_4_21B",          # 04, 4
        "Function_5_B46",          # 05, 5
        "Function_6_D77",          # 06, 6
        "Function_7_F26",          # 07, 7
        "Function_8_10C4",         # 08, 8
        "Function_9_10CE",         # 09, 9
        "Function_10_215E",        # 0A, 10
        "Function_11_21E1",        # 0B, 11
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_17E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_1D3")

    label("loc_17E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_188")
    Jump("loc_1D3")

    label("loc_188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_19C")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_1D3")

    label("loc_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1A6")
    Jump("loc_1D3")

    label("loc_1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1C4")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_1D3")

    label("loc_1C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1CE")
    Jump("loc_1D3")

    label("loc_1CE")

    SetChrFlags(0x8, 0x10)

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1E1")
    OP_A3(0x3FA)
    Event(0, 9)

    label("loc_1E1")

    Return()

    # Function_0_16A end

    def Function_1_1E2(): pass

    label("Function_1_1E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA")
    OP_B1("t0133_y")
    Jump("loc_203")

    label("loc_1FA")

    OP_B1("t0133_n")

    label("loc_203")

    Return()

    # Function_1_1E2 end

    def Function_2_204(): pass

    label("Function_2_204")

    Return()

    # Function_2_204 end

    def Function_3_205(): pass

    label("Function_3_205")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_3_205")

    label("loc_21A")

    Return()

    # Function_3_205 end

    def Function_4_21B(): pass

    label("Function_4_21B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_3FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F")
    OP_A2(0x0)

    ChrTalk(    #0
        0xFE,
        (
            "Gazing out from the top here\x01",
            "every day is quite enjoyable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "The changing seasons, the lives of\x01",
            "those people living here in town...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Though they are all minor, I can see\x01",
            "these changes with my own eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Recently, I've seen Mrs. Bloom\x01",
            "out and about quite a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "Ho ho, I wonder what she's up to.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F9")

    label("loc_36F")


    ChrTalk(    #5
        0xFE,
        (
            "Gazing out from the top here\x01",
            "every day is quite enjoyable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Though they are all minor, I can see\x01",
            "these changes with my own eyes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9")

    Jump("loc_B42")

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_541")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F1")
    OP_A2(0x0)

    ChrTalk(    #7
        0xFE,
        (
            "After the war, Melders' son restored\x01",
            "this clock tower using an orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I'm a little saddened by the fact that\x01",
            "the number of things I maintain has\x01",
            "decreased...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Ho ho, this just means that the\x01",
            "era has changed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53E")

    label("loc_4F1")


    ChrTalk(    #10
        0xFE,
        (
            "After the war, Melders' son restored\x01",
            "this clock tower using an orbment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53E")

    Jump("loc_B42")

    label("loc_541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F3")
    OP_A2(0x0)

    ChrTalk(    #11
        0xFE,
        (
            "Let's see, how about I get to\x01",
            "work on my inspections and\x01",
            "maintenance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "This tower is the symbol of Rolent, its\x01",
            "history, and it is my pride and joy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_645")

    label("loc_5F3")


    ChrTalk(    #13
        0xFE,
        (
            "This tower is the symbol of Rolent, its\x01",
            "history, and it is my pride and joy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_645")

    Jump("loc_B42")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_7AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_725")
    OP_A2(0x0)

    ChrTalk(    #14
        0x8,
        (
            "Another day has passed.\x01",
            "There is nothing better than peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "Just thinking about what happened\x01",
            "10 years ago makes my old bones\x01",
            "tremble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "War is something which should\x01",
            "never happen again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AC")

    label("loc_725")


    ChrTalk(    #17
        0x8,
        (
            "Just thinking about what happened\x01",
            "10 years ago makes my old bones\x01",
            "tremble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "War is something which should\x01",
            "never happen again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AC")

    Jump("loc_B42")

    label("loc_7AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_8BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_865")
    OP_A2(0x0)

    ChrTalk(    #19
        0x8,
        "A beautiful sound as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        "I love the toll of this tower bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "This bell does more than tell\x01",
            "the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "It's also marking Rolent's history.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BB")

    label("loc_865")


    ChrTalk(    #23
        0x8,
        (
            "This bell does more than tell\x01",
            "the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "It's also marking Rolent's history.\x02",
    )

    CloseMessageWindow()

    label("loc_8BB")

    Jump("loc_B42")

    label("loc_8BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABC")
    OP_A2(0x0)

    ChrTalk(    #25
        0x101,
        "#001FMr. Paddington!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #26
        0x8,
        (
            "Mm? Now I know that voice from\x01",
            "somewhere...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(    #27
        0x8,
        "Ho ho ho!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "Well, what have we got here? Cassius'\x01",
            "naughty daughter and clever son, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "Just when I thought you hadn't been around in a\x01",
            "while, you show up all grown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#010FAre you here every day,\x01",
            "Mr. Paddington?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #31
        0x8,
        (
            "This place has become somewhat of a new\x01",
            "home for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "I intend to spend the remainder of my days\x01",
            "guarding this clock.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B42")

    label("loc_ABC")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #33
        0x8,
        (
            "This place has become somewhat of a new\x01",
            "home for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "I intend to spend the remainder of my days\x01",
            "guarding this clock.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B42")

    TalkEnd(0x8)
    Return()

    # Function_4_21B end

    def Function_5_B46(): pass

    label("Function_5_B46")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D30")
    OP_A2(0x1)

    ChrTalk(    #35
        0x9,
        (
            "It was when the stars had just\x01",
            "emerged from the veil of night\x01",
            "that he asked me here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "Sweetly, he whispered in my ear...\x01",
            "'I want you to be mine...'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0x9,
        "How romantic!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "It's just the situation I've always\x01",
            "wanted to be in!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 500)

    ChrTalk(    #39
        0x101,
        (
            "#501F(Well, I guess it's not a bad place\x01",
            "and all, but...)\x02\x03",

            "#501F(The two of them came up\x01",
            "here just for that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#010F(Haha. I guess this type of thing\x01",
            "can only be understood by those\x01",
            "involved.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D73")

    label("loc_D30")


    ChrTalk(    #41
        0x9,
        "Teehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        "I'm on cloud nine!\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    label("loc_D73")

    TalkEnd(0x9)
    Return()

    # Function_5_B46 end

    def Function_6_D77(): pass

    label("Function_6_D77")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECE")
    OP_A2(0x2)

    ChrTalk(    #43
        0xA,
        "#4SYessssss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        "Listen to this, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        "I got her to go out with me!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 500)
    OP_62(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0xA,
        (
            "Oh, Aidios... It was all worth the\x01",
            "single day of trouble I went through\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x101,
        "#501F(A single day? Uh...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        (
            "#010F(I guess that could be called\x01",
            "a victory of perseverance.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F22")

    label("loc_ECE")


    ChrTalk(    #49
        0xA,
        (
            "Oh, Aidios... It was all worth the\x01",
            "single day of trouble I went through\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F22")

    TalkEnd(0xA)
    Return()

    # Function_6_D77 end

    def Function_7_F26(): pass

    label("Function_7_F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10BA")
    EventBegin(0x0)
    OP_A2(0x26A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05There's a ladder that goes up to the observation deck.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #51
        0x101,
        "#003F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #52
        0x102,
        (
            "#014FWhat's wrong, Estelle?\x01",
            "Something on your mind?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #53
        0x101,
        (
            "#506FIt's nothing, really!\x02\x03",

            "#006FHow about we climb up to the\x01",
            "observation deck?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        "#014FSure, I guess...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A9")

    ChrTalk(    #55
        0x103,
        "#522F...\x02",
    )

    CloseMessageWindow()

    label("loc_10A9")

    Sleep(100)
    NewScene("ED6_DT01/T0133   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_10C3")

    label("loc_10BA")

    NewScene("ED6_DT01/T0133   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_10C3")

    Return()

    # Function_7_F26 end

    def Function_8_10C4(): pass

    label("Function_8_10C4")

    NewScene("ED6_DT01/T0133   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_8_10C4 end

    def Function_9_10CE(): pass

    label("Function_9_10CE")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 54192, 10300, 44126, 180)
    SetChrPos(0x102, 55561, 10300, 44126, 180)
    SetMapFlags(0x10)
    FadeToBright(4000, 0)
    OP_6D(54670, 10300, 44190, 0)
    OP_6C(330000, 0)
    OP_67(0, 8300, -10000, 0)
    OP_6B(1560, 0)
    OP_6E(457, 0)

    def lambda_1148():
        OP_6D(54190, 10300, 41950, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1148)

    def lambda_1160():
        OP_6C(302000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1160)

    def lambda_1170():
        OP_6E(539, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1170)

    def lambda_1180():
        OP_67(0, 7060, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1180)
    Sleep(6500)
    Fade(1500)
    OP_6D(54620, 10300, 44190, 0)
    OP_67(0, 6690, -10000, 0)
    OP_6B(1660, 0)
    OP_6C(225000, 0)
    OP_6E(476, 0)
    SetChrPos(0x101, 53950, 10300, 44150, 180)
    SetChrPos(0x102, 55250, 10300, 44150, 180)
    Sleep(2000)

    ChrTalk(    #56
        0x101,
        (
            "#501F#4PThe morning air is so\x01",
            "refreshing...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #57
        0x101,
        (
            "#001F#4PHey look, Joshua.\x01",
            "We can see the house from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        "#019F#6PYou're right. I can see the roof.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #59
        0x102,
        (
            "#010F#6PBut do you want to tell me what's\x01",
            "going on since you've always\x01",
            "avoided coming up here?\x02\x03",

            "I was under the impression that\x01",
            "you didn't like this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#003F#4P...\x02",
    )

    CloseMessageWindow()

    def lambda_1365():
        OP_6E(450, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1365)
    OP_20(0x7D0)
    Sleep(1000)
    OP_8C(0x101, 180, 300)
    OP_21()
    OP_1D(0x53)
    Sleep(1000)

    ChrTalk(    #61
        0x101,
        (
            "#000F#4PI like this place, but I just can't\x01",
            "casually come up here.\x02\x03",

            "#500FBecause this is the place...\x01",
            "where my mom died.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        "#014F#6PWhat...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_AD(0x40019, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Estelle")

    AnonymousTalk(    #63
        "\x07\x0C10 years ago, during the war...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #64
        (
            "When the Imperial Army surrounded Rolent, they bombarded the symbol of\x01",
            "the city, the clock tower, to try and get the citizens to surrender.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #65
        "This was at the time Dad was fighting in the Royal Army.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #66
        (
            "I wanted to see who he was fighting against, so I climbed up the clock\x01",
            "tower...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #67
        "And when the bombardment started...I couldn't get away.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_AD(0x4001A, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("Estelle")

    AnonymousTalk(    #68
        "When I came to, I hardly had a scratch on me.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #69
        "My mother had saved me.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #70
        "I was wrapped tightly in her arms, shielded from the rubble...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #71
        "And as I cried, she sang my favorite lullaby...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #72
        "But...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #73
        "When they finally dug us free...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x64)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(    #74
        0x101,
        (
            "#003F#4P...\x02\x03",

            "After the war ended and this\x01",
            "place had been rebuilt, I avoided\x01",
            "coming here for the most part.\x02\x03",

            "It's not because I have painful\x01",
            "memories of this place, though.\x02\x03",

            "#500FIt's just, when I come here,\x01",
            "a part of me wants so much\x01",
            "to draw on her strength...\x02\x03",

            "Plus, I've felt that I can't be\x01",
            "strong like her if I'm always\x01",
            "trying to rely on her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        "#013F#6PEstelle...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #76
        0x101,
        (
            "#501F#4PBut today is okay, right?\x01",
            "Relying on her just this once...\x02\x03",

            "Asking her to bring Dad\x01",
            "home safely...\x02\x03",

            "Asking her to protect him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        "#015F#6P...Of course it is.\x02",
    )

    CloseMessageWindow()

    def lambda_192B():
        OP_6D(53840, 10300, 44180, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_192B)
    OP_92(0x102, 0x101, 0x1F4, 0x3E8, 0x0)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #78
        0x102,
        (
            "#012F#6PAnd don't worry...\x01",
            "Dad's safe for sure.\x02\x03",

            "Your mother's protecting him.\x01",
            "So there's no doubt in my mind\x01",
            "that he's safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#003F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        (
            "#010F#6PAnd if he happens to be in a bit\x01",
            "of trouble, then you can come\x01",
            "to his rescue.\x02\x03",

            "Just like your mother did for you,\x01",
            "you can do the same for your dad.\x02\x03",

            "And don't forget, I'm here to\x01",
            "help you, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#003F#4PJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        (
            "#013F#6PI know I can't completely understand\x01",
            "everything you've been through, but...\x02\x03",

            "I can stay here by your side\x01",
            "as I am now...\x02\x03",

            "#010FAnd if you need a shoulder to cry on,\x01",
            "you've always got mine.\x02\x03",

            "So...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#500F#4P...\x02\x03",

            "#008F...pfffffft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x102,
        "#014F#6PHuh?\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x1)

    ChrTalk(    #85
        0x101,
        (
            "#001F#4PHa ha ha ha!\x01",
            "Joshua, you're trying too hard!\x02\x03",

            "You shouldn't say things like\x01",
            "that so lightly.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1C5B():
        OP_6D(54620, 10300, 44190, 700)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1C5B)
    OP_8F(0x102, 0xD7D2, 0x283C, 0xAC76, 0xBB8, 0x0)
    Sleep(1000)

    ChrTalk(    #86
        0x102,
        "#014F#6PWh-What do you mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#507F#4PIf I were any other girl, I would\x01",
            "totally have misinterpreted your\x01",
            "intentions just now.\x02\x03",

            "You are seriously the type who's\x01",
            "going to have problems with romantic\x01",
            "relationships in the future.\x02\x03",

            "#007FI'm already starting to get worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        (
            "#012F#6PWell, excuse me for trying\x01",
            "to be nice!\x02\x03",

            "#013FWhy do you have to be like that\x01",
            "when someone is genuinely\x01",
            "worried about you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#008F#4PThanks for cheering me up,\x01",
            "Joshua.\x02\x03",

            "I feel a lot better now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        (
            "#018F#6PI guess as long as I get some kind\x01",
            "of thanks it was worth looking like\x01",
            "a complete fool.\x02\x03",

            "#017FBut you are unbelievable...\x01",
            "*mumble* *mumble*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#001F#4PDon't be so mad. I'm really thankful,\x01",
            "believe it or not.\x02\x03",

            "#006FSo how about we get down \x01",
            "from here, huh?\x02\x03",

            "I'm sure Schera's waiting for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x102,
        "#010F#6PYou're probably right.\x02",
    )

    CloseMessageWindow()

    def lambda_1FCC():
        OP_6D(54240, 10300, 47980, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1FCC)

    def lambda_1FE4():
        OP_67(0, 6220, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1FE4)

    def lambda_1FFC():
        OP_6C(324000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1FFC)

    def lambda_200C():
        OP_6E(470, 4000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_200C)
    OP_43(0x102, 0x0, 0x0, 0xA)
    Sleep(3000)
    SetChrFlags(0x102, 0x4)
    OP_8E(0x101, 0xCD12, 0x283C, 0xB5C7, 0xBB8, 0x0)
    Sleep(1000)

    ChrTalk(    #93
        0x101,
        "#500F...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(1000)

    ChrTalk(    #94
        0x101,
        (
            "#006F(Mom. I've finally realized why\x01",
            "I wanted to become a bracer...)\x02\x03",

            "(It's so I could become strong and\x01",
            "protect others just like you...)\x02\x03",

            "(So please watch and see...)\x02\x03",

            "(I won't fail to bring Dad\x01",
            "home safe again!)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_43(0x101, 0x0, 0x0, 0xB)
    OP_0D()
    SetChrFlags(0x102, 0x80)
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T0100   ._SN", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_9_10CE end

    def Function_10_215E(): pass

    label("Function_10_215E")

    SetChrFlags(0x102, 0x4)
    OP_8E(0x102, 0xCC9C, 0x283C, 0xB536, 0x7D0, 0x0)
    OP_8E(0x102, 0xCC88, 0x283C, 0xBB08, 0x7D0, 0x0)
    OP_8E(0x102, 0xCE72, 0x283C, 0xBB94, 0x7D0, 0x0)
    SetChrFlags(0x102, 0x4)
    OP_8C(0x102, 270, 400)
    OP_96(0x102, 0xD1C4, 0x251C, 0xBCA4, 0x258, 0x1388)
    Sleep(500)
    OP_8F(0x102, 0xD1C4, 0x206C, 0xBCA4, 0xBB8, 0x0)
    SetChrFlags(0x102, 0x80)
    Return()

    # Function_10_215E end

    def Function_11_21E1(): pass

    label("Function_11_21E1")

    SetChrFlags(0x101, 0x4)
    OP_8E(0x101, 0xCC88, 0x283C, 0xBB08, 0x7D0, 0x0)
    OP_8E(0x101, 0xCE72, 0x283C, 0xBB94, 0x7D0, 0x0)
    OP_8C(0x101, 270, 400)
    OP_96(0x101, 0xD1C4, 0x251C, 0xBCA4, 0x258, 0x1388)
    Sleep(500)
    OP_8F(0x101, 0xD1C4, 0x206C, 0xBCA4, 0xBB8, 0x0)
    SetChrFlags(0x101, 0x80)
    Return()

    # Function_11_21E1 end

    SaveToFile()

Try(main)
