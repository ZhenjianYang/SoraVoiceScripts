from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7416   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7416.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60225",
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
        'Tildawn',                              # 9
        'Arrow Balloon',                        # 10
        '',                                     # 11
        '',                                     # 12
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
        'ED6_DT29/CH14840 ._CH',             # 00
        'ED6_DT29/CH14840 ._CH',             # 01
        'ED6_DT29/CH14880 ._CH',             # 02
        'ED6_DT29/CH14880 ._CH',             # 03
        'ED6_DT29/CH14040 ._CH',             # 04
        'ED6_DT29/CH14040 ._CH',             # 05
        'ED6_DT29/CH14890 ._CH',             # 06
        'ED6_DT29/CH14890 ._CH',             # 07
        'ED6_DT29/CH14820 ._CH',             # 08
        'ED6_DT29/CH14820 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14840P._CP',             # 00
        'ED6_DT29/CH14840P._CP',             # 01
        'ED6_DT29/CH14880P._CP',             # 02
        'ED6_DT29/CH14880P._CP',             # 03
        'ED6_DT29/CH14040P._CP',             # 04
        'ED6_DT29/CH14040P._CP',             # 05
        'ED6_DT29/CH14890P._CP',             # 06
        'ED6_DT29/CH14890P._CP',             # 07
        'ED6_DT29/CH14820P._CP',             # 08
        'ED6_DT29/CH14820P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 22130,
        Z                   = 0,
        Y                   = 73450,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x321,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -60530,
        Z                   = 0,
        Y                   = 58840,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x320,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -3770,
        Y                   = -1000,
        Z                   = -36070,
        Range               = 4350,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFF7FEA,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 21980,
        TriggerZ            = 0,
        TriggerY            = 76800,
        TriggerRange        = 1000,
        ActorX              = 21980,
        ActorZ              = 1000,
        ActorY              = 76800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18170,
        TriggerZ            = 0,
        TriggerY            = 73070,
        TriggerRange        = 1000,
        ActorX              = 18170,
        ActorZ              = 1000,
        ActorY              = 73070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25730,
        TriggerZ            = 0,
        TriggerY            = 73030,
        TriggerRange        = 1000,
        ActorX              = 25730,
        ActorZ              = 1000,
        ActorY              = 73030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1FE",          # 00, 0
        "Function_1_25D",          # 01, 1
        "Function_2_2D5",          # 02, 2
        "Function_3_36E",          # 03, 3
        "Function_4_4AA",          # 04, 4
        "Function_5_605",          # 05, 5
        "Function_6_C4F",          # 06, 6
        "Function_7_C8C",          # 07, 7
    )


    def Function_0_1FE(): pass

    label("Function_0_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25C")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -150, 500, -25050, 180)

    def lambda_226():

        label("loc_226")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_226")

    QueueWorkItem2(0x10, 3, lambda_226)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1650, 2500, -25190, 180)

    def lambda_24F():

        label("loc_24F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_24F")

    QueueWorkItem2(0x11, 3, lambda_24F)

    label("loc_25C")

    Return()

    # Function_0_1FE end

    def Function_1_25D(): pass

    label("Function_1_25D")

    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B")
    OP_6F(0x0, 0)
    Jump("loc_2A2")

    label("loc_29B")

    OP_6F(0x0, 60)

    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4")
    OP_6F(0x1, 0)
    Jump("loc_2BB")

    label("loc_2B4")

    OP_6F(0x1, 60)

    label("loc_2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD")
    OP_6F(0x2, 0)
    Jump("loc_2D4")

    label("loc_2CD")

    OP_6F(0x2, 60)

    label("loc_2D4")

    Return()

    # Function_1_25D end

    def Function_2_2D5(): pass

    label("Function_2_2D5")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 24)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2CA4)
    Jump("loc_357")

    label("loc_326")


    AnonymousTalk(    #0
        "\x07\x05The cute chest is empty...but still cute.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_357")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_2_2D5 end

    def Function_3_36E(): pass

    label("Function_3_36E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_447")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_3DC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05Found \x1F\xF7\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CA5)
    Jump("loc_444")

    label("loc_3DC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Found \x1F\xF7\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF7\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_444")

    Jump("loc_49C")

    label("loc_447")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05This has been quite a journey for you, hasn't it?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_49C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_36E end

    def Function_4_4AA(): pass

    label("Function_4_4AA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_583")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_518")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05Found \x1F\x01\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CA6)
    Jump("loc_580")

    label("loc_518")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Found \x1F\x01\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x01\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_580")

    Jump("loc_5F7")

    label("loc_583")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05You deserve a win. I'll be right here and cheering you on every step of\x01",
            "the way.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_5F7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4AA end

    def Function_5_605(): pass

    label("Function_5_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 7)), scpexpr(EXPR_END)), "loc_60D")
    Return()

    label("loc_60D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 0)), scpexpr(EXPR_END)), "loc_70F")
    EventBegin(0x0)
    Fade(500)
    OP_E0(0, 0x4A, 0x2)
    OP_E0(1, 0x4B, 0x2)
    OP_E0(2, 0x4C, 0x2)
    OP_E0(3, 0x4D, 0x2)
    SetChrPos(0x0, -940, 0, -35930, 0)
    SetChrPos(0x1, 590, 0, -35940, 0)
    SetChrPos(0x2, -1160, 0, -37540, 0)
    SetChrPos(0x3, 610, 0, -37650, 0)
    OP_6D(1400, 0, -29810, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(45000, 0)
    OP_6E(455, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 10)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 11)
    SetChrSubChip(0x1, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 12)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 13)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    Sleep(500)
    Jump("loc_94F")

    label("loc_70F")

    EventBegin(0x0)
    OP_E0(0, 0x4A, 0x2)
    OP_E0(1, 0x4B, 0x2)
    OP_E0(2, 0x4C, 0x2)
    OP_E0(3, 0x4D, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -150, 2500, -25050, 180)

    def lambda_741():

        label("loc_741")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_741")

    QueueWorkItem2(0x10, 3, lambda_741)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1650, 5500, -25190, 180)

    def lambda_775():

        label("loc_775")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_775")

    QueueWorkItem2(0x11, 3, lambda_775)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7AF():
        OP_6D(2300, 0, -23590, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_7AF)

    def lambda_7C7():
        OP_67(0, 5750, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7C7)

    def lambda_7DF():
        OP_6B(2340, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_7DF)

    def lambda_7EF():
        OP_6E(454, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_7EF)

    def lambda_7FF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7FF)
    Sleep(100)

    def lambda_812():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_812)
    Sleep(100)

    def lambda_825():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_825)
    Sleep(100)
    OP_8C(0x3, 0, 400)
    WaitChrThread(0x0, 0x0)
    SetChrPos(0x0, -940, 0, -35930, 0)
    SetChrPos(0x1, 590, 0, -35940, 0)
    SetChrPos(0x2, -1160, 0, -37540, 0)
    SetChrPos(0x3, 610, 0, -37650, 0)
    OP_43(0x10, 0x0, 0x0, 0x6)
    OP_43(0x11, 0x0, 0x0, 0x7)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(1000)

    def lambda_8A5():
        OP_6D(1400, 0, -29810, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8A5)

    def lambda_8BD():
        OP_67(0, 5640, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8BD)

    def lambda_8D5():
        OP_6B(2410, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_8D5)

    def lambda_8E5():
        OP_6E(455, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_8E5)
    WaitChrThread(0x0, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 10)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 11)
    SetChrSubChip(0x1, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 12)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 13)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    Sleep(500)

    label("loc_94F")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_95E():
        OP_6D(500, 0, -34310, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_95E)

    def lambda_976():
        OP_67(0, 5760, -10000, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_976)

    def lambda_98E():
        OP_6B(1920, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_98E)

    def lambda_99E():
        OP_6E(370, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_99E)
    SetChrChipByIndex(0x11, 3)

    def lambda_9B3():
        OP_8F(0xFE, 0x28, 0x3E8, 0xFFFF7626, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_9B3)

    def lambda_9CE():

        label("loc_9CE")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_9CE")

    QueueWorkItem2(0x11, 3, lambda_9CE)
    Sleep(50)
    SetChrChipByIndex(0x10, 1)

    def lambda_9EB():
        OP_8F(0xFE, 0x28, 0x1F4, 0xFFFF7626, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_9EB)

    def lambda_A06():

        label("loc_A06")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_A06")

    QueueWorkItem2(0x10, 3, lambda_A06)
    WaitChrThread(0x0, 0x3)
    Battle(0x331, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_A45"),
        (2, "loc_B16"),
        (1, "loc_C39"),
        (SWITCH_DEFAULT, "loc_C3E"),
    )


    label("loc_A45")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(-80, 0, -32299, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, -80, 0, -32299, 0)
    SetChrPos(0x1, -80, 0, -32299, 0)
    SetChrPos(0x2, -80, 0, -32299, 0)
    SetChrPos(0x3, -80, 0, -32299, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C2F)
    Jump("loc_C3E")

    label("loc_B16")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -150, 500, -25050, 180)

    def lambda_B4D():

        label("loc_B4D")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B4D")

    QueueWorkItem2(0x10, 3, lambda_B4D)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1650, 2500, -25190, 180)

    def lambda_B76():

        label("loc_B76")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B76")

    QueueWorkItem2(0x11, 3, lambda_B76)
    OP_6D(-370, 0, -37960, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, -370, 0, -37960, 0)
    SetChrPos(0x1, -370, 0, -37960, 0)
    SetChrPos(0x2, -370, 0, -37960, 0)
    SetChrPos(0x3, -370, 0, -37960, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C30)
    Jump("loc_C3E")

    label("loc_C39")

    OP_B4(0x0)
    Jump("loc_C3E")

    label("loc_C3E")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_5_605 end

    def Function_6_C4F(): pass

    label("Function_6_C4F")


    def lambda_C55():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C55)

    def lambda_C67():
        OP_8F(0xFE, 0xFFFFFF6A, 0x1F4, 0xFFFF9E26, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C67)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_6_C4F end

    def Function_7_C8C(): pass

    label("Function_7_C8C")


    def lambda_C92():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C92)

    def lambda_CA4():
        OP_8F(0xFE, 0x672, 0x9C4, 0xFFFF9D9A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CA4)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_7_C8C end

    SaveToFile()

Try(main)
