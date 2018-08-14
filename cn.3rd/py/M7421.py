from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7421   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7421.x',
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
        '斯莱普尼尔',                           # 9
        '权杖天使',                             # 10
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
        'ED6_DT29/CH14610 ._CH',             # 00
        'ED6_DT29/CH14611 ._CH',             # 01
        'ED6_DT29/CH14040 ._CH',             # 02
        'ED6_DT29/CH14041 ._CH',             # 03
        'ED6_DT29/CH14880 ._CH',             # 04
        'ED6_DT29/CH14880 ._CH',             # 05
        'ED6_DT29/CH14890 ._CH',             # 06
        'ED6_DT29/CH14890 ._CH',             # 07
        'ED6_DT29/CH14840 ._CH',             # 08
        'ED6_DT29/CH14840 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14610P._CP',             # 00
        'ED6_DT29/CH14611P._CP',             # 01
        'ED6_DT29/CH14040P._CP',             # 02
        'ED6_DT29/CH14041P._CP',             # 03
        'ED6_DT29/CH14880P._CP',             # 04
        'ED6_DT29/CH14880P._CP',             # 05
        'ED6_DT29/CH14890P._CP',             # 06
        'ED6_DT29/CH14890P._CP',             # 07
        'ED6_DT29/CH14840P._CP',             # 08
        'ED6_DT29/CH14840P._CP',             # 09
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 130,
        Z                   = 4000,
        Y                   = 90130,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x326,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4190,
        Z                   = 0,
        Y                   = 191700,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x322,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -3910,
        Y                   = -1000,
        Z                   = -10300,
        Range               = 4260,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFE3FE,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 4000,
        TriggerY            = 88000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 5000,
        ActorY              = 88000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2500,
        TriggerZ            = 4000,
        TriggerY            = 88000,
        TriggerRange        = 1000,
        ActorX              = -2500,
        ActorZ              = 5000,
        ActorY              = 88000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2500,
        TriggerZ            = 4000,
        TriggerY            = 88000,
        TriggerRange        = 1000,
        ActorX              = 2500,
        ActorZ              = 5000,
        ActorY              = 88000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2800,
        TriggerZ            = 0,
        TriggerY            = 229000,
        TriggerRange        = 1000,
        ActorX              = 2800,
        ActorZ              = 1000,
        ActorY              = 229000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2800,
        TriggerZ            = 0,
        TriggerY            = 229000,
        TriggerRange        = 1000,
        ActorX              = -2800,
        ActorZ              = 1000,
        ActorY              = 229000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_246",          # 00, 0
        "Function_1_2D1",          # 01, 1
        "Function_2_3D6",          # 02, 2
        "Function_3_4F8",          # 03, 3
        "Function_4_575",          # 04, 4
        "Function_5_695",          # 05, 5
        "Function_6_7B5",          # 06, 6
        "Function_7_8D5",          # 07, 7
        "Function_8_F1F",          # 08, 8
        "Function_9_F5C",          # 09, 9
    )


    def Function_0_246(): pass

    label("Function_0_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A4")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -180, 500, 850, 180)

    def lambda_26E():

        label("loc_26E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_26E")

    QueueWorkItem2(0x10, 3, lambda_26E)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1600, 2500, 440, 180)

    def lambda_297():

        label("loc_297")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_297")

    QueueWorkItem2(0x11, 3, lambda_297)

    label("loc_2A4")

    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_246 end

    def Function_1_2D1(): pass

    label("Function_1_2D1")

    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F9")
    OP_6F(0x0, 0)
    Jump("loc_300")

    label("loc_2F9")

    OP_6F(0x0, 60)

    label("loc_300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312")
    OP_6F(0x1, 0)
    Jump("loc_319")

    label("loc_312")

    OP_6F(0x1, 60)

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B")
    OP_6F(0x2, 0)
    Jump("loc_332")

    label("loc_32B")

    OP_6F(0x2, 60)

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344")
    OP_6F(0x3, 0)
    Jump("loc_34B")

    label("loc_344")

    OP_6F(0x3, 60)

    label("loc_34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D")
    OP_6F(0x4, 0)
    Jump("loc_364")

    label("loc_35D")

    OP_6F(0x4, 60)

    label("loc_364")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A5")
    OP_E5(0x0, 0xFF, 0x1, 1)
    OP_E5(0x0, 0xFF, 0x17, 1)
    OP_E5(0x0, 0xFF, 0x19, 1)
    OP_E5(0x1, 0xFF, 0x2, 1)
    OP_E5(0x1, 0xFF, 0x18, 1)
    OP_E5(0x1, 0xFF, 0x1A, 1)
    Jump("loc_3D5")

    label("loc_3A5")

    OP_E5(0x1, 0xFF, 0x1, 1)
    OP_E5(0x1, 0xFF, 0x17, 1)
    OP_E5(0x1, 0xFF, 0x19, 1)
    OP_E5(0x0, 0xFF, 0x2, 1)
    OP_E5(0x0, 0xFF, 0x18, 1)
    OP_E5(0x0, 0xFF, 0x1A, 1)

    label("loc_3D5")

    Return()

    # Function_1_2D1 end

    def Function_2_3D6(): pass

    label("Function_2_3D6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_44A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    Jump("loc_42F")

    label("loc_42F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CBC)
    Jump("loc_4B6")

    label("loc_44A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x06\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_497")

    label("loc_497")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4B6")

    Jump("loc_4EA")

    label("loc_4B9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4EA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3D6 end

    def Function_3_4F8(): pass

    label("Function_3_4F8")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_549")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 24)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2CBD)
    Jump("loc_563")

    label("loc_549")


    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_563")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4F8 end

    def Function_4_575(): pass

    label("Function_4_575")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_656")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x173, 1)"), scpexpr(EXPR_END)), "loc_5E7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\x73\x01\x07\x00。\x02",
    )

    Jump("loc_5CC")

    label("loc_5CC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CBE)
    Jump("loc_653")

    label("loc_5E7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\x73\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x73\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_634")

    label("loc_634")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_653")

    Jump("loc_687")

    label("loc_656")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_687")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_575 end

    def Function_5_695(): pass

    label("Function_5_695")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_776")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_707")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_6EC")

    label("loc_6EC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CBF)
    Jump("loc_773")

    label("loc_707")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_754")

    label("loc_754")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_773")

    Jump("loc_7A7")

    label("loc_776")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7A7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_695 end

    def Function_6_7B5(): pass

    label("Function_6_7B5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_896")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_827")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    Jump("loc_80C")

    label("loc_80C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CBB)
    Jump("loc_893")

    label("loc_827")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x01\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_874")

    label("loc_874")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_893")

    Jump("loc_8C7")

    label("loc_896")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8C7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7B5 end

    def Function_7_8D5(): pass

    label("Function_7_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 1)), scpexpr(EXPR_END)), "loc_8DD")
    Return()

    label("loc_8DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 2)), scpexpr(EXPR_END)), "loc_9DF")
    EventBegin(0x0)
    Fade(500)
    OP_E0(0, 0x4A, 0x2)
    OP_E0(1, 0x4B, 0x2)
    OP_E0(2, 0x4C, 0x2)
    OP_E0(3, 0x4D, 0x2)
    SetChrPos(0x0, -580, 0, -9940, 0)
    SetChrPos(0x1, 780, 0, -10100, 0)
    SetChrPos(0x2, -1000, 0, -11770, 0)
    SetChrPos(0x3, 720, 0, -11820, 0)
    OP_6D(1500, 0, -4950, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(2360, 0)
    OP_6C(45000, 0)
    OP_6E(426, 0)
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
    Jump("loc_C1F")

    label("loc_9DF")

    EventBegin(0x0)
    OP_E0(0, 0x4A, 0x2)
    OP_E0(1, 0x4B, 0x2)
    OP_E0(2, 0x4C, 0x2)
    OP_E0(3, 0x4D, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -180, 2500, 850, 180)

    def lambda_A11():

        label("loc_A11")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A11")

    QueueWorkItem2(0x10, 3, lambda_A11)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1600, 5500, 440, 180)

    def lambda_A45():

        label("loc_A45")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A45")

    QueueWorkItem2(0x11, 3, lambda_A45)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_A7F():
        OP_6D(1980, 0, 2020, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A7F)

    def lambda_A97():
        OP_67(0, 4950, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A97)

    def lambda_AAF():
        OP_6B(2390, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_AAF)

    def lambda_ABF():
        OP_6E(436, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_ABF)

    def lambda_ACF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_ACF)
    Sleep(100)

    def lambda_AE2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AE2)
    Sleep(100)

    def lambda_AF5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AF5)
    Sleep(100)
    OP_8C(0x3, 0, 400)
    WaitChrThread(0x0, 0x0)
    SetChrPos(0x0, -580, 0, -9940, 0)
    SetChrPos(0x1, 780, 0, -10100, 0)
    SetChrPos(0x2, -1000, 0, -11770, 0)
    SetChrPos(0x3, 720, 0, -11820, 0)
    OP_43(0x10, 0x0, 0x0, 0x8)
    OP_43(0x11, 0x0, 0x0, 0x9)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(1000)

    def lambda_B75():
        OP_6D(1500, 0, -4950, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_B75)

    def lambda_B8D():
        OP_67(0, 5520, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B8D)

    def lambda_BA5():
        OP_6B(2360, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BA5)

    def lambda_BB5():
        OP_6E(426, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_BB5)
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

    label("loc_C1F")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C2E():
        OP_6D(1100, 0, -7600, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_C2E)

    def lambda_C46():
        OP_67(0, 5640, -10000, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_C46)

    def lambda_C5E():
        OP_6B(1880, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_C5E)

    def lambda_C6E():
        OP_6E(370, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_C6E)
    SetChrChipByIndex(0x11, 3)

    def lambda_C83():
        OP_8F(0xFE, 0x96, 0x3E8, 0xFFFFD81E, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_C83)

    def lambda_C9E():

        label("loc_C9E")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_C9E")

    QueueWorkItem2(0x11, 3, lambda_C9E)
    Sleep(50)
    SetChrChipByIndex(0x10, 1)

    def lambda_CBB():
        OP_8F(0xFE, 0x96, 0x1F4, 0xFFFFD81E, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_CBB)

    def lambda_CD6():

        label("loc_CD6")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_CD6")

    QueueWorkItem2(0x10, 3, lambda_CD6)
    WaitChrThread(0x0, 0x3)
    Battle(0x332, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D15"),
        (2, "loc_DE6"),
        (1, "loc_F09"),
        (SWITCH_DEFAULT, "loc_F0E"),
    )


    label("loc_D15")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(50, 0, -6510, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, 50, 0, -6510, 0)
    SetChrPos(0x1, 50, 0, -6510, 0)
    SetChrPos(0x2, 50, 0, -6510, 0)
    SetChrPos(0x3, 50, 0, -6510, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C31)
    Jump("loc_F0E")

    label("loc_DE6")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -180, 500, 850, 180)

    def lambda_E1D():

        label("loc_E1D")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_E1D")

    QueueWorkItem2(0x10, 3, lambda_E1D)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1600, 2500, 440, 180)

    def lambda_E46():

        label("loc_E46")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_E46")

    QueueWorkItem2(0x11, 3, lambda_E46)
    OP_6D(-30, 0, -11530, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, -30, 0, -11530, 0)
    SetChrPos(0x1, -30, 0, -11530, 0)
    SetChrPos(0x2, -30, 0, -11530, 0)
    SetChrPos(0x3, -30, 0, -11530, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C32)
    Jump("loc_F0E")

    label("loc_F09")

    OP_B4(0x0)
    Jump("loc_F0E")

    label("loc_F0E")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_8D5 end

    def Function_8_F1F(): pass

    label("Function_8_F1F")


    def lambda_F25():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F25)

    def lambda_F37():
        OP_8F(0xFE, 0xFFFFFF4C, 0x1F4, 0x352, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F37)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_8_F1F end

    def Function_9_F5C(): pass

    label("Function_9_F5C")


    def lambda_F62():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F62)

    def lambda_F74():
        OP_8F(0xFE, 0x640, 0x9C4, 0x1B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F74)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_9_F5C end

    SaveToFile()

Try(main)
