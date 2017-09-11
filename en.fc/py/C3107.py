from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3107   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3107.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Captain Amalthea',                     # 9
        '2nd Lieutenant Lorence',               # 10
        'Colonel Richard',                      # 11
        'Black-Clad Man',                       # 12
        'Black-Clad Man',                       # 13
        'Black-Clad Man',                       # 14
        'Black-Clad Man',                       # 15
        'Black-Clad Man',                       # 16
        'Black-Clad Man',                       # 17
        'Special Ops Frigate',                  # 18
        'Special Ops Frigate-Light',            # 19
        'Special Ops Frigate-Shadow',           # 20
        'Soldier',                              # 21
        'Soldier',                              # 22
        'Soldier',                              # 23
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
        'ED6_DT07/CH01610 ._CH',             # 00
        'ED6_DT07/CH02100 ._CH',             # 01
        'ED6_DT07/CH02200 ._CH',             # 02
        'ED6_DT07/CH02030 ._CH',             # 03
        'ED6_DT07/CH00100 ._CH',             # 04
        'ED6_DT07/CH00101 ._CH',             # 05
        'ED6_DT07/CH00110 ._CH',             # 06
        'ED6_DT07/CH00111 ._CH',             # 07
        'ED6_DT07/CH00150 ._CH',             # 08
        'ED6_DT07/CH00151 ._CH',             # 09
        'ED6_DT07/CH00160 ._CH',             # 0A
        'ED6_DT07/CH00161 ._CH',             # 0B
        'ED6_DT06/CH20042 ._CH',             # 0C
        'ED6_DT07/CH00442 ._CH',             # 0D
        'ED6_DT07/CH01650 ._CH',             # 0E
        'ED6_DT07/CH01640 ._CH',             # 0F
        'ED6_DT07/CH01790 ._CH',             # 10
        'ED6_DT07/CH00502 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH01610P._CP',             # 00
        'ED6_DT07/CH02100P._CP',             # 01
        'ED6_DT07/CH02200P._CP',             # 02
        'ED6_DT07/CH02030P._CP',             # 03
        'ED6_DT07/CH00100P._CP',             # 04
        'ED6_DT07/CH00101P._CP',             # 05
        'ED6_DT07/CH00110P._CP',             # 06
        'ED6_DT07/CH00111P._CP',             # 07
        'ED6_DT07/CH00150P._CP',             # 08
        'ED6_DT07/CH00151P._CP',             # 09
        'ED6_DT07/CH00160P._CP',             # 0A
        'ED6_DT07/CH00161P._CP',             # 0B
        'ED6_DT06/CH20042P._CP',             # 0C
        'ED6_DT07/CH00442P._CP',             # 0D
        'ED6_DT07/CH01650P._CP',             # 0E
        'ED6_DT07/CH01640P._CP',             # 0F
        'ED6_DT07/CH01790P._CP',             # 10
        'ED6_DT07/CH00502P._CP',             # 11
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8500,
        Z                   = 0,
        Y                   = 33940,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 12530,
        Z                   = 0,
        Y                   = 33790,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 21330,
        Z                   = 0,
        Y                   = 25970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18240,
        Z                   = 0,
        Y                   = 25980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 22510,
        Z                   = 0,
        Y                   = 25840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17040,
        Z                   = 0,
        Y                   = 25840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17040,
        Z                   = 0,
        Y                   = 25840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17040,
        Z                   = 0,
        Y                   = 25840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17040,
        Z                   = 200,
        Y                   = 25840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 10390,
        Y                   = -1000,
        Z                   = 34100,
        Range               = 11000,
        Unknown_10          = 0x2AF8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 300,
        TriggerZ            = 0,
        TriggerY            = 45490,
        TriggerRange        = 800,
        ActorX              = 300,
        ActorZ              = 1300,
        ActorY              = 45490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_35E",          # 00, 0
        "Function_1_44E",          # 01, 1
        "Function_2_512",          # 02, 2
        "Function_3_528",          # 03, 3
        "Function_4_973",          # 04, 4
        "Function_5_13C5",         # 05, 5
        "Function_6_1584",         # 06, 6
        "Function_7_1D21",         # 07, 7
        "Function_8_1D66",         # 08, 8
        "Function_9_1DBF",         # 09, 9
        "Function_10_2276",        # 0A, 10
        "Function_11_22DB",        # 0B, 11
        "Function_12_2383",        # 0C, 12
        "Function_13_2540",        # 0D, 13
    )


    def Function_0_35E(): pass

    label("Function_0_35E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_36C")
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_37A")
    OP_A3(0x3FB)
    Event(0, 13)

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_388")
    OP_A3(0x3FC)
    Event(0, 12)

    label("loc_388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_390")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DD")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x14, 11810, 0, 31000, 0)
    SetChrPos(0x15, 8930, 0, 32619, 270)
    SetChrPos(0x16, 10250, 500, 34340, 180)

    label("loc_3DD")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 0)), scpexpr(EXPR_END)), "loc_42E")
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 12)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xB, 7830, 0, 33420, 199)
    SetChrPos(0xC, 11920, 0, 31940, 272)

    label("loc_42E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_43A"),
        (SWITCH_DEFAULT, "loc_44D"),
    )


    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44A")
    Event(0, 3)

    label("loc_44A")

    Jump("loc_44D")

    label("loc_44D")

    Return()

    # Function_0_35E end

    def Function_1_44E(): pass

    label("Function_1_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_465")
    OP_72(0x0, 0x10)
    OP_6F(0x0, 9)

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_END)), "loc_470")
    OP_64(0x0, 0x1)

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_481")
    OP_1B(0x0, 0x0, 0xB)

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_505")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_505")
    OP_6F(0xB, 1200)
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)
    SetChrPos(0x11, 19820, 0, 15980, 180)
    SetChrPos(0x12, 19820, 0, 15980, 180)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 19820, 400, 15980, 180)
    OP_A1(0x11, 0xB)
    OP_A1(0x13, 0xC)
    OP_A1(0x12, 0xD)
    OP_6F(0xB, 560)
    OP_6F(0xD, 560)

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_END)), "loc_511")
    OP_22(0xAC, 0x1, 0x64)

    label("loc_511")

    Return()

    # Function_1_44E end

    def Function_2_512(): pass

    label("Function_2_512")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_527")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_512")

    label("loc_527")

    Return()

    # Function_2_512 end

    def Function_3_528(): pass

    label("Function_3_528")

    EventBegin(0x0)
    OP_6D(20, 0, 6550, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2130, 0, 2640, 0)
    SetChrPos(0x102, 870, 0, 2190, 0)
    SetChrPos(0x106, 1560, 0, 3520, 0)
    SetChrPos(0x107, 1680, 0, 1380, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        "#2P#004FOh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#012FI know them...\x02",
    )

    CloseMessageWindow()
    OP_66(0x0)

    def lambda_5EB():
        OP_6D(23090, 0, 16160, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EB)
    Sleep(5000)
    SetChrPos(0x101, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 6480, 45)
    OP_6D(10200, 0, 35370, 3000)
    Sleep(1000)
    OP_6D(-12420, 0, 7490, 3000)

    ChrTalk(    #2
        0x106,
        (
            "#051FHeh...\x01",
            "So they ARE here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        "#065FThe airship from the tower...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#002FI THOUGHT they must be\x01",
            "military...\x02\x03",

            "They look nothing like the\x01",
            "regular soldiers, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#012FThey're probably a special force,\x01",
            "here to practice covert ops.\x02\x03",

            "It's no wonder that they're\x01",
            "so tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        "#065FS-So is my grandpa in there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x106,
        (
            "#057FIt's looking more and more likely.\x02\x03",

            "But if we try to take them\x01",
            "on here, we're going to have\x01",
            "a rough time of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#012FYou're right...\x02\x03",

            "If we cause a disturbance,\x01",
            "we'll get swarmed by the\x01",
            "soldiers inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#002FIsn't there some way we can get\x01",
            "inside without getting spotted?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x565)
    OP_28(0x44, 0x1, 0x4)
    Sleep(100)
    Fade(1000)
    OP_66(0x1)
    OP_6D(-13020, 0, 7160, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -13020, 0, 7160, 0)
    SetChrPos(0x102, -13020, 0, 7160, 0)
    SetChrPos(0x106, -13020, 0, 7160, 0)
    SetChrPos(0x107, -13020, 0, 7160, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_3_528 end

    def Function_4_973(): pass

    label("Function_4_973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BD8")
    EventBegin(0x0)
    OP_6D(10780, 0, 34400, 1500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A78")
    OP_A2(0x54F)

    ChrTalk(    #10
        0x14,
        "H-Hey! They're out cold!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x15,
        (
            "These guys must be pretty damn\x01",
            "tough to take out Special Ops...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x16,
        (
            "The building's empty!\x01",
            "Search the premises!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#004F(Whoa...\x01",
            "Did they spot us?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        "#012F(Fall back for now!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_B62")

    label("loc_A78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAD")

    ChrTalk(    #15
        0x101,
        "#002F(Crap! We have to go back!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_B62")

    label("loc_AAD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF1")

    ChrTalk(    #16
        0x102,
        (
            "#012F(Uh-oh... We'll have to withdraw\x01",
            "for now.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B62")

    label("loc_AF1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2A")

    ChrTalk(    #17
        0x106,
        "#057F(Bah... Gotta pull back again!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_B62")

    label("loc_B2A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B62")

    ChrTalk(    #18
        0x107,
        "#065F(Eeeep! We're gonna get spotted!)\x02",
    )

    CloseMessageWindow()

    label("loc_B62")

    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 7280, 45)
    SetChrPos(0x10B, -13200, 0, 6480, 45)
    OP_6D(-12420, 0, 7490, 0)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_13C4")

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_END)), "loc_11E2")
    EventBegin(0x0)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)
    OP_6D(10780, 0, 34400, 1500)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x106, 8)
    SetChrChipByIndex(0x107, 10)
    SetChrPos(0x106, 7580, 0, 27490, 0)
    SetChrPos(0x101, 8140, 0, 26150, 0)
    SetChrPos(0x102, 6300, 0, 26560, 0)
    SetChrPos(0x107, 7180, 0, 25690, 0)

    ChrTalk(    #19
        0xB,
        (
            "*sigh*... I really wanted to be\x01",
            "part of the Grancel operation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "But nooo... I'm left here,\x01",
            "guarding an old man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xC,
        "*grumble*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xC,
        (
            "We do so much for the kingdom,\x01",
            "and for our dream...all in the\x01",
            "colonel's name...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        (
            "Such is the life of the Intelligence\x01",
            "Division's Special Ops, I suppose.\x01",
            "We're the colonel's hands and eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        (
            "Hmph... If you ask me, you're the\x01",
            "colonel's ass!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)

    def lambda_DFC():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DFC)
    TurnDirection(0xB, 0x106, 400)

    NpcTalk(    #25
        0xB,
        "Special Ops Soldier",
        "What...?\x02",
    )

    CloseMessageWindow()

    def lambda_E33():
        OP_6D(9740, 0, 30350, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E33)
    OP_6C(52000, 1500)

    NpcTalk(    #26
        0xB,
        "Special Ops Soldier",
        "I-It can't be!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #27
        0xC,
        "Special Ops Soldier",
        "#4PAgate Crosner?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0xB, 13)
    SetChrSubChip(0xB, 0)
    Sleep(100)
    SetChrChipByIndex(0xC, 13)
    SetChrSubChip(0xC, 0)

    ChrTalk(    #28
        0x106,
        "#054FYou're too damn slow!\x02",
    )

    CloseMessageWindow()

    def lambda_F05():
        OP_8E(0xFE, 0x299A, 0x0, 0x8476, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_F05)
    Sleep(50)

    def lambda_F25():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F25)
    Sleep(50)

    def lambda_F3F():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F3F)
    Sleep(100)

    def lambda_F59():
        OP_8E(0xFE, 0x299A, 0x0, 0x8476, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_F59)
    Sleep(300)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    Battle(0x252, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_F9C"),
        (SWITCH_DEFAULT, "loc_F9F"),
    )


    label("loc_F9C")

    OP_B4(0x0)
    Return()

    label("loc_F9F")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 12)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    OP_6D(8250, 0, 31140, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, 7830, 0, 33420, 199)
    SetChrPos(0xC, 11920, 0, 31940, 272)
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 12)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrPos(0x106, 8240, 0, 31790, 45)
    SetChrPos(0x101, 8960, 0, 30390, 45)
    SetChrPos(0x102, 6540, 0, 31580, 45)
    SetChrPos(0x107, 7210, 0, 30100, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #29
        0x106,
        (
            "#051FHeh... Sucks to be you.\x02\x03",

            "It's no fun when someone gets\x01",
            "back at you for making a fool\x01",
            "of him, huh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #30
        0x101,
        (
            "#506FIt's not good to carry a grudge,\x01",
            "you know...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1144():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1144)

    def lambda_1152():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1152)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #31
        0x102,
        (
            "#012FNow it's a race against time.\x02\x03",

            "We have to get the professor\x01",
            "out as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x107,
        "#560FRight!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x568)
    OP_28(0x44, 0x1, 0x20)
    EventEnd(0x0)
    Jump("loc_13C4")

    label("loc_11E2")

    EventBegin(0x0)
    OP_6D(10780, 0, 34400, 1500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1278")
    OP_A2(0x566)

    ChrTalk(    #33
        0xB,
        (
            "Hmm...? I thought I saw\x01",
            "something move...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#004F(Whoa... Did they spot us?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#012F(Fall back for now!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1362")

    label("loc_1278")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AD")

    ChrTalk(    #36
        0x101,
        "#002F(Crap! We have to go back!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1362")

    label("loc_12AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F1")

    ChrTalk(    #37
        0x102,
        (
            "#012F(Uh-oh... We'll have to withdraw\x01",
            "for now.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1362")

    label("loc_12F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132A")

    ChrTalk(    #38
        0x106,
        "#057F(Bah... Gotta pull back again!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1362")

    label("loc_132A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1362")

    ChrTalk(    #39
        0x107,
        "#065F(Eeeep! We're gonna get spotted!)\x02",
    )

    CloseMessageWindow()

    label("loc_1362")

    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 6480, 45)
    OP_6D(-12420, 0, 7490, 0)
    OP_0D()
    EventEnd(0x0)

    label("loc_13C4")

    Return()

    # Function_4_973 end

    def Function_5_13C5(): pass

    label("Function_5_13C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1583")
    OP_A2(0x567)
    OP_28(0x44, 0x1, 0x8)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-490, 0, 45500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(63000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -490, 0, 45980, 90)
    SetChrPos(0x102, -1420, 0, 46110, 90)
    SetChrPos(0x107, -490, 0, 45040, 90)
    SetChrPos(0x106, -1380, 0, 45220, 90)
    OP_0D()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #40
        0x101,
        (
            "#006FHey...\x01",
            "Can't we get in from here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#013FNo...there are iron bars over\x01",
            "the windows.\x02\x03",

            "If we make any noise, this is\x01",
            "going to get even tougher.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x107,
        "#065F...Oh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x106,
        "#057FJackpot...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #44
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C3115   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1583")

    Return()

    # Function_5_13C5 end

    def Function_6_1584(): pass

    label("Function_6_1584")

    EventBegin(0x0)
    OP_6F(0xB, 1200)
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)
    SetChrPos(0x11, 19820, 0, 15980, 180)
    SetChrPos(0x12, 19820, 0, 15980, 180)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 19820, 400, 15980, 180)
    OP_A1(0x11, 0xB)
    OP_A1(0x13, 0xC)
    OP_A1(0x12, 0xD)
    OP_6F(0xB, 560)
    OP_6F(0xD, 560)
    OP_6D(-1910, 0, 45400, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x107, -1470, 0, 45910, 0)
    SetChrPos(0x106, -1230, 0, 44430, 0)
    SetChrPos(0x101, -2870, 0, 44560, 0)
    SetChrPos(0x102, -3200, 0, 46380, 0)
    TurnDirection(0x101, 0x107, 0)
    TurnDirection(0x107, 0x101, 0)
    TurnDirection(0x102, 0x101, 0)
    TurnDirection(0x106, 0x101, 0)
    OP_0D()

    ChrTalk(    #45
        0x101,
        (
            "#002FSo...Colonel Richard was the\x01",
            "man behind all this trouble.\x02\x03",

            "Plus, it looks like he\x01",
            "wants to find my dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#013FYeah... I wonder what\x01",
            "that's all about.\x02\x03",

            "And who was that masked man?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x106,
        (
            "#057FOf COURSE that bastard\x01",
            "would show up now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x106, 135, 400)

    ChrTalk(    #48
        0x106,
        "#052FHmph. And there he goes. \x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(21250, 0, 16520, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4170, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x75, 0x1, 0x64)
    OP_6F(0xB, 1200)
    OP_6F(0xD, 1200)
    SetChrPos(0x8, 20330, 0, 28410, 180)
    SetChrPos(0x9, 19810, 0, 30280, 180)
    SetChrPos(0xA, 19810, 0, 27620, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_43(0xA, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x7)

    def lambda_1890():
        OP_6C(102000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1890)

    def lambda_18A0():
        OP_6D(19600, 3300, 18970, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18A0)
    Sleep(1000)
    OP_43(0xD, 0x1, 0x0, 0x8)
    Sleep(500)
    OP_43(0xE, 0x1, 0x0, 0x8)
    Sleep(400)
    OP_43(0xF, 0x1, 0x0, 0x8)
    Sleep(500)
    OP_43(0x10, 0x1, 0x0, 0x8)
    SetChrBattleFlags(0x9, 0x20)
    OP_8E(0x9, 0x4D80, 0xCE4, 0x4876, 0x7D0, 0x0)
    Sleep(1000)
    TurnDirection(0x9, 0x102, 400)
    Sleep(500)

    ChrTalk(    #49
        0x9,
        (
            "#280FGrand plans...but what will\x01",
            "come of them?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    Sleep(100)
    OP_8E(0x9, 0x4D80, 0xCE4, 0x4592, 0xBB8, 0x0)

    def lambda_1966():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1966)
    OP_8E(0x9, 0x4D80, 0xCE4, 0x3C50, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    Sleep(1000)
    OP_43(0x11, 0x1, 0x0, 0x9)
    WaitChrThread(0x11, 0x1)
    Sleep(3000)
    OP_44(0x101, 0xFF)
    Fade(1000)
    OP_6D(-1180, 0, 35690, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, -1920, 0, 35410, 135)
    SetChrPos(0x101, -840, 0, 35470, 135)
    SetChrPos(0x102, -2220, 0, 36430, 135)
    SetChrPos(0x107, -1130, 0, 36470, 135)
    OP_0D()

    ChrTalk(    #50
        0x106,
        (
            "#051FNOW things have gotten\x01",
            "interesting...\x02\x03",

            "I really wanted to settle the score\x01",
            "with him, but I've got a job to do,\x01",
            "and that takes precedence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#006FSince the window's a no-go, we'll\x01",
            "have to take out the guards.\x02\x03",

            "Let's make this quick and clean!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x107,
        "#062FR-Right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#510F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #54
        0x101,
        (
            "#004F#4PJoshua?\x01",
            "Hey, you listening?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B82():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B82)

    def lambda_1B90():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1B90)

    def lambda_1B9E():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1B9E)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #55
        0x102,
        "#014FUm...Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x107,
        "#065F#4PA-Are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x106,
        (
            "#052F#4PHey, snap out of it. It's not\x01",
            "like you to freeze up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#013FS-Sorry...\x01",
            "I just spaced out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#002F#4PAre you sure you're feeling okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        (
            "#010FI'm fine. It's no big deal.\x02\x03",

            "We have to take out the guards\x01",
            "by the entrance, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x106,
        (
            "#050F#4PYep...\x01",
            "So let's get a move on.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x44, 0x1, 0x10)
    OP_44(0x11, 0xFF)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    EventEnd(0x0)
    Return()

    # Function_6_1584 end

    def Function_7_1D21(): pass

    label("Function_7_1D21")

    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0x4D80, 0xCE4, 0x4592, 0xBB8, 0x0)

    def lambda_1D40():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1D40)
    OP_8E(0xFE, 0x4D80, 0xCE4, 0x3C50, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_7_1D21 end

    def Function_8_1D66(): pass

    label("Function_8_1D66")

    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0x4D80, 0x0, 0x6644, 0xBB8, 0x0)
    OP_8E(0xFE, 0x4D80, 0xCE4, 0x4592, 0xBB8, 0x0)

    def lambda_1D99():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1D99)
    OP_8E(0xFE, 0x4D80, 0xCE4, 0x3C50, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_8_1D66 end

    def Function_9_1DBF(): pass

    label("Function_9_1DBF")

    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x12, 0x4)
    OP_71(0xB, 0x2)
    OP_71(0xC, 0x2)
    OP_71(0xD, 0x2)
    OP_22(0xE6, 0x0, 0x64)
    OP_6F(0xB, 1200)
    OP_6F(0xD, 1200)
    OP_70(0xB, 0x474)
    OP_70(0xD, 0x474)
    OP_73(0xB)

    def lambda_1E07():
        OP_6C(0, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E07)

    def lambda_1E17():
        OP_6D(19690, 3300, 12830, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E17)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0xB, 361)
    OP_6F(0xD, 361)
    OP_70(0xB, 0x230)
    OP_70(0xD, 0x230)
    OP_73(0xB)
    WaitChrThread(0x101, 0x2)
    OP_72(0xD, 0x4)
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    PlayEffect(0x1, 0x1, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xB, 561)
    OP_6F(0xD, 561)
    OP_70(0xB, 0x244)
    OP_70(0xD, 0x244)
    OP_73(0xB)
    OP_6F(0xB, 581)
    OP_6F(0xD, 581)
    OP_70(0xB, 0x28A)
    OP_70(0xD, 0x28A)

    def lambda_1EEB():
        OP_6D(19690, 8020, 12830, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EEB)

    def lambda_1F03():
        OP_91(0x12, 0x0, 0x1F4, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1F03)
    OP_91(0x11, 0x0, 0x1F4, 0x0, 0x3E8, 0x0)

    def lambda_1F32():
        OP_91(0x12, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1F32)
    OP_91(0x11, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)

    def lambda_1F61():
        OP_91(0x12, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1F61)
    OP_91(0x11, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)

    def lambda_1F90():
        OP_91(0x12, 0x0, 0x3E8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1F90)
    OP_91(0x11, 0x0, 0x3E8, 0x0, 0xBB8, 0x0)

    def lambda_1FBF():
        OP_91(0x12, 0x0, 0x1F4, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1FBF)
    OP_91(0x11, 0x0, 0x1F4, 0x0, 0x7D0, 0x0)

    def lambda_1FEE():
        OP_91(0x12, 0x0, 0x1F4, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1FEE)
    OP_91(0x11, 0x0, 0x1F4, 0x0, 0x3E8, 0x0)

    def lambda_201D():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF7CCA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_201D)

    def lambda_2038():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF7CCA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2038)

    def lambda_2053():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF7CCA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2053)

    def lambda_206E():
        OP_6D(20020, 10000, -13080, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_206E)
    OP_6F(0xB, 651)
    OP_6F(0xD, 651)
    OP_70(0xB, 0x2A8)
    OP_70(0xD, 0x2A8)
    OP_73(0xB)
    OP_43(0x12, 0x0, 0x0, 0xA)

    def lambda_20AC():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF7CCA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_20AC)

    def lambda_20C7():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF7CCA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_20C7)

    def lambda_20E2():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF7CCA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_20E2)
    OP_71(0xB, 0x20)
    OP_71(0xD, 0x20)
    OP_6F(0xB, 680)
    OP_6F(0xD, 680)
    OP_70(0xB, 0x30C)
    OP_70(0xD, 0x30C)
    Sleep(1000)

    def lambda_2128():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF079A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2128)

    def lambda_2143():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF079A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2143)

    def lambda_215E():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF079A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_215E)
    Sleep(500)

    def lambda_217E():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF079A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_217E)

    def lambda_2199():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF079A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2199)

    def lambda_21B4():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF079A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_21B4)
    Sleep(500)

    def lambda_21D4():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF079A, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_21D4)

    def lambda_21EF():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF079A, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_21EF)

    def lambda_220A():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF079A, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_220A)
    Sleep(500)

    def lambda_222A():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF079A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_222A)

    def lambda_2245():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF079A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2245)

    def lambda_2260():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF079A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2260)
    Return()

    # Function_9_1DBF end

    def Function_10_2276(): pass

    label("Function_10_2276")

    OP_24(0x75, 0x5A)
    OP_24(0x77, 0x5A)
    Sleep(200)
    OP_24(0x75, 0x50)
    OP_24(0x77, 0x50)
    Sleep(200)
    OP_24(0x75, 0x46)
    OP_24(0x77, 0x46)
    Sleep(200)
    OP_24(0x75, 0x3C)
    OP_24(0x77, 0x3C)
    Sleep(200)
    OP_24(0x75, 0x32)
    OP_24(0x77, 0x32)
    Sleep(200)
    OP_24(0x75, 0x28)
    OP_24(0x77, 0x28)
    Sleep(200)
    OP_24(0x75, 0x1E)
    OP_24(0x77, 0x1E)
    Sleep(200)
    OP_23(0x75)
    OP_23(0x77)
    OP_23(0xCF)
    Return()

    # Function_10_2276 end

    def Function_11_22DB(): pass

    label("Function_11_22DB")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(11490, 0, 31730, 0)
    OP_0D()
    OP_62(0xC, 0xFFFFFE0C, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xC)

    NpcTalk(    #62
        0xC,
        "Special Ops Soldier",
        (
            "Ungh...agh... You think...\x01",
            "we'll just let you escape?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_22(0xAC, 0x1, 0x64)
    OP_A2(0x3FA)
    OP_A2(0x56A)
    OP_28(0x44, 0x1, 0x80)
    NewScene("ED6_DT01/C3105   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_11_22DB end

    def Function_12_2383(): pass

    label("Function_12_2383")

    EventBegin(0x0)
    OP_6D(-12420, 0, 7490, 0)
    SetChrPos(0x101, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 7280, 45)
    SetChrPos(0x10B, -13200, 0, 6480, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #63
        0x10B,
        (
            "#102FGetting through the airship\x01",
            "port to the wharf isn't going\x01",
            "to be easy.\x02\x03",

            "We'll have to find another\x01",
            "escape route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x102,
        (
            "#012FYes... Getting anywhere near\x01",
            "there is probably unwise.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x14, 11810, 0, 31000, 0)
    SetChrPos(0x15, 8930, 0, 32619, 270)
    SetChrPos(0x16, 10250, 500, 34340, 180)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2513")
    OP_28(0x44, 0x1, 0x2000)
    Jump("loc_253A")

    label("loc_2513")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2528")
    OP_28(0x44, 0x1, 0x4000)
    Jump("loc_253A")

    label("loc_2528")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_253A")
    OP_28(0x44, 0x1, 0x8000)

    label("loc_253A")

    OP_A2(0x54D)
    EventEnd(0x0)
    Return()

    # Function_12_2383 end

    def Function_13_2540(): pass

    label("Function_13_2540")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2555")
    OP_28(0x44, 0x1, 0x2000)
    Jump("loc_257C")

    label("loc_2555")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_256A")
    OP_28(0x44, 0x1, 0x4000)
    Jump("loc_257C")

    label("loc_256A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257C")
    OP_28(0x44, 0x1, 0x8000)

    label("loc_257C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2764")
    EventBegin(0x0)
    OP_6D(-12420, 0, 7490, 0)
    SetChrPos(0x101, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 7280, 45)
    SetChrPos(0x10B, -13200, 0, 6480, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #65
        0x107,
        (
            "#561F*huff* *huff*\x02\x03",

            "#063FUm... Are those soldiers\x01",
            "going to be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x106,
        (
            "#053FOh, don't sweat it...\x01",
            "They're just unconscious.\x02\x03",

            "#552FAnyway, the less fighting we\x01",
            "have to deal with, the better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        (
            "#012FWe'll have to avoid the soldiers\x01",
            "while we look for another way out.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x14, 11810, 0, 31000, 0)
    SetChrPos(0x15, 8930, 0, 32619, 270)
    SetChrPos(0x16, 10250, 500, 34340, 180)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 9)
    OP_A2(0x54E)
    EventEnd(0x0)
    Jump("loc_27CC")

    label("loc_2764")

    OP_6D(-12420, 0, 7490, 0)
    SetChrPos(0x0, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 7280, 45)
    SetChrPos(0x10B, -13200, 0, 6480, 45)
    OP_30(0x1)

    label("loc_27CC")

    Return()

    # Function_13_2540 end

    SaveToFile()

Try(main)
