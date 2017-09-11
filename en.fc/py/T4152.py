from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4152   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4152.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Nial',                                 # 9
        'Soldier',                              # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Pigeon',                               # 16
        'Pigeon',                               # 17
        'Pigeon',                               # 18
        'Pigeon',                               # 19
        'Pigeon',                               # 20
        'Pigeon',                               # 21
        'Pigeon',                               # 22
        'Pigeon',                               # 23
        'Pigeon',                               # 24
        'Pigeon',                               # 25
        'Grancel - North Block',                # 26
        'Grancel - West Block',                 # 27
    )

    DeclEntryPoint(
        Unknown_00              = -80000,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 4200,
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH01650 ._CH',             # 01
        'ED6_DT07/CH01730 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT07/CH01350 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01030 ._CH',             # 07
        'ED6_DT07/CH01640 ._CH',             # 08
        'ED6_DT07/CH01680 ._CH',             # 09
        'ED6_DT07/CH01690 ._CH',             # 0A
        'ED6_DT07/CH01330 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH01650P._CP',             # 01
        'ED6_DT07/CH01730P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT07/CH01350P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01030P._CP',             # 07
        'ED6_DT07/CH01640P._CP',             # 08
        'ED6_DT07/CH01680P._CP',             # 09
        'ED6_DT07/CH01690P._CP',             # 0A
        'ED6_DT07/CH01330P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        X                   = -39960,
        Z                   = 0,
        Y                   = 43920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -7520,
        Z                   = 300,
        Y                   = -20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -82190,
        Y                   = 0,
        Z                   = 13740,
        Range               = -75710,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x292C,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -63040,
        Y                   = -3750,
        Z                   = -33480,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = -63390,
        Y                   = -3750,
        Z                   = -24940,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -78840,
        Y                   = 1250,
        Z                   = 12430,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 19,
    )


    DeclActor(
        TriggerX            = -76990,
        TriggerZ            = -3500,
        TriggerY            = -30450,
        TriggerRange        = 800,
        ActorX              = -76990,
        ActorZ              = -2500,
        ActorY              = -30450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -92000,
        TriggerZ            = 800,
        TriggerY            = -4000,
        TriggerRange        = 800,
        ActorX              = -92000,
        ActorZ              = 1800,
        ActorY              = -4000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -72220,
        TriggerZ            = -3180,
        TriggerY            = -15630,
        TriggerRange        = 800,
        ActorX              = -72220,
        ActorZ              = -2000,
        ActorY              = -15630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_456",          # 00, 0
        "Function_1_473",          # 01, 1
        "Function_2_5A0",          # 02, 2
        "Function_3_5B6",          # 03, 3
        "Function_4_AA8",          # 04, 4
        "Function_5_C7A",          # 05, 5
        "Function_6_EC8",          # 06, 6
        "Function_7_EEF",          # 07, 7
        "Function_8_F16",          # 08, 8
        "Function_9_F84",          # 09, 9
        "Function_10_FF2",         # 0A, 10
        "Function_11_1060",        # 0B, 11
        "Function_12_10CE",        # 0C, 12
        "Function_13_1262",        # 0D, 13
        "Function_14_14CD",        # 0E, 14
        "Function_15_1596",        # 0F, 15
        "Function_16_1614",        # 10, 16
        "Function_17_1676",        # 11, 17
        "Function_18_167A",        # 12, 18
        "Function_19_167E",        # 13, 19
    )


    def Function_0_456(): pass

    label("Function_0_456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_464")
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_472")
    OP_A3(0x3FB)
    Event(0, 13)

    label("loc_472")

    Return()

    # Function_0_456 end

    def Function_1_473(): pass

    label("Function_1_473")

    OP_16(0x2, 0xFA0, 0xFFFD2D58, 0xFFFE0048, 0x3005D)
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49A")
    OP_72(0xA, 0x10)
    OP_65(0x0, 0x1)

    label("loc_49A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AD")
    OP_1B(0x3, 0x0, 0xE)

    label("loc_4AD")

    OP_72(0xE, 0x8)
    OP_72(0xE, 0x20)
    OP_72(0xE, 0x2)
    OP_6F(0xE, 0)
    OP_72(0xB, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x7, 0x10)
    OP_72(0xD, 0x10)
    OP_72(0x5, 0x10)
    OP_72(0x9, 0x10)
    OP_72(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59F")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_43(0x9, 0x1, 0x0, 0x5)
    OP_43(0xA, 0x1, 0x0, 0x5)
    OP_43(0xB, 0x1, 0x0, 0x5)
    OP_43(0xC, 0x1, 0x0, 0x5)
    OP_43(0xD, 0x1, 0x0, 0x5)
    OP_43(0xE, 0x1, 0x0, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_545")

    label("loc_545")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_550")

    label("loc_550")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_564")
    SetChrFlags(0xB, 0x80)
    OP_44(0xB, 0xFF)

    label("loc_564")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_578")
    SetChrFlags(0xD, 0x80)
    OP_44(0xD, 0xFF)

    label("loc_578")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_58C")
    SetChrFlags(0xE, 0x80)
    OP_44(0xE, 0xFF)

    label("loc_58C")

    OP_6B(4200, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59F")

    Return()

    # Function_1_473 end

    def Function_2_5A0(): pass

    label("Function_2_5A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5A0")

    label("loc_5B5")

    Return()

    # Function_2_5A0 end

    def Function_3_5B6(): pass

    label("Function_3_5B6")

    EventBegin(0x0)
    OP_6D(-63290, -3220, -25240, 0)
    OP_67(0, 12660, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(442, 0)

    def lambda_5FB():
        OP_67(0, 9500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5FB)

    def lambda_613():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_613)

    def lambda_623():
        OP_6C(270000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_623)

    def lambda_633():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_633)
    SetChrPos(0x101, -61850, -3500, -25070, 270)
    SetChrPos(0x102, -62010, -3500, -26170, 270)
    SetChrPos(0x8, -63080, -3500, -25100, 270)
    ClearChrFlags(0x8, 0x80)
    Sleep(6000)

    ChrTalk(    #0
        0x101,
        (
            "#000FHeeey, this is a nice little place.\x02\x03",

            "Feels less like a bar and\x01",
            "more like a coffee shop.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #1
        0x102,
        (
            "#010FThat might explain the\x01",
            "smell of coffee.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    ChrTalk(    #2
        0x8,
        (
            "#141F#6PI hear the owner started up\x01",
            "this place as a hobby.\x02\x03",

            "The brew here is amazing.\x02\x03",

            "Plus, he took some advice from someone\x01",
            "later on and added curry rice to the\x01",
            "menu. Curry with AUTHENTIC spices.\x02\x03",

            "I just like the atmosphere out here,\x01",
            "though, personally. Have a seat! Let's\x01",
            "get this interview started!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#005F#3SNot so fast!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(200)

    ChrTalk(    #4
        0x101,
        (
            "#007FWe were just in that big match, so we're\x01",
            "pretty damned hungry. And I'm not about\x01",
            "to smell food without EATING food!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#019FDinner does sound lovely right\x01",
            "about now, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#142F#6PGrrr... Damn kids.\x02\x03",

            "#144FFine! I'll buy you dinner.\x02\x03",

            "And while you're stuffing your faces,\x01",
            "you can give me the exclusive on any\x01",
            "news you've found!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#006FAaaand, there's the pitch!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#014FBy the way, isn't Dorothy\x01",
            "with you today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#140F#6PNah, I gave her something else\x01",
            "to work on...\x02\x03",

            "Now, come on.\x01",
            "Inside with the both of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4137   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_5B6 end

    def Function_4_AA8(): pass

    label("Function_4_AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFB")
    EventBegin(0x1)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #10
        "\x07\x05It's locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x1)
    Jump("loc_C79")

    label("loc_AFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C06")
    EventBegin(0x1)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #11
        "\x07\x05It's locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #12
        0x102,
        (
            "#010FThis must be the entrance to\x01",
            "the Grancel Sewers that the\x01",
            "Ravens mentioned.\x02\x03",

            "It's late, so why don't we check\x01",
            "this out tomorrow when Zin and\x01",
            "Olivier are with us.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_C79")

    label("loc_C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C79")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #13
        "\x07\x00Used \x07\x02Grancel Sewer Key A\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x622)
    OP_70(0xA, 0x3C)
    OP_73(0xA)
    OP_64(0x0, 0x1)
    OP_71(0xA, 0x10)
    EventEnd(0x0)

    label("loc_C79")

    Return()

    # Function_4_AA8 end

    def Function_5_C7A(): pass

    label("Function_5_C7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC7")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCA")

    label("loc_CAD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCA")

    label("loc_CD3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCA")

    label("loc_CF9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D20")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCA")

    label("loc_D20")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D46")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCA")

    label("loc_D46")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCA")

    label("loc_D6C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D91")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCA")

    label("loc_D91")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCA")

    label("loc_DB6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DCA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB5")

    ChrTalk(    #14
        0xFE,
        "Hey! You two!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#580F(Crap...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#017F(Caught already...)\x02",
    )

    CloseMessageWindow()

    label("loc_EB5")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_EC4")

    Jump("Function_5_C7A")

    label("loc_EC7")

    Return()

    # Function_5_C7A end

    def Function_6_EC8(): pass

    label("Function_6_EC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EEE")
    SetChrPos(0xFE, -42250, 0, -8170, 180)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_6_EC8")

    label("loc_EEE")

    Return()

    # Function_6_EC8 end

    def Function_7_EEF(): pass

    label("Function_7_EEF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F15")
    SetChrPos(0xFE, -38960, 0, -8109, 180)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_7_EEF")

    label("loc_F15")

    Return()

    # Function_7_EEF end

    def Function_8_F16(): pass

    label("Function_8_F16")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F83")
    SetChrPos(0xFE, -54990, -3750, -18870, 180)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    Jump("Function_8_F16")

    label("loc_F83")

    Return()

    # Function_8_F16 end

    def Function_9_F84(): pass

    label("Function_9_F84")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FF1")
    SetChrPos(0xFE, -74820, -3500, -19000, 180)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    Jump("Function_9_F84")

    label("loc_FF1")

    Return()

    # Function_9_F84 end

    def Function_10_FF2(): pass

    label("Function_10_FF2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_105F")
    SetChrPos(0xFE, -74820, -3500, -30850, 180)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    Jump("Function_10_FF2")

    label("loc_105F")

    Return()

    # Function_10_FF2 end

    def Function_11_1060(): pass

    label("Function_11_1060")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10CD")
    SetChrPos(0xFE, -54990, -3750, -30850, 180)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    Jump("Function_11_1060")

    label("loc_10CD")

    Return()

    # Function_11_1060 end

    def Function_12_10CE(): pass

    label("Function_12_10CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1261")
    OP_A2(0x62E)
    OP_28(0x48, 0x1, 0x200)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -78280, 1760, 11580, 0)
    SetChrPos(0x102, -79290, 1760, 11770, 45)

    def lambda_1112():
        OP_6C(350000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1112)
    OP_6D(-79030, 1760, 13490, 2000)
    Fade(1000)
    OP_6B(2800, 0)
    OP_0D()

    ChrTalk(    #17
        0x101,
        "#001F(All right, we made it!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#012F(Stay focused, Estelle...)\x02\x03",

            "(I'll go in first. Stay close.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#002F(Okay...!)\x02",
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xFFFECB04, 0x6E0, 0x30C0, 0x7D0, 0x0)
    OP_8C(0x102, 0, 400)
    OP_70(0xC, 0x3C)
    OP_73(0xC)

    def lambda_11E5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11E5)

    def lambda_11F7():
        OP_8E(0xFE, 0xFFFECBB8, 0x6E0, 0x369C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11F7)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_8E(0x101, 0xFFFECCDA, 0x6E0, 0x30A2, 0x7D0, 0x0)

    def lambda_1235():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1235)
    OP_8E(0x101, 0xFFFECBB8, 0x6E0, 0x369C, 0x7D0, 0x0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4134   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1261")

    Return()

    # Function_12_10CE end

    def Function_13_1262(): pass

    label("Function_13_1262")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_6D(-79450, 4770, 11320, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(39000, 0)
    OP_6E(478, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0xF, -80280, 1520, 11070, 218)
    SetChrPos(0x10, -77730, 1490, 10600, 146)
    SetChrPos(0x11, -81930, 1250, 9130, 327)
    SetChrPos(0x12, -79450, 1250, 9450, 44)
    SetChrPos(0x13, -76040, 1250, 8290, 156)
    SetChrPos(0x14, -81880, 750, 6280, 145)
    SetChrPos(0x15, -79420, 250, 5000, 190)
    SetChrPos(0x16, -77590, 750, 6270, 7)

    def lambda_138E():
        OP_67(0, 11700, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_138E)

    def lambda_13A6():
        OP_6C(351000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13A6)

    def lambda_13B6():
        OP_6E(544, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13B6)

    def lambda_13C6():
        OP_90(0xFE, 0xFFFFEC78, 0x27B0, 0xFFFFB1E0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_13C6)
    Sleep(500)

    def lambda_13E6():
        OP_90(0xFE, 0xFFFFF63C, 0x6630, 0xFFFFADF8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13E6)

    def lambda_1401():
        OP_90(0xFE, 0x2710, 0x4EC0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1401)
    Sleep(200)

    def lambda_1421():
        OP_90(0xFE, 0x3A98, 0x3B38, 0xFFFFC568, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1421)
    Sleep(200)

    def lambda_1441():
        OP_90(0xFE, 0x3A98, 0x4EC0, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1441)

    def lambda_145C():
        OP_90(0xFE, 0xFFFFEC78, 0x3B38, 0xFFFFD8F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_145C)
    Sleep(500)

    def lambda_147C():
        OP_90(0xFE, 0x3A98, 0x3B38, 0xFFFFEC78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_147C)
    Sleep(300)

    def lambda_149C():
        OP_90(0xFE, 0xFFFFD8F0, 0x3B38, 0xFFFFC568, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_149C)
    Sleep(100)
    Sleep(200)
    Sleep(7000)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1262 end

    def Function_14_14CD(): pass

    label("Function_14_14CD")

    EventBegin(0x1)

    ChrTalk(    #20
        0x102,
        (
            "#010FThis must be the entrance to\x01",
            "the Grancel Sewers that the\x01",
            "Ravens mentioned.\x02\x03",

            "It's late, so why don't we check\x01",
            "this out tomorrow when Zin and\x01",
            "Olivier are with us.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_14_14CD end

    def Function_15_1596(): pass

    label("Function_15_1596")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #21
        (
            "\x07\x05Harbor District\x01",
            "※Unauthorized entry prohibited\x01",
            "due to heightened security.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_1596 end

    def Function_16_1614(): pass

    label("Function_16_1614")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #22
        (
            "\x07\x05House for Sale\x01",
            "※Easy conversion to restaurant!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_1614 end

    def Function_17_1676(): pass

    label("Function_17_1676")

    SetPlaceName(0xB8)
    Return()

    # Function_17_1676 end

    def Function_18_167A(): pass

    label("Function_18_167A")

    SetPlaceName(0xB7)
    Return()

    # Function_18_167A end

    def Function_19_167E(): pass

    label("Function_19_167E")

    SetPlaceName(0xAF)
    Return()

    # Function_19_167E end

    SaveToFile()

Try(main)
