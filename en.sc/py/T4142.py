from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4142   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4142.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Baral',                                # 9
        'Cready',                               # 10
        'Spencer',                              # 11
        'Nial',                                 # 12
        'Noticia',                              # 13
        'Faults',                               # 14
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01023 ._CH',             # 02
        'ED6_DT07/CH02060 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT07/CH01143 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01023P._CP',             # 02
        'ED6_DT07/CH02060P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT07/CH01143P._CP',             # 05
    )

    DeclNpc(
        X                   = 61020,
        Z                   = 0,
        Y                   = 2490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4560,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 186,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 100,
        Y                   = -3850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -64450,
        Z                   = 0,
        Y                   = 60580,
        Direction           = 1,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -53860,
        Z                   = 250,
        Y                   = 121340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -59030,
        Z                   = 100,
        Y                   = 59540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 60700,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = 61020,
        ActorZ              = 1500,
        ActorY              = 2490,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4530,
        TriggerZ            = 0,
        TriggerY            = 590,
        TriggerRange        = 400,
        ActorX              = 4560,
        ActorZ              = 1500,
        ActorY              = 2500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_1E3",          # 01, 1
        "Function_2_1F5",          # 02, 2
        "Function_3_1FA",          # 03, 3
        "Function_4_3B2",          # 04, 4
        "Function_5_3B7",          # 05, 5
        "Function_6_61C",          # 06, 6
        "Function_7_77C",          # 07, 7
        "Function_8_A6E",          # 08, 8
        "Function_9_B23",          # 09, 9
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Return()

    # Function_0_1E2 end

    def Function_1_1E3(): pass

    label("Function_1_1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F4")

    Return()

    # Function_1_1E3 end

    def Function_2_1F5(): pass

    label("Function_2_1F5")

    Call(0, 3)
    Return()

    # Function_2_1F5 end

    def Function_3_1FA(): pass

    label("Function_3_1FA")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                              # 0
            "Shop\x01",                              # 1
            "[Curry of Dreams] - 900 mira\x01",      # 2
            "Leave\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_277")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xCB)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_277")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_351")
    SubMira(900)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06Ate #2CCurry of Dreams#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x640)
    OP_31(0x1, 0xFD, 0x640)
    OP_31(0x2, 0xFD, 0x640)
    OP_31(0x3, 0xFD, 0x640)
    OP_31(0x4, 0xFD, 0x640)
    OP_31(0x5, 0xFD, 0x640)
    OP_31(0x6, 0xFD, 0x640)
    OP_31(0x7, 0xFD, 0x640)
    OP_31(0x8, 0xFD, 0x640)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_343")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0xB)"), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_343")

    label("loc_312")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06Learned [#2CCurry of Dreams#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_343")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_379")

    label("loc_351")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_379")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x8)
    Return()

    label("loc_38B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A5")
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    label("loc_3A5")

    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    # Function_3_1FA end

    def Function_4_3B2(): pass

    label("Function_4_3B2")

    Call(0, 5)
    Return()

    # Function_4_3B2 end

    def Function_5_3B7(): pass

    label("Function_5_3B7")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                              # 0
            "Shop\x01",                              # 1
            "[Seafood Hotpot] - 1200 mira\x01",      # 2
            "Leave\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_434")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xCA)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_434")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_546")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_50C")
    SubMira(1200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #3
        "\x06Ate #2CSeafood Hotpot#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x9C4)
    OP_31(0x1, 0xFD, 0x9C4)
    OP_31(0x2, 0xFD, 0x9C4)
    OP_31(0x3, 0xFD, 0x9C4)
    OP_31(0x4, 0xFD, 0x9C4)
    OP_31(0x5, 0xFD, 0x9C4)
    OP_31(0x6, 0xFD, 0x9C4)
    OP_31(0x7, 0xFD, 0x9C4)
    OP_31(0x8, 0xFD, 0x9C4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x2)"), scpexpr(EXPR_END)), "loc_4CE")
    Jump("loc_4FE")

    label("loc_4CE")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #4
        "\x06Learned [#2CSeafood Hotpot#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_4FE")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_534")

    label("loc_50C")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_534")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x9)
    Return()

    label("loc_546")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_560")
    FadeToBright(300, 0)
    TalkEnd(0x9)
    Return()

    label("loc_560")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_5A8")

    ChrTalk(    #6
        0x9,
        "...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        "Did I just hear a bird's cry outside?\x02",
    )

    CloseMessageWindow()
    Jump("loc_618")

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_618")

    ChrTalk(    #8
        0x9,
        (
            "Now, then, the busiest time of day\x01",
            "is behind us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "I need to get started on prep for tomorrow!\x02",
    )

    CloseMessageWindow()

    label("loc_618")

    TalkEnd(0x9)
    Return()

    # Function_5_3B7 end

    def Function_6_61C(): pass

    label("Function_6_61C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_68F")

    ChrTalk(    #10
        0xFE,
        (
            "Phew! Just about time to go\x01",
            "home and take a bath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "The best way to end a day is with a bath!\x02",
    )

    CloseMessageWindow()
    Jump("loc_778")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_778")

    ChrTalk(    #12
        0xFE,
        (
            "By the way, a friend of mine who works\x01",
            "at the harbor mentioned something odd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Apparently, every night they hear strange noises\x01",
            "from a warehouse there that should be empty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Could it be...a GHOST?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "*shudder*\x02",
    )

    CloseMessageWindow()

    label("loc_778")

    TalkEnd(0xFE)
    Return()

    # Function_6_61C end

    def Function_7_77C(): pass

    label("Function_7_77C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0A")

    ChrTalk(    #16
        0xB,
        "#143FOh, what's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#1002FNial, has anything odd happened around here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xB,
        "#140FOdd? Like what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1002FWell, like a sudden disturbance, or someone\x01",
            "seeing something strange. Anything, really!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "#142FDon't think I've heard about anything\x01",
            "like that.\x02\x03",

            "And a sudden disturbance is more the\x01",
            "kind of thing I should be asking you\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1003FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        (
            "#143FThere some kinda trouble afoot?\x02\x03",

            "#141FIf there is, I'm comin' along!\x02\x03",

            "I'll be ready right away.\x01",
            "Wait for me in the lobby!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1000FAh, o-okay. But, we need to hurry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        (
            "#143FWhat, it's an emergency?\x02\x03",

            "#140FYou guys go on ahead, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1002FYeah, sorry.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x164A)
    Jump("loc_A6A")

    label("loc_A0A")


    ChrTalk(    #26
        0xB,
        (
            "#140FWest Block, right?\x02\x03",

            "As soon as I'm ready, I'll meet you there.\x02\x03",

            "You guys go on ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6A")

    TalkEnd(0xB)
    Return()

    # Function_7_77C end

    def Function_8_A6E(): pass

    label("Function_8_A6E")

    TalkBegin(0xFE)

    ChrTalk(    #27
        0xFE,
        (
            "It's always a little sad that all us reporters,\x01",
            "and only us, are left behind in the office\x01",
            "when it's this late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "But, this is still a job that's really\x01",
            "worth doing.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_A6E end

    def Function_9_B23(): pass

    label("Function_9_B23")

    TalkBegin(0xFE)

    ChrTalk(    #29
        0xFE,
        "Ahh, I wanna go home and eat. *sigh*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_B23 end

    SaveToFile()

Try(main)
