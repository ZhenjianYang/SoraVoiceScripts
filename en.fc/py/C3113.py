from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3113   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3113.x',
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
        'Josette',                              # 9
        'Kyle',                                 # 10
        'Don',                                  # 11
        "Soldier's Voice",                      # 12
        "Man's Voice",                          # 13
        'Sky Bandit',                           # 14
        'Sky Bandit',                           # 15
        'Sky Bandit',                           # 16
        'Sky Bandit',                           # 17
        'Sky Bandit',                           # 18
        'Sky Bandit',                           # 19
        'Guardsman',                            # 20
        'Guardsman',                            # 21
        'Guardsman',                            # 22
        'Mayor Dalmore',                        # 23
        'Gilbert',                              # 24
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
        'ED6_DT07/CH02130 ._CH',             # 00
        'ED6_DT07/CH02120 ._CH',             # 01
        'ED6_DT07/CH02110 ._CH',             # 02
        'ED6_DT07/CH01380 ._CH',             # 03
        'ED6_DT07/CH01320 ._CH',             # 04
        'ED6_DT07/CH02410 ._CH',             # 05
        'ED6_DT07/CH02420 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02130P._CP',             # 00
        'ED6_DT07/CH02120P._CP',             # 01
        'ED6_DT07/CH02110P._CP',             # 02
        'ED6_DT07/CH01380P._CP',             # 03
        'ED6_DT07/CH01320P._CP',             # 04
        'ED6_DT07/CH02410P._CP',             # 05
        'ED6_DT07/CH02420P._CP',             # 06
    )

    DeclNpc(
        X                   = -142470,
        Z                   = 0,
        Y                   = -550,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -142390,
        Z                   = 0,
        Y                   = 4030,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -140430,
        Z                   = 0,
        Y                   = 4030,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8770,
        Z                   = 0,
        Y                   = -4840,
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
        X                   = 18140,
        Z                   = 0,
        Y                   = -490,
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
        X                   = -132720,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 171,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -131510,
        Z                   = 0,
        Y                   = 2890,
        Direction           = 167,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -130850,
        Z                   = 0,
        Y                   = 1430,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -124600,
        Z                   = 0,
        Y                   = 2120,
        Direction           = 154,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -123080,
        Z                   = 0,
        Y                   = 2980,
        Direction           = 177,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -123420,
        Z                   = 0,
        Y                   = 950,
        Direction           = 189,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -110610,
        Z                   = 0,
        Y                   = 3930,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -108510,
        Z                   = 0,
        Y                   = 3910,
        Direction           = 179,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -106630,
        Z                   = 0,
        Y                   = 3280,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -119400,
        Z                   = 0,
        Y                   = 4390,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -115010,
        Z                   = 0,
        Y                   = -550,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 20980,
        TriggerZ            = 0,
        TriggerY            = 158210,
        TriggerRange        = 800,
        ActorX              = 20980,
        ActorZ              = 1000,
        ActorY              = 158210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14930,
        TriggerZ            = 0,
        TriggerY            = 1930,
        TriggerRange        = 800,
        ActorX              = -14930,
        ActorZ              = 1000,
        ActorY              = 1930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2910,
        TriggerZ            = 0,
        TriggerY            = 1930,
        TriggerRange        = 800,
        ActorX              = -2910,
        ActorZ              = 1000,
        ActorY              = 1930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7070,
        TriggerZ            = 0,
        TriggerY            = 1930,
        TriggerRange        = 800,
        ActorX              = 7070,
        ActorZ              = 1000,
        ActorY              = 1930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23900,
        TriggerZ            = 0,
        TriggerY            = 114940,
        TriggerRange        = 800,
        ActorX              = 23900,
        ActorZ              = 1000,
        ActorY              = 114940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23900,
        TriggerZ            = 0,
        TriggerY            = 126940,
        TriggerRange        = 800,
        ActorX              = 23900,
        ActorZ              = 1000,
        ActorY              = 126940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23900,
        TriggerZ            = 0,
        TriggerY            = 138940,
        TriggerRange        = 800,
        ActorX              = 23900,
        ActorZ              = 1000,
        ActorY              = 138940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3DE",          # 00, 0
        "Function_1_41B",          # 01, 1
        "Function_2_454",          # 02, 2
        "Function_3_46A",          # 03, 3
        "Function_4_1226",         # 04, 4
        "Function_5_126A",         # 05, 5
        "Function_6_129A",         # 06, 6
        "Function_7_12CA",         # 07, 7
        "Function_8_12FA",         # 08, 8
        "Function_9_132A",         # 09, 9
        "Function_10_1371",        # 0A, 10
        "Function_11_13C7",        # 0B, 11
        "Function_12_1409",        # 0C, 12
        "Function_13_1455",        # 0D, 13
        "Function_14_1492",        # 0E, 14
        "Function_15_165C",        # 0F, 15
        "Function_16_1C0D",        # 10, 16
        "Function_17_1D0C",        # 11, 17
        "Function_18_1DF8",        # 12, 18
        "Function_19_1F38",        # 13, 19
    )


    def Function_0_3DE(): pass

    label("Function_0_3DE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_3EE"),
        (104, "loc_404"),
        (SWITCH_DEFAULT, "loc_41A"),
    )


    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_401")
    OP_A2(0x56C)
    Event(0, 3)

    label("loc_401")

    Jump("loc_41A")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_417")
    OP_A2(0x56E)
    Event(0, 16)

    label("loc_417")

    Jump("loc_41A")

    label("loc_41A")

    Return()

    # Function_0_3DE end

    def Function_1_41B(): pass

    label("Function_1_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 4)), scpexpr(EXPR_END)), "loc_427")
    OP_1B(0x1, 0x0, 0xE)

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 4)), scpexpr(EXPR_END)), "loc_433")
    OP_1B(0x0, 0x0, 0xF)

    label("loc_433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_443")
    OP_72(0x12, 0x10)
    Jump("loc_447")

    label("loc_443")

    OP_64(0x0, 0x1)

    label("loc_447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_END)), "loc_453")
    OP_22(0xAC, 0x1, 0x50)

    label("loc_453")

    Return()

    # Function_1_41B end

    def Function_2_454(): pass

    label("Function_2_454")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_469")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_454")

    label("loc_469")

    Return()

    # Function_2_454 end

    def Function_3_46A(): pass

    label("Function_3_46A")

    EventBegin(0x0)
    OP_24(0xAC, 0x3C)
    OP_6D(-98070, 0, 2550, 0)
    OP_67(0, 8870, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -150200, 3000, 3950, 90)
    SetChrPos(0x102, -150200, 3000, 3950, 90)
    SetChrPos(0x106, -150200, 3000, 3950, 90)
    SetChrPos(0x107, -150200, 3000, 3950, 90)
    SetChrPos(0x10B, -150200, 3000, 3950, 90)
    FadeToBright(2000, 0)

    def lambda_511():
        OP_6D(-142510, 0, 2940, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_511)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(-142510, 0, 2940, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x8,
        (
            "#215F#1PH-Hey... Don't you think\x01",
            "it's awfully noisy outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#200FSounds to me like someone's\x01",
            "breaking in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xA,
        (
            "#192FSay what?\x01",
            "Who's breaking in?\x02\x03",

            "#196FNobody's allowed to break in \x01",
            "'til we break out! NOBODY!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "#203FEasy, bro. You know your\x01",
            "simple little escape plan\x01",
            "won't ever--\x02",
        )
    )

    CloseMessageWindow()

    def lambda_696():
        OP_6D(-146150, 0, -10, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_696)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(600)
    OP_43(0x102, 0x1, 0x0, 0x5)
    Sleep(600)
    OP_43(0x107, 0x1, 0x0, 0x6)
    Sleep(600)
    OP_43(0x10B, 0x1, 0x0, 0x8)
    Sleep(600)
    OP_43(0x106, 0x1, 0x0, 0x7)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #4
        0x102,
        "#012FThis looks like the dungeon...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #5
        0x101,
        (
            "#501F#5PWow. It's a lot bigger than the\x01",
            "dungeon at the Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_760():
        OP_6D(-142480, 0, -140, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_760)

    def lambda_778():
        OP_6C(13000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_778)

    def lambda_788():
        OP_6B(3170, 2000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_788)

    def lambda_798():

        label("loc_798")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_798")

    QueueWorkItem2(0x107, 1, lambda_798)

    def lambda_7A9():

        label("loc_7A9")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_7A9")

    QueueWorkItem2(0x102, 1, lambda_7A9)

    def lambda_7BA():

        label("loc_7BA")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_7BA")

    QueueWorkItem2(0x10B, 1, lambda_7BA)

    def lambda_7CB():

        label("loc_7CB")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_7CB")

    QueueWorkItem2(0x106, 1, lambda_7CB)

    def lambda_7DC():
        OP_8E(0xFE, 0xFFFDD2B2, 0x0, 0xFFFFF5D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7DC)
    Sleep(100)

    def lambda_7FC():
        OP_8E(0xFE, 0xFFFDD636, 0x0, 0xFFFFF240, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_7FC)
    Sleep(300)

    def lambda_81C():
        OP_8E(0xFE, 0xFFFDD3FC, 0x0, 0xFFFFEFD4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_81C)

    def lambda_837():
        OP_8E(0xFE, 0xFFFDCE52, 0x0, 0xFFFFEE80, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_837)
    Sleep(200)

    def lambda_857():
        OP_8E(0xFE, 0xFFFDCE2A, 0x0, 0xFFFFF25E, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_857)
    WaitChrThread(0x101, 0x2)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #6
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "#213F#6PWha--?\x02",
    )

    CloseMessageWindow()

    def lambda_8BB():

        label("loc_8BB")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_8BB")

    QueueWorkItem2(0x101, 1, lambda_8BB)

    def lambda_8CC():

        label("loc_8CC")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_8CC")

    QueueWorkItem2(0x107, 1, lambda_8CC)

    def lambda_8DD():

        label("loc_8DD")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_8DD")

    QueueWorkItem2(0x102, 1, lambda_8DD)

    def lambda_8EE():

        label("loc_8EE")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_8EE")

    QueueWorkItem2(0x10B, 1, lambda_8EE)

    def lambda_8FF():

        label("loc_8FF")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_8FF")

    QueueWorkItem2(0x106, 1, lambda_8FF)

    ChrTalk(    #8
        0x101,
        "#501FI...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0x8)

    ChrTalk(    #9
        0x101,
        "#005F#1K#3SYOU?!\x02",
    )


    ChrTalk(    #10
        0x8,
        "#214F#1K#3S#6PYOU?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    OP_56(0x1)
    OP_59()
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0xFFFDD802, 0x0, 0x3F2, 0x1770, 0x0)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #11
        0x9,
        "#201FYou guys are--?!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x4)
    OP_8E(0xA, 0xFFFDDC80, 0x0, 0xFFFFFDEE, 0x1388, 0x0)
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #12
        0xA,
        "#192FYou're those punks from before!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#014FWell, then... Umm...\x01",
            "Long time no see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#002FOh, okay... You guys\x01",
            "are being held here.\x02\x03",

            "#003F...\x02\x03",

            "#506FUmm...err...\x01",
            "How have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#214F#6PHey! We don't need your\x01",
            "damn pity!\x02\x03",

            "The only thing you're good\x01",
            "for is handling a pole,\x01",
            "air-for-brains!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#007FGeez... I was just trying\x01",
            "to be polite.\x02\x03",

            "If it'll make you feel better,\x01",
            "insult me all you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#216F#6PWh...WHAT?!\x01",
            "Don't try to play it cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x106,
        (
            "#052FUh... I'm assuming you\x01",
            "know these folks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#010FThey're the Capua sky bandits.\x01",
            "They hijacked that airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10B,
        (
            "#103FAhh, I've heard stories\x01",
            "about them.\x02\x03",

            "They use a very high-powered\x01",
            "airship, don't they?\x02\x03",

            "#101FI've heard it's of Imperial make,\x01",
            "but I'm curious about the specs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "#202FY-Yeah... It's got a top speed\x01",
            "of 2300 selge per hour.\x02\x03",

            "#201FEr, I mean, why should I have\x01",
            "to answer your questions?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10B,
        "#102FMy. Aren't WE petty?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x107,
        (
            "#067FGr-grandpa...\x02\x03",

            "I don't think this is the\x01",
            "right time for asking about\x01",
            "that kind of stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xA,
        (
            "#190FNow wait just one damn minute.\x02\x03",

            "Why are you bracers here\x01",
            "in the first place?\x02\x03",

            "Are you the cause of that\x01",
            "siren?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#509F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#015F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10B,
        "#100F...Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x107,
        "#562F...Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x106,
        "#053F...Well, sorry we intruded.\x02",
    )

    CloseMessageWindow()

    def lambda_EC7():
        OP_6D(-143280, 0, 2210, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EC7)

    def lambda_EDF():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_EDF)
    OP_43(0x106, 0x1, 0x0, 0xD)
    OP_43(0x10B, 0x1, 0x0, 0xB)
    OP_43(0x102, 0x1, 0x0, 0xA)
    OP_43(0x107, 0x1, 0x0, 0xC)
    OP_43(0x101, 0x1, 0x0, 0x9)
    Sleep(2000)

    ChrTalk(    #30
        0x8,
        "#214FNo fair!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        "#201FYou're the intruders, right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        "#196FHey! Let us out of here!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0xAC, 0x46)
    OP_6D(-24930, 0, 38220, 0)
    OP_6B(3000, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10B, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    SetChrPos(0x101, -25930, 0, 36130, 0)
    SetChrPos(0x102, -24890, 0, 36720, 315)
    SetChrPos(0x10B, -26310, 0, 37690, 135)
    SetChrPos(0x107, -25050, 0, 38100, 225)
    SetChrPos(0x106, -25740, 0, 38770, 180)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0x106, 0)
    SetChrSubChip(0x10B, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #33
        0x101,
        (
            "#007F*sigh*...\x01",
            "That was a surprise.\x02\x03",

            "#003FCome to think of it... Those\x01",
            "guys have some connection\x01",
            "to the men in black, right?\x02\x03",

            "But they got arrested by Colonel\x01",
            "Richard, which means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#013F#4PMaybe the colonel's trumping it\x01",
            "up as one of his accomplishments.\x02\x03",

            "And maybe Mayor Dalmore was\x01",
            "used in a similar fashion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x106,
        (
            "#551FHmph. And yet, I somehow just\x01",
            "can't seem to muster up any\x01",
            "sympathy for him.\x02\x03",

            "#057FWe're wasting time here. We've\x01",
            "got to find another escape route.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x44, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_3_46A end

    def Function_4_1226(): pass

    label("Function_4_1226")

    OP_8E(0xFE, 0xFFFDC3B2, 0x3E8, 0xF6E, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFDC498, 0x0, 0xFFFFF542, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFDC948, 0x0, 0xFFFFF542, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_4_1226 end

    def Function_5_126A(): pass

    label("Function_5_126A")

    OP_8E(0xFE, 0xFFFDC3B2, 0x3E8, 0xF6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC524, 0x0, 0xFFFFF196, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_126A end

    def Function_6_129A(): pass

    label("Function_6_129A")

    OP_8E(0xFE, 0xFFFDC3B2, 0x3E8, 0xF6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC560, 0x0, 0xFFFFF560, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_129A end

    def Function_7_12CA(): pass

    label("Function_7_12CA")

    OP_8E(0xFE, 0xFFFDC3B2, 0x3E8, 0xF6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC0D8, 0x0, 0xFFFFF736, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_7_12CA end

    def Function_8_12FA(): pass

    label("Function_8_12FA")

    OP_8E(0xFE, 0xFFFDC3B2, 0x3E8, 0xF6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC088, 0x0, 0xFFFFF2F4, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_8_12FA end

    def Function_9_132A(): pass

    label("Function_9_132A")

    Sleep(500)
    Sleep(500)
    OP_8E(0xFE, 0xFFFDC3EE, 0x0, 0xFFFFF3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC1BE, 0x3E8, 0xEB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDB548, 0xBB8, 0xF6E, 0xBB8, 0x0)
    Return()

    # Function_9_132A end

    def Function_10_1371(): pass

    label("Function_10_1371")

    Sleep(500)
    Sleep(500)
    Sleep(500)
    Sleep(500)
    Sleep(300)
    OP_8E(0xFE, 0xFFFDC3EE, 0x0, 0xFFFFF3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC1BE, 0x3E8, 0xEB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDB548, 0xBB8, 0xF6E, 0xBB8, 0x0)
    Return()

    # Function_10_1371 end

    def Function_11_13C7(): pass

    label("Function_11_13C7")

    Sleep(500)
    OP_8E(0xFE, 0xFFFDC3EE, 0x0, 0xFFFFF3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC1BE, 0x3E8, 0xEB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDB548, 0xBB8, 0xF6E, 0xBB8, 0x0)
    Return()

    # Function_11_13C7 end

    def Function_12_1409(): pass

    label("Function_12_1409")

    Sleep(500)
    Sleep(500)
    Sleep(500)
    OP_8E(0xFE, 0xFFFDC3EE, 0x0, 0xFFFFF3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC1BE, 0x3E8, 0xEB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDB548, 0xBB8, 0xF6E, 0xBB8, 0x0)
    Return()

    # Function_12_1409 end

    def Function_13_1455(): pass

    label("Function_13_1455")

    OP_8E(0xFE, 0xFFFDC3EE, 0x0, 0xFFFFF3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC1BE, 0x3E8, 0xEB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDB548, 0xBB8, 0xF6E, 0xBB8, 0x0)
    Return()

    # Function_13_1455 end

    def Function_14_1492(): pass

    label("Function_14_1492")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 5)), scpexpr(EXPR_END)), "loc_153F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14EF")

    ChrTalk(    #36
        0x106,
        (
            "#054FIt's a dead end! We need to\x01",
            "find the source of that voice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153C")

    label("loc_14EF")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #37
        0x106,
        (
            "#054FIt's a dead end! We've gotta\x01",
            "find the source of that voice!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153C")

    Jump("loc_1640")

    label("loc_153F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C5")

    ChrTalk(    #38
        0x106,
        (
            "#050FAt any rate, the dungeon's\x01",
            "a dead end.\x02\x03",

            "With those guys hounding us,\x01",
            "we really need to find another\x01",
            "way out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1640")

    label("loc_15C5")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #39
        0x106,
        (
            "#050FHey, the dungeon's a dead end.\x02\x03",

            "Hurry! With those guys hounding us,\x01",
            "we've gotta look for another way out!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1640")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_14_1492 end

    def Function_15_165C(): pass

    label("Function_15_165C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A91")
    EventBegin(0x0)
    OP_A2(0x56D)
    OP_28(0x44, 0x1, 0x400)

    ChrTalk(    #40
        0xB,
        "#2PHey, did you find them?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    TurnDirection(0x2, 0xB, 0)
    TurnDirection(0x3, 0xB, 0)
    TurnDirection(0x4, 0xB, 0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0xB,
        (
            "#2PNo, and I've searched the\x01",
            "barracks top-to-bottom!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xB,
        "#2PSame goes for the watchtower!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        "#2P...All that leaves is headquarters.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xB,
        (
            "#2PWhile we're there, we can report to\x01",
            "the major that we've gone over the\x01",
            "place with a fine-toothed comb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#005F#6PUh-oh! I think they're\x01",
            "coming this way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x106,
        (
            "#057FShit...and this is\x01",
            "a blind alley, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#012F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xC,
        "Come on! This way!\x02",
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x0, 0xC, 0)
    TurnDirection(0x1, 0xC, 0)
    TurnDirection(0x2, 0xC, 0)
    TurnDirection(0x3, 0xC, 0)
    TurnDirection(0x4, 0xC, 0)

    ChrTalk(    #49
        0x101,
        "#004F#6PHey, did you hear something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x107,
        (
            "#065FY-Yeah... I think it said,\x01",
            "'This way.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xC,
        (
            "...There's no time! You don't\x01",
            "want to be caught, do you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10B,
        "#102FI don't think I misheard that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x106,
        (
            "#054FWe don't have a choice!\x01",
            "We might as well give\x01",
            "it a shot!\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1C0C")

    label("loc_1A91")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE4")

    ChrTalk(    #54
        0x101,
        (
            "#005FThe soldiers are coming! We've\x01",
            "gotta follow that voice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF1")

    label("loc_1AE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B47")

    ChrTalk(    #55
        0x102,
        (
            "#012FThe footsteps are getting\x01",
            "closer... We'll just have\x01",
            "to follow that voice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF1")

    label("loc_1B47")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B98")

    ChrTalk(    #56
        0x106,
        (
            "#057FWe can't go this way... Let's\x01",
            "try following that voice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF1")

    label("loc_1B98")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BF1")

    ChrTalk(    #57
        0x107,
        (
            "#065FThose soldiers are coming\x01",
            "this way... We have to\x01",
            "follow the voice!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF1")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1C0C")

    Return()

    # Function_15_165C end

    def Function_16_1C0D(): pass

    label("Function_16_1C0D")

    EventBegin(0x0)
    OP_6D(21440, 0, 108290, 0)
    SetChrPos(0xC, 20330, 0, 120850, 0)
    SetChrPos(0x101, 21240, 0, 106790, 0)
    SetChrPos(0x102, 20030, 0, 106050, 0)
    SetChrPos(0x107, 21530, 0, 105630, 0)
    SetChrPos(0x106, 21050, 0, 104420, 0)
    SetChrPos(0x10B, 20280, 0, 104880, 0)
    OP_0D()

    ChrTalk(    #58
        0xC,
        (
            "Come on...\x01",
            "Just down the corridor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#004FHey, Joshua... Do you\x01",
            "recognize that voice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        "#012FYes...it sounds familiar.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_16_1C0D end

    def Function_17_1D0C(): pass

    label("Function_17_1D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DF7")
    OP_A2(0x56F)
    SetChrPos(0xC, 21160, 0, 159230, 0)
    OP_1C(0x12, 0x0, 0xFFFF)
    EventBegin(0x0)
    OP_6D(21080, 0, 158340, 1000)

    ChrTalk(    #61
        0xC,
        "Quickly, get inside!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x106,
        (
            "#050FHey, now...\x01",
            "This room is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10B,
        (
            "#100FHmph... Well, I don't know what\x01",
            "he's intending, but we don't have\x01",
            "any other choice but to keep going.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    OP_71(0x12, 0x10)

    label("loc_1DF7")

    Return()

    # Function_17_1D0C end

    def Function_18_1DF8(): pass

    label("Function_18_1DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 6)), scpexpr(EXPR_END)), "loc_1EE9")
    OP_A2(0x56F)
    SetChrPos(0xC, 21160, 0, 159230, 0)
    OP_1C(0x12, 0x0, 0xFFFF)
    EventBegin(0x0)
    OP_6D(21080, 0, 158340, 1000)

    ChrTalk(    #64
        0xC,
        "Quickly, get inside!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x106,
        (
            "#052FHey, now...\x01",
            "This room is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10B,
        (
            "#102FHmph... Well, I don't know what\x01",
            "he's intending, but we don't have\x01",
            "any other choice but to keep going.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    OP_71(0x12, 0x10)
    OP_64(0x0, 0x1)
    Jump("loc_1F37")

    label("loc_1EE9")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #67
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_1F37")

    Return()

    # Function_18_1DF8 end

    def Function_19_1F38(): pass

    label("Function_19_1F38")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #68
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_1F38 end

    SaveToFile()

Try(main)
