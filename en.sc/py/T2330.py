from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2330   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2330.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2330   ._SN',
            'ED6_DT21/T2330_1 ._SN',
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
        'Rex',                                  # 9
        'Carla',                                # 10
        'Dario',                                # 11
        'Orvid',                                # 12
        'Melvin',                               # 13
        'Royal Army Soldier',                   # 14
        'Booze',                                # 15
        'Booze',                                # 16
        'Booze+',                               # 17
        'Sky Booze',                            # 18
        'Booze',                                # 19
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01030 ._CH',             # 01
        'ED6_DT07/CH01563 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01760 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT07/CH01300 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01030P._CP',             # 01
        'ED6_DT07/CH01563P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01760P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT07/CH01300P._CP',             # 07
    )

    DeclNpc(
        X                   = -25500,
        Z                   = 0,
        Y                   = 43210,
        Direction           = 270,
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
        X                   = -37500,
        Z                   = 0,
        Y                   = 44500,
        Direction           = 180,
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
        X                   = -37480,
        Z                   = 200,
        Y                   = 39900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = 0,
        Y                   = 2330,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = -30680,
        Z                   = 0,
        Y                   = 44805,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -2200,
        Z                   = 0,
        Y                   = 2490,
        Direction           = 284,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -37820,
        Z                   = 750,
        Y                   = 38730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966085,
        ChipIndex           = 0x5,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -37470,
        Z                   = 750,
        Y                   = 38480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966085,
        ChipIndex           = 0x5,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -37530,
        Z                   = 750,
        Y                   = 39070,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -37260,
        Z                   = 750,
        Y                   = 38950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65542,
        ChipIndex           = 0x6,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -37010,
        Z                   = 800,
        Y                   = 38560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900549,
        ChipIndex           = 0x5,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -37020,
        TriggerZ            = 0,
        TriggerY            = 42970,
        TriggerRange        = 400,
        ActorX              = -37500,
        ActorZ              = 1500,
        ActorY              = 44500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26870,
        TriggerZ            = 0,
        TriggerY            = 42820,
        TriggerRange        = 400,
        ActorX              = -25500,
        ActorZ              = 1500,
        ActorY              = 43210,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_2D6",          # 01, 1
        "Function_2_2D7",          # 02, 2
        "Function_3_2DC",          # 03, 3
        "Function_4_C5F",          # 04, 4
        "Function_5_C64",          # 05, 5
        "Function_6_162A",         # 06, 6
        "Function_7_1C5D",         # 07, 7
        "Function_8_1D9E",         # 08, 8
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C4")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_2D5")

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D5")
    ClearChrFlags(0xC, 0x80)

    label("loc_2D5")

    Return()

    # Function_0_292 end

    def Function_1_2D6(): pass

    label("Function_1_2D6")

    Return()

    # Function_1_2D6 end

    def Function_2_2D7(): pass

    label("Function_2_2D7")

    Call(0, 3)
    Return()

    # Function_2_2D7 end

    def Function_3_2DC(): pass

    label("Function_3_2DC")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                               # 0
            "Shop\x01",                               # 1
            "[Garden of Seaden] - 600 mira\x01",      # 2
            "Leave\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A")
    OP_0D()
    OP_A9(0x70)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_35A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_470")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_436")
    SubMira(600)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06Ate #2CGarden of Seaden#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x258)
    OP_31(0x1, 0xFD, 0x258)
    OP_31(0x2, 0xFD, 0x258)
    OP_31(0x3, 0xFD, 0x258)
    OP_31(0x4, 0xFD, 0x258)
    OP_31(0x5, 0xFD, 0x258)
    OP_31(0x6, 0xFD, 0x258)
    OP_31(0x7, 0xFD, 0x258)
    OP_31(0x8, 0xFD, 0x258)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_428")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x1)"), scpexpr(EXPR_END)), "loc_3F6")
    Jump("loc_428")

    label("loc_3F6")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06Learned [#2CGarden of Seaden#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_428")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_45E")

    label("loc_436")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_45E")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x8)
    Return()

    label("loc_470")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_481")
    TalkEnd(0x8)
    Return()

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_548")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_514")

    ChrTalk(    #3
        0x8,
        "That injured soldier's gotten a lot better.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "It's not like the patrol ships can fly,\x01",
            "so I hope he's able to rest up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_545")

    label("loc_514")


    ChrTalk(    #5
        0x8,
        "That injured soldier's gotten a lot better.\x02",
    )

    CloseMessageWindow()

    label("loc_545")

    Jump("loc_C5B")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_618")

    ChrTalk(    #6
        0x8,
        "Hey! Welcome to the White Magnolia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "Can't get a lot of stock right\x01",
            "now, but we're still open!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "It's times like these that I want\x01",
            "to do what I can to help all the\x01",
            "villagers.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6AC")

    label("loc_618")


    ChrTalk(    #9
        0x8,
        (
            "Can't get a lot of stock right now,\x01",
            "but we're making do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "Things aren't so bad here, since\x01",
            "we mostly rely on our own catches.\x01",
            "But still...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AC")

    Jump("loc_C5B")

    label("loc_6AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 6)), scpexpr(EXPR_END)), "loc_A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_745")

    ChrTalk(    #11
        0x8,
        (
            "My inn's hosting the voting area\x01",
            "for this upcoming election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "I owe everyone so much, so it's\x01",
            "my little way of giving back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A79")

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_8AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_794")

    ChrTalk(    #13
        0x8,
        (
            "The mayoral election's coming\x01",
            "up, but who to vote for...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A9")

    label("loc_794")

    OP_A2(0x0)

    ChrTalk(    #14
        0x8,
        (
            "The mayoral election's coming up,\x01",
            "but, Who to vote for...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "I'd be happy if the tourism industry\x01",
            "expanded, but Ruan is a harbor city\x01",
            "first and foremost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "Nothing good can come of allowing\x01",
            "the harbor to fall into decay. We\x01",
            "need to stay on top of it at all times!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A9")

    Jump("loc_A79")

    label("loc_8AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_966")

    ChrTalk(    #17
        0x8,
        "Hey, did you go to the Windmill Lodge?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "The view from there's beautiful.\x01",
            "Keeps the customers coming back\x01",
            "time and time again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "I guarantee you, it's worth a look!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A79")

    label("loc_966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_A79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9E4")

    ChrTalk(    #20
        0x8,
        (
            "If you're looking for a good meal,\x01",
            "I recommend our new dish!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "It's our number one seller right now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A79")

    label("loc_9E4")

    OP_A2(0x0)

    ChrTalk(    #22
        0x8,
        (
            "Welcome to the White Magnolia!\x01",
            "If you're looking for a good meal,\x01",
            "I recommend our newest special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "It's our number one seller right now.\x02",
    )

    CloseMessageWindow()

    label("loc_A79")

    Jump("loc_C5B")

    label("loc_A7C")

    OP_A2(0x122E)
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(    #24
        0x8,
        (
            "Welcome to The White Magnolia!\x01",
            "Don't think I've seen you around\x01",
            "here before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "...Actually, wait a sec. I DO know you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "You've been here before, haven't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1011FYou remember me?\x02\x03",

            "That was a while back, too.\x01",
            "I bought a boxed lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "Ohh, that's right. Well, how\x01",
            "about trying our new dish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "It's the most popular thing on\x01",
            "our menu right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1018FMmm, that does sound promising.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "Well, if you're feeling hungry,\x01",
            "just say the word!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5B")

    TalkEnd(0x8)
    Return()

    # Function_3_2DC end

    def Function_4_C5F(): pass

    label("Function_4_C5F")

    Call(0, 5)
    Return()

    # Function_4_C5F end

    def Function_5_C64(): pass

    label("Function_5_C64")

    TalkBegin(0x9)
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C81")
    OP_A9(0x6F)
    TalkEnd(0x9)
    Return()

    label("loc_C81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C92")
    TalkEnd(0x9)
    Return()

    label("loc_C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_E16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8F")

    ChrTalk(    #32
        0x9,
        (
            "The patrol ship's still grounded\x01",
            "on the beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x9,
        (
            "Not that they have many options,\x01",
            "what with orbments not working\x01",
            "and all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "Honestly, they should all just stay\x01",
            "here! We'd be more than happy to\x01",
            "lend them a helping hand.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_E13")

    label("loc_D8F")


    ChrTalk(    #35
        0x9,
        (
            "The patrol ship's still grounded\x01",
            "on the beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "Not that they have many options,\x01",
            "what with orbments not working\x01",
            "and all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E13")

    Jump("loc_1626")

    label("loc_E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_FB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0D")

    ChrTalk(    #37
        0x9,
        (
            "The soldiers on the second floor\x01",
            "are the crew of a downed airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "They're the ones who protected\x01",
            "the village when it was attacked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "Even if their injuries are light,\x01",
            "it's only natural we take good\x01",
            "care of them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_FAE")

    label("loc_F0D")


    ChrTalk(    #40
        0x9,
        (
            "The soldiers who were on\x01",
            "the patrol ship are the ones\x01",
            "who protected us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "Just as they'd gotten everything\x01",
            "under control, all the power was\x01",
            "knocked out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAE")

    Jump("loc_1626")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_10E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_101E")

    ChrTalk(    #42
        0x9,
        (
            "Oh, but the mayoral residence\x01",
            "isn't Dalmore's anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "So who do I contact, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_10E3")

    label("loc_101E")

    OP_A2(0x1)

    ChrTalk(    #44
        0x9,
        (
            "Is that guest really Dalmore's\x01",
            "former butler?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "If so, maybe I should contact the\x01",
            "manor and have someone come\x01",
            "pick him up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "He's so drunk, there's no way\x01",
            "he can get home on his own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E3")

    Jump("loc_1626")

    label("loc_10E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_12CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11AE")

    ChrTalk(    #47
        0x9,
        (
            "See that guest at the table over there?\x01",
            "He's really starting to freak me out.\x01",
            "Nothing he says makes sense!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "He just keeps saying stuff like,\x01",
            "'I'm not me!' It's super creepy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CB")

    label("loc_11AE")

    OP_A2(0x1)

    ChrTalk(    #49
        0x9,
        (
            "See that guest at the table over there?\x01",
            "He's really starting to freak me out.\x01",
            "Nothing he says makes sense!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "Once you start spouting stuff\x01",
            "like, 'I'm not me!', it's over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "Hmm. I think I'm gonna call it.\x01",
            "He's officially been cut off. No more\x01",
            "Azelia Kisses for you, sir!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CB")

    Jump("loc_1626")

    label("loc_12CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_1435")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1376")

    ChrTalk(    #52
        0x9,
        (
            "That poor guest has been so depressed.\x01",
            "It's kind of hard to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "I wonder if he really is the Dalmore\x01",
            "family butler. Or if he was, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1432")

    label("loc_1376")

    OP_A2(0x1)

    ChrTalk(    #54
        0x9,
        (
            "That poor guest looks so depressed.\x01",
            "It's kind of hard to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "He claims he's the butler for the\x01",
            "Dalmore family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "And despite the way he's acting,\x01",
            "it might just be true.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1432")

    Jump("loc_1626")

    label("loc_1435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1626")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1552")

    ChrTalk(    #57
        0x9,
        (
            "That guy deep in his drink over there\x01",
            "is the Dalmore family butler, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "A little hard to believe when he's\x01",
            "just rambling on about one strange\x01",
            "thing after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "...Of course, given how much he's\x01",
            "had to drink, that shouldn't be too\x01",
            "surprising.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1626")

    label("loc_1552")

    OP_A2(0x1)

    ChrTalk(    #60
        0x9,
        "See that guest at the table over there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "That guy's says he's Dalmore family\x01",
            "butler. Or was, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1004FHuh? Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        (
            "I don't know if it's true or not.\x01",
            "That's just what he's been saying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1626")

    TalkEnd(0x9)
    Return()

    # Function_5_C64 end

    def Function_6_162A(): pass

    label("Function_6_162A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_18CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 5)), scpexpr(EXPR_END)), "loc_16C1")

    ChrTalk(    #64
        0xFE,
        "Uhhh... *hic* Th-That wasn't me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "What the maids in the mansion saw...\x01",
            "Th-That Dario wasn't meeeee...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "Uhh... *hic*\x02",
    )

    CloseMessageWindow()
    Jump("loc_18CA")

    label("loc_16C1")

    OP_A2(0x1425)

    ChrTalk(    #67
        0xFE,
        "...*hic*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "*hic* It wasn't...*hic*...me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x105,
        (
            "#042F...\x02\x03",

            "#042F(Estelle...)\x02\x03",

            "(This man is the Dalmore family butler.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1002F(Yeah, it's him, all right.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x104,
        "#032F(Hmm. So it is.)\x02",
    )

    CloseMessageWindow()

    def lambda_178E():
        TurnDirection(0xF7, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_178E)

    def lambda_179C():
        TurnDirection(0x104, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_179C)
    TurnDirection(0x101, 0xFE, 400)
    Sleep(250)

    ChrTalk(    #72
        0xFE,
        "Uhhh... Th-That... That wasn't me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "The me the maids saw...wasn't...\x01",
            "That...*hic*...Dario wasn't me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "Uhh... *hic*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1002F(...)\x02\x03",

            "(What he's talking about?)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_189A")

    ChrTalk(    #76
        0x103,
        "#022F(I think he's telling the truth.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_18CA")

    label("loc_189A")


    ChrTalk(    #77
        0x106,
        "#050F(Yeah... I don't think he's kiddin'.)\x02",
    )

    CloseMessageWindow()

    label("loc_18CA")

    Jump("loc_1C59")

    label("loc_18CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1A00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1958")

    ChrTalk(    #78
        0xFE,
        "*hic* S-Someone, please listen to me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "The me in the mansion wasn't...\x01",
            "*hic*...wasn't me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "Uhh... *hic*...\x02",
    )

    CloseMessageWindow()
    Jump("loc_19FD")

    label("loc_1958")

    OP_A2(0x2)

    ChrTalk(    #81
        0xFE,
        "Uhh... *hic*... Please, believe me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "The me in the mansion wasn't...\x01",
            "*hic*...wasn't me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Th-That's all that's...ungh...\x01",
            "going through...my head...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FD")

    Jump("loc_1C59")

    label("loc_1A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_1B41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1AA4")

    ChrTalk(    #84
        0xFE,
        "Uhh...*hic*... It's so s-strange...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I was on leave... Why...? Wh-Why would\x01",
            "I have been in the mansion?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "*hic* There must be two mes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B3E")

    label("loc_1AA4")

    OP_A2(0x2)

    ChrTalk(    #87
        0xFE,
        "Uh... *hic*... I-It's really strange..\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "I was on vacation...\x01",
            "Wasn't...in the mansion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "*hic* Why does everyone\x01",
            "s-say I was there? *hic*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B3E")

    Jump("loc_1C59")

    label("loc_1B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1BC9")

    ChrTalk(    #90
        0xFE,
        (
            "Th... The good sir being arrested must...\x01",
            "b-be some kind of mistake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "Wh-What happened while I was away...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C59")

    label("loc_1BC9")

    OP_A2(0x2)

    ChrTalk(    #92
        0xFE,
        "Uhhh... *hic*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "Th... The good sir being arrested must...\x01",
            "b-be some kind of mistake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "Wh-What happened while I was away...?\x02",
    )

    CloseMessageWindow()

    label("loc_1C59")

    TalkEnd(0xFE)
    Return()

    # Function_6_162A end

    def Function_7_1C5D(): pass

    label("Function_7_1C5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1C6A")
    Jump("loc_1D9A")

    label("loc_1C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1D9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1CDA")

    ChrTalk(    #95
        0xFE,
        "The lunches here're great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "It's my secret little pleasure\x01",
            "when I come here for work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D9A")

    label("loc_1CDA")

    OP_A2(0x3)

    ChrTalk(    #97
        0xFE,
        (
            "I hear you guys have been cleanin'\x01",
            "house lately. Nice work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "I just defeated a wanted monster\x01",
            "myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "The monsters've been gettin' stronger\x01",
            "lately. It's real rough out there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9A")

    TalkEnd(0xFE)
    Return()

    # Function_7_1C5D end

    def Function_8_1D9E(): pass

    label("Function_8_1D9E")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F15")

    ChrTalk(    #100
        0xFE,
        (
            "My wounds aren't serious, so it\x01",
            "should be fine for me to return to\x01",
            "the ship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "The people at the lodge are so kind,\x01",
            "though. It's hard to leave them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Thanks to all this mess lately,\x01",
            "I've gotten a real sense of where\x01",
            "my duties lie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Protecting people like this is what\x01",
            "a soldier does. It's why we're needed.\x01",
            "And it's a great feeling.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1FE0")

    label("loc_1F15")


    ChrTalk(    #104
        0xFE,
        (
            "Talking with the people at the lodge\x01",
            "here has given me a real sense of\x01",
            "where my duties lie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Protecting people like this is what\x01",
            "a soldier does. It's why we're needed.\x01",
            "And it's a great feeling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE0")

    Jump("loc_218F")

    label("loc_1FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_218F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F4")

    ChrTalk(    #106
        0xFE,
        (
            "All orbal energy on our patrol\x01",
            "ship suddenly cut out while we\x01",
            "were in the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "We got lucky because our altitude\x01",
            "happened to be low, but it was a\x01",
            "hell of a shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "I've got bruises all over me from the\x01",
            "impact of the landing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "Owww...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_218F")

    label("loc_20F4")


    ChrTalk(    #110
        0xFE,
        (
            "We got lucky because our altitude\x01",
            "happened to be low, but it was a\x01",
            "hell of a shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "I've got bruises all over me from the\x01",
            "impact of the landing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218F")

    TalkEnd(0xD)
    Return()

    # Function_8_1D9E end

    SaveToFile()

Try(main)
