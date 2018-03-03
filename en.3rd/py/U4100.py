from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4100   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'Roaming Monster',                      # 9
        'Roaming Monster',                      # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH14500 ._CH',             # 00
        'ED6_DT29/CH14501 ._CH',             # 01
        'ED6_DT29/CH14510 ._CH',             # 02
        'ED6_DT29/CH14511 ._CH',             # 03
        'ED6_DT29/CH14520 ._CH',             # 04
        'ED6_DT29/CH14521 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14500P._CP',             # 00
        'ED6_DT29/CH14501P._CP',             # 01
        'ED6_DT29/CH14510P._CP',             # 02
        'ED6_DT29/CH14511P._CP',             # 03
        'ED6_DT29/CH14520P._CP',             # 04
        'ED6_DT29/CH14521P._CP',             # 05
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


    DeclMonster(
        X                   = -140,
        Z                   = 0,
        Y                   = -21440,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xC8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 140,
        Z                   = 0,
        Y                   = -5820,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xC8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -140,
        Z                   = 0,
        Y                   = -21440,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 140,
        Z                   = 0,
        Y                   = -5820,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 8880,
        TriggerZ            = 0,
        TriggerY            = -43040,
        TriggerRange        = 1000,
        ActorX              = 8880,
        ActorZ              = 2000,
        ActorY              = -43040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1AE",          # 00, 0
        "Function_1_224",          # 01, 1
        "Function_2_2DF",          # 02, 2
        "Function_3_144D",         # 03, 3
        "Function_4_14E6",         # 04, 4
        "Function_5_155C",         # 05, 5
        "Function_6_1598",         # 06, 6
        "Function_7_16A8",         # 07, 7
        "Function_8_17AC",         # 08, 8
        "Function_9_1A2E",         # 09, 9
        "Function_10_1B19",        # 0A, 10
        "Function_11_1BD5",        # 0B, 11
        "Function_12_1CEB",        # 0C, 12
        "Function_13_1D39",        # 0D, 13
        "Function_14_1D51",        # 0E, 14
    )


    def Function_0_1AE(): pass

    label("Function_0_1AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (115, "loc_1E0"),
        (116, "loc_1E7"),
        (SWITCH_DEFAULT, "loc_1FA"),
    )


    label("loc_1E0")

    Event(0, 9)
    Jump("loc_1FA")

    label("loc_1E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_1F7")
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_1F7")

    Jump("loc_1FA")

    label("loc_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_210")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 7)
    Jump("loc_223")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_223")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_223")

    Return()

    # Function_0_1AE end

    def Function_1_224(): pass

    label("Function_1_224")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x23005B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A")
    SoundDistance(0x1CB, 0x64, 0x0, 0xFFFF4BD8, 0x7D0, 0x3A98, 0x64, 0x0)

    label("loc_25A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_26D")
    OP_B1("U4100_y")
    Jump("loc_276")

    label("loc_26D")

    OP_B1("U4100_n")

    label("loc_276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_28A")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_294")

    label("loc_28A")

    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2")
    OP_10(0xA, 0x0)
    Jump("loc_2A8")

    label("loc_2A2")

    OP_71(0x41A, 0x0)
    ExitThread()

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6")
    OP_10(0x9, 0x0)
    Jump("loc_2BC")

    label("loc_2B6")

    OP_71(0x41B, 0x0)
    ExitThread()

    label("loc_2BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD")
    OP_1B(0xF, 0x0, 0xA)

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    OP_82(0x8C, 0x0)
    OP_82(0x8D, 0x0)
    OP_82(0x8F, 0x0)

    label("loc_2DE")

    Return()

    # Function_1_224 end

    def Function_2_2DF(): pass

    label("Function_2_2DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 120, 0, -54230, 0)
    SetChrPos(0x10F, 910, 0, -55320, 0)
    SetChrPos(0x107, -910, 0, -55370, 0)
    SetChrPos(0x10E, -20, 0, -56270, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-140, 0, -54880, 0)
    OP_67(0, 9630, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(270000, 0)
    OP_6E(272, 0)
    Sleep(1000)

    def lambda_3A3():
        OP_6D(-600, 0, -54600, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3A3)

    def lambda_3BB():
        OP_67(0, 10270, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3BB)

    def lambda_3D3():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_3D3)

    def lambda_3E3():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_3E3)
    FadeToBright(2000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, 0, -55300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(200)

    def lambda_454():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_454)

    def lambda_466():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_466)

    def lambda_478():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_478)

    def lambda_48A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_48A)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x2)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x109,
        "#1079F#5P...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_542():
        OP_6D(-1480, 500, -47750, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_542)

    def lambda_55A():
        OP_67(0, 5180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_55A)

    def lambda_572():
        OP_6B(3220, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_572)

    def lambda_582():
        OP_6E(323, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_582)

    def lambda_592():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFF3BC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_592)
    Sleep(300)

    def lambda_5B2():
        OP_8E(0xFE, 0x334, 0x0, 0xFFFF383C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_5B2)
    Sleep(300)

    def lambda_5D2():
        OP_8E(0xFE, 0xFFFFFA92, 0x0, 0xFFFF380A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_5D2)
    Sleep(300)

    def lambda_5F2():
        OP_8E(0xFE, 0xFFFFFE34, 0x0, 0xFFFF340E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_5F2)
    OP_6D(78070, -8000, -23700, 1500)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #1
        0x109,
        (
            "#1078F#6PThat's a statue of a white falcon.\x01",
            "Wait... Isn't this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10E,
        "#171F#6PThis is the southern block of Grancel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        "#067F#6PThank goodness! We're finally out of there!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x10F, 180, 400)
    Sleep(500)

    ChrTalk(    #4
        0x10F,
        "#1444F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_747():
        OP_6D(-1370, 0, -49900, 1300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_747)

    def lambda_75F():
        OP_67(0, 5380, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_75F)

    def lambda_777():
        OP_6B(2970, 1300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_777)

    def lambda_787():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_787)
    Sleep(50)

    def lambda_79A():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_79A)
    Sleep(50)

    def lambda_7AD():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_7AD)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #5
        0x109,
        (
            "#1079F#5PWhat's up with you, Ries? You look like you've\x01",
            "seen a ghost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        (
            "#1802F#6PWell, I can't pretend to be all that familiar\x01",
            "with Grancel...\x02\x03",

            "...but that's...not its main gate, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        "#1064F#5PWha...?\x02",
    )

    CloseMessageWindow()
    OP_1D(0xDD)

    def lambda_89A():
        OP_6D(2550, 0, -61010, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_89A)

    def lambda_8B2():
        OP_67(0, 7590, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8B2)

    def lambda_8CA():
        OP_6B(3190, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8CA)

    def lambda_8DA():
        OP_6C(33000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_8DA)

    def lambda_8EA():
        OP_6E(444, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_8EA)

    def lambda_8FA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8FA)
    Sleep(50)

    def lambda_90D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_90D)
    Sleep(50)

    def lambda_920():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_920)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    OP_6D(30, 0, -53360, 0)
    OP_67(0, 8029, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(180000, 0)
    OP_6E(304, 0)

    def lambda_975():
        OP_6D(20, 9090, -58470, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_975)

    def lambda_98D():
        OP_67(0, 6770, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_98D)

    def lambda_9A5():
        OP_6B(2800, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9A5)

    def lambda_9B5():
        OP_6C(180000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_9B5)

    def lambda_9C5():
        OP_6E(262, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_9C5)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #8
        0x109,
        "#1069F#5P#4SCrap!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(1310, 0, -49490, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(304, 0)
    SetChrPos(0x109, 0, 0, -50280, 180)
    SetChrPos(0x10F, 1060, 0, -50870, 180)
    SetChrPos(0x107, -1330, 0, -50890, 180)
    SetChrPos(0x10E, -600, 0, -51780, 180)
    OP_0D()
    Sleep(300)

    ChrTalk(    #9
        0x107,
        "#065F#5PWh-What...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10E,
        "#177F#5PNo, it isn't!\x02",
    )

    CloseMessageWindow()

    def lambda_ACC():
        OP_6D(-1240, 0, -47340, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ACC)

    def lambda_AE4():
        OP_67(0, 5320, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AE4)

    def lambda_AFC():
        OP_6B(2950, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_AFC)

    def lambda_B0C():
        OP_6E(304, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_B0C)
    OP_43(0x10E, 0x0, 0x0, 0x5)

    def lambda_B23():

        label("loc_B23")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_B23")

    QueueWorkItem2(0x109, 0, lambda_B23)

    def lambda_B34():

        label("loc_B34")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_B34")

    QueueWorkItem2(0x10F, 0, lambda_B34)

    def lambda_B45():

        label("loc_B45")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_B45")

    QueueWorkItem2(0x107, 0, lambda_B45)
    WaitChrThread(0x10E, 0x0)
    OP_44(0x109, 0x0)
    OP_44(0x10F, 0x0)
    OP_44(0x107, 0x0)
    WaitChrThread(0x109, 0x1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 4280, 0, -1520, 180)
    SetChrPos(0x11, -3740, 0, -19500, 270)

    def lambda_B98():

        label("loc_B98")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B98")

    QueueWorkItem2(0x10, 1, lambda_B98)

    def lambda_BAB():

        label("loc_BAB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_BAB")

    QueueWorkItem2(0x11, 1, lambda_BAB)
    OP_43(0x10, 0x0, 0x0, 0x3)
    OP_43(0x11, 0x0, 0x0, 0x4)
    Fade(1000)
    OP_23(0x1CB)
    SetChrPos(0x10E, -4380, 0, -48840, 0)
    OP_6D(80, 3150, -50840, 0)
    OP_67(0, 6830, -10000, 0)
    OP_6B(4070, 0)
    OP_6C(0, 0)
    OP_6E(322, 0)

    def lambda_C22():
        OP_6D(80, 4550, -21340, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C22)

    def lambda_C3A():
        OP_67(0, 5560, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C3A)

    def lambda_C52():
        OP_6B(4070, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_C52)

    def lambda_C62():
        OP_6E(338, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_C62)
    Sleep(500)

    def lambda_C77():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_C77)
    Sleep(50)

    def lambda_C8A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_C8A)
    Sleep(100)

    def lambda_C9D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_C9D)
    Sleep(100)
    WaitChrThread(0x109, 0x0)
    Fade(1000)
    OP_6D(38000, 0, -1390, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(101000, 0)
    OP_6E(364, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_6D(-35060, 0, -19650, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(260000, 0)
    OP_6E(364, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_6D(3860, 3150, -3200, 0)
    OP_67(0, 7640, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(45000, 0)
    OP_6E(335, 0)
    OP_0D()
    Sleep(1000)

    def lambda_D8D():
        OP_6B(3500, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_D8D)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x10F, 0x0)
    Sleep(1000)
    OP_AD(0x2400E4, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    SetChrPos(0x109, -3670, 0, -47720, 0)
    SetChrPos(0x10F, -3420, 0, -49110, 0)
    SetChrPos(0x107, -4770, 0, -50200, 0)
    SetChrPos(0x10E, -5390, 0, -48730, 0)
    OP_6D(-3590, 300, -48330, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(45000, 0)
    OP_6E(364, 0)
    Sleep(2000)
    SoundDistance(0x1CB, 0x64, 0x0, 0xFFFF4BD8, 0x7D0, 0x3A98, 0x64, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #11
        0x107,
        "#065F#6PThose soldiers aren't the Royal Army!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10E,
        (
            "#172F#6PWhat has happened here...?\x02\x03",

            "What happened to the capital while\x01",
            "I was away?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1063F#5PMan, I did not see this coming when we\x01",
            "stepped out of that warp.\x02\x03",

            "#1067FEither something happened here while\x01",
            "we were stuck inside that place, or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10F,
        (
            "#1446F...or Phantasma is now able to influence\x01",
            "the world outside.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10E, 90, 400)
    Sleep(300)

    ChrTalk(    #15
        0x10E,
        (
            "#177F#6PNgh... I apologize, but I cannot stand\x01",
            "here any longer!\x02\x03",

            "I need to go check on Grancel Castle!\x02\x03",

            "I am concerned for this city's citizens,\x01",
            "but above all, I fear for the safety of\x01",
            "Her Majesty and the princess!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10F4():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10F4)
    Sleep(100)
    OP_8C(0x10F, 270, 400)
    Sleep(200)

    ChrTalk(    #16
        0x109,
        (
            "#1063F#5PI don't blame you, but we're coming with.\x02\x03",

            "Strong as you are, going alone isn't smart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10E,
        "#172F#6PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#1446F#2PPanicking is the worst thing you can do right\x01",
            "now.\x02\x03",

            "#1443FExtraordinary situations like these are when\x01",
            "caution and careful thinking are your most\x01",
            "valued allies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10E,
        (
            "#175F#6P...\x02\x03",

            "#176FYou're quite right, of course. I understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x109,
        (
            "#1063F#5PThen castle it is. We should try and investigate\x01",
            "the city on our way there, too.\x02\x03",

            "Keep your eyes peeled, though. The fiends here\x01",
            "look like they're not playing around.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)

    ChrTalk(    #21
        0x10F,
        "#1443FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x107,
        "#062F#6PRight!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-4130, 0, -50490, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -4130, 0, -50490, 0)
    SetChrPos(0x1, -4130, 0, -50490, 0)
    SetChrPos(0x2, -4130, 0, -50490, 0)
    SetChrPos(0x3, -4130, 0, -50490, 0)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    OP_A2(0x2702)
    OP_28(0x2B, 0x1, 0x2)
    OP_28(0x2B, 0x1, 0x4)
    OP_28(0x2B, 0x1, 0x8)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_2_2DF end

    def Function_3_144D(): pass

    label("Function_3_144D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14E5")
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xFC8, 0x0, 0x4EC, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0x1CC0, 0x0, 0xFFFFFD4E, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xDAC, 0x0, 0xFFFFED90, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(2000)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xF50, 0x0, 0xFFFFF678, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1500)
    Jump("Function_3_144D")

    label("loc_14E5")

    Return()

    # Function_3_144D end

    def Function_4_14E6(): pass

    label("Function_4_14E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_155B")
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xFFFFF2AE, 0x0, 0xFFFFA862, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xFFFFB24E, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xFFFFF2E0, 0x0, 0xFFFFBBAE, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1500)
    Jump("Function_4_14E6")

    label("loc_155B")

    Return()

    # Function_4_14E6 end

    def Function_5_155C(): pass

    label("Function_5_155C")

    OP_8C(0x10E, 270, 600)
    Sleep(100)
    OP_8E(0xFE, 0xFFFFF52E, 0x0, 0xFFFF3508, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFEAFC, 0x0, 0xFFFF4138, 0x1388, 0x0)
    OP_8C(0x10E, 0, 600)
    Return()

    # Function_5_155C end

    def Function_6_1598(): pass

    label("Function_6_1598")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(12710, 2900, 1350, 0)
    OP_67(0, 9260, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(45000, 0)
    OP_6E(352, 0)

    def lambda_15FB():
        OP_6D(33810, 2900, -1050, 5500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_15FB)

    def lambda_1613():
        OP_67(0, 5570, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1613)

    def lambda_162B():
        OP_6B(2450, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_162B)

    def lambda_163B():
        OP_6C(90000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_163B)

    def lambda_164B():
        OP_6E(352, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_164B)
    FadeToBright(2000, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)

    def lambda_1673():
        OP_6B(2250, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1673)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_0D()
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4200   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_6_1598 end

    def Function_7_16A8(): pass

    label("Function_7_16A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_72(0x41B, 0x0)
    ExitThread()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-3000, 6050, -19740, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(270000, 0)
    OP_6E(352, 0)

    def lambda_1711():
        OP_6D(-35770, -500, -19740, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1711)

    def lambda_1729():
        OP_67(0, 7410, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1729)

    def lambda_1741():
        OP_6B(3040, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1741)

    def lambda_1751():
        OP_6E(322, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1751)
    FadeToBright(2000, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(1000)

    def lambda_1779():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1779)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2508)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_16A8 end

    def Function_8_17AC(): pass

    label("Function_8_17AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187B")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x8C, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(768)
    Sleep(500)
    Jump("loc_187E")

    label("loc_187B")

    TalkBegin(0xFF)

    label("loc_187E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #23
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19FD")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1916"),
        (1, "loc_1991"),
        (2, "loc_19BF"),
        (SWITCH_DEFAULT, "loc_19ED"),
    )


    label("loc_1916")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19FA")

    label("loc_1991")

    OP_A9(0x16)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #24
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_19FA")

    label("loc_19BF")

    OP_A9(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #25
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_19FA")

    label("loc_19ED")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19FA")

    label("loc_19FA")

    Jump("loc_18BA")

    label("loc_19FD")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A2A")
    OP_A2(0x2586)
    EventEnd(0x1)
    Jump("loc_1A2D")

    label("loc_1A2A")

    TalkEnd(0xFF)

    label("loc_1A2D")

    Return()

    # Function_8_17AC end

    def Function_9_1A2E(): pass

    label("Function_9_1A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3B")
    Call(0, 2)
    Return()

    label("loc_1A3B")

    OP_DE(0x0, 0xF, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 120, 0, -54230, 0)
    SetChrPos(0x1, 910, 0, -55320, 0)
    SetChrPos(0x2, -910, 0, -55370, 0)
    SetChrPos(0x3, -20, 0, -56270, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, 0, -55300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 11)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_9_1A2E end

    def Function_10_1B19(): pass

    label("Function_10_1B19")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 120, 0, -54230, 180)
    SetChrPos(0x2, 910, 0, -55320, 180)
    SetChrPos(0x1, -910, 0, -55370, 180)
    SetChrPos(0x0, -20, 0, -56270, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, 0, -55300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 12)
    NewScene("ED6_DT21/M7005   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1B19 end

    def Function_11_1BD5(): pass

    label("Function_11_1BD5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BFE")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1BF2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1BF2)

    label("loc_1BFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C27")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C1B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1C1B)

    label("loc_1C27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C50")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C44():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1C44)

    label("loc_1C50")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C79")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C6D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1C6D)

    label("loc_1C79")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA5")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1CA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CBC")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1CBC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CD3")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1CD3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CEA")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1CEA")

    Return()

    # Function_11_1BD5 end

    def Function_12_1CEB(): pass

    label("Function_12_1CEB")


    def lambda_1CF1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1CF1)

    def lambda_1D03():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1D03)

    def lambda_1D15():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1D15)

    def lambda_1D27():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1D27)
    Sleep(1000)
    Return()

    # Function_12_1CEB end

    def Function_13_1D39(): pass

    label("Function_13_1D39")

    EventBegin(0x1)
    OP_23(0x1CB)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/U4150   ._SN", 116, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1D39 end

    def Function_14_1D51(): pass

    label("Function_14_1D51")

    EventBegin(0x0)
    SetChrPos(0x0, 6000, 0, -42000, 270)
    SetChrPos(0x1, 6000, 0, -44000, 270)
    SetChrPos(0x2, 8000, 0, -42000, 270)
    SetChrPos(0x3, 8000, 0, -44000, 270)
    Call(6, 27)
    EventEnd(0x0)
    Return()

    # Function_14_1D51 end

    SaveToFile()

Try(main)
