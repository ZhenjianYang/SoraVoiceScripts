from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2200.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60020",
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
        'Clem',                                 # 9
        'Manoria Village',                      # 10
        'Mercia Orphanage',                     # 11
        'Ruan',                                 # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
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
        Unknown_3A              = 101,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02590 ._CH',             # 00
        'ED6_DT07/CH00040 ._CH',             # 01
        'ED6_DT07/CH00041 ._CH',             # 02
        'ED6_DT09/CH10160 ._CH',             # 03
        'ED6_DT09/CH10161 ._CH',             # 04
        'ED6_DT09/CH10450 ._CH',             # 05
        'ED6_DT09/CH10451 ._CH',             # 06
        'ED6_DT09/CH10220 ._CH',             # 07
        'ED6_DT09/CH10221 ._CH',             # 08
        'ED6_DT09/CH10460 ._CH',             # 09
        'ED6_DT09/CH10461 ._CH',             # 0A
        'ED6_DT09/CH10480 ._CH',             # 0B
        'ED6_DT09/CH10481 ._CH',             # 0C
        'ED6_DT09/CH10470 ._CH',             # 0D
        'ED6_DT09/CH10471 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02590P._CP',             # 00
        'ED6_DT07/CH00040P._CP',             # 01
        'ED6_DT07/CH00041P._CP',             # 02
        'ED6_DT09/CH10160P._CP',             # 03
        'ED6_DT09/CH10161P._CP',             # 04
        'ED6_DT09/CH10450P._CP',             # 05
        'ED6_DT09/CH10451P._CP',             # 06
        'ED6_DT09/CH10220P._CP',             # 07
        'ED6_DT09/CH10221P._CP',             # 08
        'ED6_DT09/CH10460P._CP',             # 09
        'ED6_DT09/CH10461P._CP',             # 0A
        'ED6_DT09/CH10480P._CP',             # 0B
        'ED6_DT09/CH10481P._CP',             # 0C
        'ED6_DT09/CH10470P._CP',             # 0D
        'ED6_DT09/CH10471P._CP',             # 0E
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
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
        X                   = -139370,
        Z                   = -2020,
        Y                   = 15120,
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
        X                   = -28630,
        Z                   = -1990,
        Y                   = 79340,
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
        X                   = 7410,
        Z                   = -2000,
        Y                   = 29980,
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


    DeclMonster(
        X                   = -96260,
        Z                   = -1950,
        Y                   = 27960,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x181,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -104740,
        Z                   = -5970,
        Y                   = 11000,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -81100,
        Z                   = -5870,
        Y                   = 13330,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88220,
        Z                   = -5960,
        Y                   = 9810,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -96260,
        Z                   = -1950,
        Y                   = 27960,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x325,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -104740,
        Z                   = -5970,
        Y                   = 11000,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x330,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -81100,
        Z                   = -5870,
        Y                   = 13330,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x330,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88220,
        Z                   = -5960,
        Y                   = 9810,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x331,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -30500,
        Y                   = 2000,
        Z                   = 36300,
        Range               = -27500,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0x6464,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -14300,
        Y                   = 2000,
        Z                   = 34900,
        Range               = -11500,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0x58AC,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -23460,
        Y                   = 2000,
        Z                   = 55770,
        Range               = -34700,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0xC760,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -38000,
        Y                   = 2000,
        Z                   = 33000,
        Range               = -40000,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0x55F0,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = -21830,
        TriggerZ            = -2000,
        TriggerY            = 37790,
        TriggerRange        = 1500,
        ActorX              = -21830,
        ActorZ              = -800,
        ActorY              = 37790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18840,
        TriggerZ            = -2000,
        TriggerY            = 33860,
        TriggerRange        = 1500,
        ActorX              = -18840,
        ActorZ              = -500,
        ActorY              = 33860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -114230,
        TriggerZ            = -6050,
        TriggerY            = 11770,
        TriggerRange        = 1000,
        ActorX              = -114730,
        ActorZ              = -6040,
        ActorY              = 12270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -77980,
        TriggerZ            = -6870,
        TriggerY            = -11780,
        TriggerRange        = 1000,
        ActorX              = -77540,
        ActorZ              = -6730,
        ActorY              = -11140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_392",          # 00, 0
        "Function_1_3B5",          # 01, 1
        "Function_2_477",          # 02, 2
        "Function_3_7C8",          # 03, 3
        "Function_4_1172",         # 04, 4
        "Function_5_128A",         # 05, 5
        "Function_6_13B4",         # 06, 6
        "Function_7_182B",         # 07, 7
        "Function_8_1875",         # 08, 8
        "Function_9_18DF",         # 09, 9
        "Function_10_1A30",        # 0A, 10
    )


    def Function_0_392(): pass

    label("Function_0_392")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_39E"),
        (SWITCH_DEFAULT, "loc_3B4"),
    )


    label("loc_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B1")
    OP_A2(0x43D)
    Event(0, 6)

    label("loc_3B1")

    Jump("loc_3B4")

    label("loc_3B4")

    Return()

    # Function_0_392 end

    def Function_1_3B5(): pass

    label("Function_1_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CD")
    OP_B1("R2200_y")
    Jump("loc_3D6")

    label("loc_3CD")

    OP_B1("R2200_n")

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_40D")

    label("loc_3F9")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_41D")
    OP_10(0x1, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_423")

    label("loc_41D")

    OP_10(0x1, 0x1)
    OP_10(0x3, 0x0)

    label("loc_423")

    OP_16(0x2, 0xFA0, 0xFFFD21A0, 0xFFFE5638, 0x30026)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_447")
    OP_6F(0x0, 0)
    Jump("loc_44E")

    label("loc_447")

    OP_6F(0x0, 60)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_460")
    OP_6F(0x1, 0)
    Jump("loc_467")

    label("loc_460")

    OP_6F(0x1, 60)

    label("loc_467")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C8, 0x1, 0x64)
    Return()

    # Function_1_3B5 end

    def Function_2_477(): pass

    label("Function_2_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C7")
    OP_A2(0x40E)
    EventBegin(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4A6():
        OP_6D(-22740, -1990, 38220, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4A6)

    def lambda_4BE():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4BE)

    def lambda_4CE():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4CE)
    WaitChrThread(0x0, 0x2)
    SetChrPos(0x101, -28320, -2000, 32860, 90)
    SetChrPos(0x102, -28920, -2000, 32460, 90)

    def lambda_505():
        OP_8E(0xFE, 0xFFFFA646, 0xFFFFF83A, 0x9448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_505)
    Sleep(800)

    def lambda_525():
        OP_8E(0xFE, 0xFFFFA4F2, 0xFFFFF830, 0x8EC6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_525)
    WaitChrThread(0x101, 0x1)

    def lambda_545():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_545)
    WaitChrThread(0x102, 0x1)

    def lambda_558():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_558)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05North: Mercia Orphanage\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #1
        0x101,
        "#002F#3P...\x02",
    )

    CloseMessageWindow()

    def lambda_5B4():
        OP_6D(-23610, -2000, 39450, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5B4)
    OP_8C(0x102, 315, 400)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #2
        0x102,
        "#010FLooks like it's up ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#007F#3PYeah...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_632():
        OP_6D(-22740, -1990, 38220, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_632)
    TurnDirection(0x102, 0x101, 400)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #4
        0x102,
        "#014FWhat's wrong, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#006F#3P...Okay, that settles it!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #6
        0x101,
        (
            "#005F#3PThe situation has nothing to do\x01",
            "with it! It's not okay to take\x01",
            "things from people!\x02\x03",

            "When we find him, we need\x01",
            "to punish him!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x102,
        (
            "#019FHa ha. Leave it to you to get all\x01",
            "worked up over it.\x02\x03",

            "#010FBut for right now you need\x01",
            "to just settle down, okay?\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_7C7")

    Return()

    # Function_2_477 end

    def Function_3_7C8(): pass

    label("Function_3_7C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1171")
    OP_A2(0x411)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x136, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -22174, -700, 54574, 0)

    NpcTalk(    #8
        0x8,
        "Boy's Voice",
        "...Miss Kloe?\x02",
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(-25380, -2050, 57450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -25380, -2000, 57447, 225)
    SetChrPos(0x136, -26370, -2000, 58130, 180)
    SetChrPos(0x102, -27810, -2000, 57580, 135)
    OP_0D()
    OP_8E(0x8, 0xFFFF9F2A, 0xFFFFFD44, 0xCC6A, 0x1B58, 0x0)
    OP_8C(0x8, 270, 0)
    OP_96(0x8, 0xFFFF9BCE, 0xFFFFF7F4, 0xD340, 0x3E8, 0x1B58)
    OP_8E(0x8, 0xFFFF96EC, 0xFFFFF830, 0xD49E, 0x1B58, 0x0)
    OP_8C(0x8, 0, 600)
    ClearChrFlags(0x8, 0x4)

    ChrTalk(    #9
        0x136,
        "#044FClem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#004FOh, it's that brat!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x136, 0x2)

    ChrTalk(    #11
        0x136,
        (
            "#042FYou know you shouldn't be\x01",
            "playing around here.\x02\x03",

            "What would you do if a monster\x01",
            "attacked you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#775FI just had to come apologize\x01",
            "to you...\x02\x03",

            "I'm sorry for lying about the\x01",
            "emblem thingy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x136,
        (
            "#041FHa ha...well, don't worry.\x01",
            "I'm not mad at you.\x02\x03",

            "#041FBut isn't there someone else\x01",
            "you should be apologizing to?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #14
        0x8,
        (
            "#774FAck...\x02\x03",

            "N-No, there isn't!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#000F???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x136,
        (
            "#048FI know you're a good boy.\x02\x03",

            "So...why don't you go and\x01",
            "apologize?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#773F...\x02\x03",

            "Well, if you want me to,\x01",
            "I guess I gotta.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B81():

        label("loc_B81")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_B81")

    QueueWorkItem2(0x101, 1, lambda_B81)

    def lambda_B92():

        label("loc_B92")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_B92")

    QueueWorkItem2(0x136, 1, lambda_B92)

    def lambda_BA3():

        label("loc_BA3")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_BA3")

    QueueWorkItem2(0x102, 1, lambda_BA3)
    OP_8E(0x8, 0xFFFF9CA5, 0xFFFFF830, 0xDC3C, 0xBB8, 0x0)
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(    #18
        0x8,
        (
            "#773FUm...Miss Bracer-lady?\x02\x03",

            "I'm... I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#008FOh, uh...ha ha ha... You're\x01",
            "apologizing to me?\x02\x03",

            "#001FSo there IS justice in this world!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x8, 0xFFFF9D54, 0xFFFFF7CC, 0xD9F8, 0xBB8, 0x0)

    ChrTalk(    #20
        0x8,
        (
            "#774FH-Hey, don't get me wrong!\x02\x03",

            "I just wanted to apologize to\x01",
            "Miss Kloe!\x02\x03",

            "#772FAren't bracers supposed to pay\x01",
            "attention to what's going on?\x02\x03",

            "If a little kid like me can grab\x01",
            "something off you so easily,\x01",
            "what's your excuse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#009FGah...!\x02",
    )

    CloseMessageWindow()
    OP_95(0x8, 0x0, 0x0, 0x0, 0x320, 0x1770)

    ChrTalk(    #22
        0x8,
        (
            "#770FBye-bye! Make sure you hone that\x01",
            "training of yours, before you lose\x01",
            "something even MORE valuable!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFA1D0, 0xFFFFF830, 0xE006, 0x1770, 0x0)
    OP_8E(0x8, 0xFFFFA010, 0xFFFFF830, 0x12494, 0x1B58, 0x0)
    SetChrFlags(0x8, 0x80)

    ChrTalk(    #23
        0x101,
        "#009F#4PWhat a little...BRAT!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x136, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #24
        0x102,
        (
            "#010FSettle down. He was just trying\x01",
            "to hide his own embarrassment.\x02\x03",

            "Not to mention, you really aren't\x01",
            "the most attentive person in the\x01",
            "world.\x02\x03",

            "Maybe you should heed his advice...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #25
        0x101,
        (
            "#007F#4PGrrrr... You're an even bigger\x01",
            "brat!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x136, 180, 400)

    ChrTalk(    #26
        0x136,
        (
            "#041F*giggle*\x02\x03",

            "You two must be really close.\x02\x03",

            "I mean, you act like brother\x01",
            "and sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#008F#4PEr, we do...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#019FOnly insofar as we try to look\x01",
            "out for each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#009F#4POh, that's a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x136,
        (
            "#040FHa ha. I'm honestly a little envious.\x01",
            "I was an only child.\x02\x03",

            "#049FI wish I knew what that kind of\x01",
            "relationship feels like...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#000F#4PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x136,
        (
            "#045FOh, it's nothing...\x02\x03",

            "#040FAnyway, shouldn't we be\x01",
            "heading out?\x02\x03",

            "We can get to Ruan just by\x01",
            "following the beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#006F#4POkay. Let's get going, then.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_1171")

    Return()

    # Function_3_7C8 end

    def Function_4_1172(): pass

    label("Function_4_1172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1289")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EB")

    ChrTalk(    #34
        0x102,
        (
            "#010FThat's the way to Ruan.\x02\x03",

            "If we want to go to the orphanage,\x01",
            "we need to go the other way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126E")

    ChrTalk(    #35
        0x101,
        (
            "#000FOh... Isn't the orphanage this\x01",
            "way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#010FNo...this is the way to Ruan.\x02\x03",

            "We need to take the other road.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126E")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1289")

    Return()

    # Function_4_1172 end

    def Function_5_128A(): pass

    label("Function_5_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131E")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #37
        0x102,
        (
            "#012FManoria's down that way.\x02\x03",

            "If we want to go to the orphanage,\x01",
            "we need to go back to the fork in\x01",
            "the road.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1398")

    ChrTalk(    #38
        0x102,
        (
            "#012F(Manoria's down this way...)\x02\x03",

            "(We need to go back to the fork in\x01",
            "the road to get to the orphanage.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1398")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_13B3")

    Return()

    # Function_5_128A end

    def Function_6_13B4(): pass

    label("Function_6_13B4")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-114260, -2000, 16980, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    SetChrPos(0x101, -113570, -2029, 17310, 270)
    SetChrPos(0x105, -114690, -1960, 16400, 0)
    SetChrPos(0x102, -115110, -2020, 17800, 135)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #39
        0x101,
        (
            "#582FDalmore was behind everything...\x02\x03",

            "#005FHe was just pretending to be all kind\x01",
            "and everything from the start!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x105,
        (
            "#043FUm... I've been kind of wondering\x01",
            "about this...\x02\x03",

            "...but will we be able to catch\x01",
            "the mayor this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#004F...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#013FShe raises a good question... \x01",
            "This may be difficult.\x02\x03",

            "The Bracer Guild has a non-interference\x01",
            "policy when it comes to government\x01",
            "affairs.\x02\x03",

            "And considering he has control over the whole\x01",
            "Ruan region, arresting the mayor isn't going\x01",
            "to be easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#580FHold on just a second! Doesn't\x01",
            "anyone else find that strange?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#015FIt is funny, but the law is the law.\x02\x03",

            "That's why the guild can have\x01",
            "branches anywhere, even in the\x01",
            "Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#003FYeah, but still...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#012FAnyway, let's just get to the\x01",
            "guild and talk to Jean.\x02\x03",

            "I think he'll have some useful\x01",
            "advice for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#002FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        "#049F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#006FI'm fine! Don't worry about me.\x02\x03",

            "We just need to make the man\x01",
            "in charge pay his tab!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x105,
        "#542FYes...that's right.\x02",
    )

    CloseMessageWindow()
    OP_28(0x3E, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_6_13B4 end

    def Function_7_182B(): pass

    label("Function_7_182B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #51
        "\x07\x05North: Mercia Orphanage\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_182B end

    def Function_8_1875(): pass

    label("Function_8_1875")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #52
        (
            "\x07\x05East: Ruan - 238 selge\x01",
            "West: Manoria Village - 74 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1875 end

    def Function_9_18DF(): pass

    label("Function_9_18DF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1955")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x00Found \x07\x02Tear Balm\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4B9)
    Jump("loc_19CB")

    label("loc_1955")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #54
        (
            "\x07\x00Found \x07\x02Tear Balm\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Tear Balm\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_19CB")

    Jump("loc_1A22")

    label("loc_19CE")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #55
        "\x07\x05Fill this chest with your tears because it is empty!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x83)

    label("loc_1A22")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_18DF end

    def Function_10_1A30(): pass

    label("Function_10_1A30")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1AA6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x00Found \x07\x02Tear Balm\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4BA)
    Jump("loc_1B1C")

    label("loc_1AA6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #57
        (
            "\x07\x00Found \x07\x02Tear Balm\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Tear Balm\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_1B1C")

    Jump("loc_1B73")

    label("loc_1B1F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #58
        "\x07\x05Fill this chest with your tears because it is empty!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x84)

    label("loc_1B73")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1A30 end

    SaveToFile()

Try(main)
