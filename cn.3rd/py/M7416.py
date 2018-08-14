from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '命运终结天使',                         # 9
        '神箭天使',                             # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        "Function_3_354",          # 03, 3
        "Function_4_476",          # 04, 4
        "Function_5_596",          # 05, 5
        "Function_6_BE0",          # 06, 6
        "Function_7_C1D",          # 07, 7
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
    Jump("loc_342")

    label("loc_326")


    AnonymousTalk(    #0
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_342")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2D5 end

    def Function_3_354(): pass

    label("Function_3_354")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_437")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_3C8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_3AD")

    label("loc_3AD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CA5)
    Jump("loc_434")

    label("loc_3C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_415")

    label("loc_415")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_434")

    Jump("loc_468")

    label("loc_437")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_468")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_354 end

    def Function_4_476(): pass

    label("Function_4_476")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x594, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_557")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_4E8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    Jump("loc_4CD")

    label("loc_4CD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CA6)
    Jump("loc_554")

    label("loc_4E8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x01\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_535")

    label("loc_535")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_554")

    Jump("loc_588")

    label("loc_557")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_588")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_476 end

    def Function_5_596(): pass

    label("Function_5_596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 7)), scpexpr(EXPR_END)), "loc_59E")
    Return()

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 0)), scpexpr(EXPR_END)), "loc_6A0")
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
    Jump("loc_8E0")

    label("loc_6A0")

    EventBegin(0x0)
    OP_E0(0, 0x4A, 0x2)
    OP_E0(1, 0x4B, 0x2)
    OP_E0(2, 0x4C, 0x2)
    OP_E0(3, 0x4D, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -150, 2500, -25050, 180)

    def lambda_6D2():

        label("loc_6D2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6D2")

    QueueWorkItem2(0x10, 3, lambda_6D2)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1650, 5500, -25190, 180)

    def lambda_706():

        label("loc_706")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_706")

    QueueWorkItem2(0x11, 3, lambda_706)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_740():
        OP_6D(2300, 0, -23590, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_740)

    def lambda_758():
        OP_67(0, 5750, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_758)

    def lambda_770():
        OP_6B(2340, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_770)

    def lambda_780():
        OP_6E(454, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_780)

    def lambda_790():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_790)
    Sleep(100)

    def lambda_7A3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7A3)
    Sleep(100)

    def lambda_7B6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7B6)
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

    def lambda_836():
        OP_6D(1400, 0, -29810, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_836)

    def lambda_84E():
        OP_67(0, 5640, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_84E)

    def lambda_866():
        OP_6B(2410, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_866)

    def lambda_876():
        OP_6E(455, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_876)
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

    label("loc_8E0")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8EF():
        OP_6D(500, 0, -34310, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_8EF)

    def lambda_907():
        OP_67(0, 5760, -10000, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_907)

    def lambda_91F():
        OP_6B(1920, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_91F)

    def lambda_92F():
        OP_6E(370, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_92F)
    SetChrChipByIndex(0x11, 3)

    def lambda_944():
        OP_8F(0xFE, 0x28, 0x3E8, 0xFFFF7626, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_944)

    def lambda_95F():

        label("loc_95F")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_95F")

    QueueWorkItem2(0x11, 3, lambda_95F)
    Sleep(50)
    SetChrChipByIndex(0x10, 1)

    def lambda_97C():
        OP_8F(0xFE, 0x28, 0x1F4, 0xFFFF7626, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_97C)

    def lambda_997():

        label("loc_997")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_997")

    QueueWorkItem2(0x10, 3, lambda_997)
    WaitChrThread(0x0, 0x3)
    Battle(0x331, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_9D6"),
        (2, "loc_AA7"),
        (1, "loc_BCA"),
        (SWITCH_DEFAULT, "loc_BCF"),
    )


    label("loc_9D6")

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
    Jump("loc_BCF")

    label("loc_AA7")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -150, 500, -25050, 180)

    def lambda_ADE():

        label("loc_ADE")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_ADE")

    QueueWorkItem2(0x10, 3, lambda_ADE)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1650, 2500, -25190, 180)

    def lambda_B07():

        label("loc_B07")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B07")

    QueueWorkItem2(0x11, 3, lambda_B07)
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
    Jump("loc_BCF")

    label("loc_BCA")

    OP_B4(0x0)
    Jump("loc_BCF")

    label("loc_BCF")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_5_596 end

    def Function_6_BE0(): pass

    label("Function_6_BE0")


    def lambda_BE6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE6)

    def lambda_BF8():
        OP_8F(0xFE, 0xFFFFFF6A, 0x1F4, 0xFFFF9E26, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BF8)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_6_BE0 end

    def Function_7_C1D(): pass

    label("Function_7_C1D")


    def lambda_C23():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C23)

    def lambda_C35():
        OP_8F(0xFE, 0x672, 0x9C4, 0xFFFF9D9A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C35)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_7_C1D end

    SaveToFile()

Try(main)
