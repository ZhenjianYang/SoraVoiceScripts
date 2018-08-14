from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7426   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7426.x',
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
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT29/CH14881 ._CH',             # 03
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
        'ED6_DT29/CH14881P._CP',             # 03
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
        X                   = -90260,
        Z                   = 0,
        Y                   = -73990,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -93990,
        Z                   = 0,
        Y                   = -77780,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -97810,
        Z                   = 0,
        Y                   = -73980,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -94000,
        Z                   = 0,
        Y                   = -70240,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19620,
        Z                   = 6000,
        Y                   = 113250,
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
        X                   = 15450,
        Z                   = 6000,
        Y                   = 124860,
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
        X                   = -8240,
        Y                   = 5000,
        Z                   = 249100,
        Range               = 160,
        Unknown_10          = 0x2AF8,
        Unknown_14          = 0x3DD1A,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = -94060,
        TriggerZ            = 0,
        TriggerY            = -74020,
        TriggerRange        = 1000,
        ActorX              = -94060,
        ActorZ              = 1000,
        ActorY              = -74020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -23590,
        TriggerZ            = 6000,
        TriggerY            = 112970,
        TriggerRange        = 1000,
        ActorX              = -23590,
        ActorZ              = 7000,
        ActorY              = 112970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19950,
        TriggerZ            = 6000,
        TriggerY            = 116710,
        TriggerRange        = 1000,
        ActorX              = -19950,
        ActorZ              = 7000,
        ActorY              = 116710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19950,
        TriggerZ            = 6000,
        TriggerY            = 109240,
        TriggerRange        = 1000,
        ActorX              = -19950,
        ActorZ              = 7000,
        ActorY              = 109240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 19860,
        TriggerZ            = 6000,
        TriggerY            = 125000,
        TriggerRange        = 1000,
        ActorX              = 19860,
        ActorZ              = 7000,
        ActorY              = 125000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15980,
        TriggerZ            = 6000,
        TriggerY            = 128820,
        TriggerRange        = 1000,
        ActorX              = 15980,
        ActorZ              = 7000,
        ActorY              = 128820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16010,
        TriggerZ            = 6000,
        TriggerY            = 121230,
        TriggerRange        = 1000,
        ActorX              = 16010,
        ActorZ              = 7000,
        ActorY              = 121230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2FE",          # 00, 0
        "Function_1_35D",          # 01, 1
        "Function_2_47B",          # 02, 2
        "Function_3_59D",          # 03, 3
        "Function_4_6BD",          # 04, 4
        "Function_5_7DD",          # 05, 5
        "Function_6_8FD",          # 06, 6
        "Function_7_97A",          # 07, 7
        "Function_8_A9A",          # 08, 8
        "Function_9_BBA",          # 09, 9
        "Function_10_1204",        # 0A, 10
        "Function_11_1241",        # 0B, 11
    )


    def Function_0_2FE(): pass

    label("Function_0_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35C")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -4140, 6500, 260810, 180)

    def lambda_326():

        label("loc_326")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_326")

    QueueWorkItem2(0x10, 3, lambda_326)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2570, 8500, 260230, 180)

    def lambda_34F():

        label("loc_34F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_34F")

    QueueWorkItem2(0x11, 3, lambda_34F)

    label("loc_35C")

    Return()

    # Function_0_2FE end

    def Function_1_35D(): pass

    label("Function_1_35D")

    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD")
    OP_6F(0x0, 0)
    Jump("loc_3E4")

    label("loc_3DD")

    OP_6F(0x0, 60)

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6")
    OP_6F(0x1, 0)
    Jump("loc_3FD")

    label("loc_3F6")

    OP_6F(0x1, 60)

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F")
    OP_6F(0x2, 0)
    Jump("loc_416")

    label("loc_40F")

    OP_6F(0x2, 60)

    label("loc_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_428")
    OP_6F(0x3, 0)
    Jump("loc_42F")

    label("loc_428")

    OP_6F(0x3, 60)

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441")
    OP_6F(0x4, 0)
    Jump("loc_448")

    label("loc_441")

    OP_6F(0x4, 60)

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A")
    OP_6F(0x5, 0)
    Jump("loc_461")

    label("loc_45A")

    OP_6F(0x5, 60)

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_473")
    OP_6F(0x6, 0)
    Jump("loc_47A")

    label("loc_473")

    OP_6F(0x6, 60)

    label("loc_47A")

    Return()

    # Function_1_35D end

    def Function_2_47B(): pass

    label("Function_2_47B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17F, 1)"), scpexpr(EXPR_END)), "loc_4EF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x7F\x01\x07\x00。\x02",
    )

    Jump("loc_4D4")

    label("loc_4D4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CCD)
    Jump("loc_55B")

    label("loc_4EF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x7F\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x7F\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_53C")

    label("loc_53C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_55B")

    Jump("loc_58F")

    label("loc_55E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_58F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_47B end

    def Function_3_59D(): pass

    label("Function_3_59D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_60F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    Jump("loc_5F4")

    label("loc_5F4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CCE)
    Jump("loc_67B")

    label("loc_60F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x01\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_65C")

    label("loc_65C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_67B")

    Jump("loc_6AF")

    label("loc_67E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6AF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_59D end

    def Function_4_6BD(): pass

    label("Function_4_6BD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_72F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    Jump("loc_714")

    label("loc_714")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CCF)
    Jump("loc_79B")

    label("loc_72F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFB\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_77C")

    label("loc_77C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_79B")

    Jump("loc_7CF")

    label("loc_79E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7CF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6BD end

    def Function_5_7DD(): pass

    label("Function_5_7DD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_84F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    Jump("loc_834")

    label("loc_834")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CD0)
    Jump("loc_8BB")

    label("loc_84F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x06\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_89C")

    label("loc_89C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_8BB")

    Jump("loc_8EF")

    label("loc_8BE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8EF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7DD end

    def Function_6_8FD(): pass

    label("Function_6_8FD")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 28)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2CD1)
    Jump("loc_968")

    label("loc_94E")


    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_968")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8FD end

    def Function_7_97A(): pass

    label("Function_7_97A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_9EC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\xFA\x01\x07\x00。\x02",
    )

    Jump("loc_9D1")

    label("loc_9D1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CD2)
    Jump("loc_A58")

    label("loc_9EC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "宝箱里装有\x1F\xFA\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFA\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_A39")

    label("loc_A39")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_A58")

    Jump("loc_A8C")

    label("loc_A5B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A8C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_97A end

    def Function_8_A9A(): pass

    label("Function_8_A9A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_B0C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\x04\x02\x07\x00。\x02",
    )

    Jump("loc_AF1")

    label("loc_AF1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CD3)
    Jump("loc_B78")

    label("loc_B0C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "宝箱里装有\x1F\x04\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x04\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_B59")

    label("loc_B59")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_B78")

    Jump("loc_BAC")

    label("loc_B7B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BAC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_A9A end

    def Function_9_BBA(): pass

    label("Function_9_BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 3)), scpexpr(EXPR_END)), "loc_BC2")
    Return()

    label("loc_BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 4)), scpexpr(EXPR_END)), "loc_CC4")
    EventBegin(0x0)
    Fade(500)
    OP_E0(0, 0x4A, 0x2)
    OP_E0(1, 0x4B, 0x2)
    OP_E0(2, 0x4C, 0x2)
    OP_E0(3, 0x4D, 0x2)
    SetChrPos(0x0, -4780, 6000, 249400, 0)
    SetChrPos(0x1, -3370, 6000, 249200, 0)
    SetChrPos(0x2, -5020, 6000, 247450, 0)
    SetChrPos(0x3, -3250, 6000, 247430, 0)
    OP_6D(-2700, 6000, 254320, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(2210, 0)
    OP_6C(45000, 0)
    OP_6E(462, 0)
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
    Jump("loc_F04")

    label("loc_CC4")

    EventBegin(0x0)
    OP_E0(0, 0x4A, 0x2)
    OP_E0(1, 0x4B, 0x2)
    OP_E0(2, 0x4C, 0x2)
    OP_E0(3, 0x4D, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -4140, 8500, 260810, 180)

    def lambda_CF6():

        label("loc_CF6")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_CF6")

    QueueWorkItem2(0x10, 3, lambda_CF6)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2570, 11500, 260230, 180)

    def lambda_D2A():

        label("loc_D2A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D2A")

    QueueWorkItem2(0x11, 3, lambda_D2A)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_D64():
        OP_6D(-1490, 6000, 262240, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_D64)

    def lambda_D7C():
        OP_67(0, 5750, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D7C)

    def lambda_D94():
        OP_6B(2340, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D94)

    def lambda_DA4():
        OP_6E(454, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_DA4)

    def lambda_DB4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DB4)
    Sleep(100)

    def lambda_DC7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_DC7)
    Sleep(100)

    def lambda_DDA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_DDA)
    Sleep(100)
    OP_8C(0x3, 0, 400)
    WaitChrThread(0x0, 0x0)
    SetChrPos(0x0, -4780, 6000, 249400, 0)
    SetChrPos(0x1, -3370, 6000, 249200, 0)
    SetChrPos(0x2, -5020, 6000, 247450, 0)
    SetChrPos(0x3, -3250, 6000, 247430, 0)
    OP_43(0x10, 0x0, 0x0, 0xA)
    OP_43(0x11, 0x0, 0x0, 0xB)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(1000)

    def lambda_E5A():
        OP_6D(-2700, 6000, 254320, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_E5A)

    def lambda_E72():
        OP_67(0, 6360, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E72)

    def lambda_E8A():
        OP_6B(2210, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_E8A)

    def lambda_E9A():
        OP_6E(465, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_E9A)
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

    label("loc_F04")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_F13():
        OP_6D(-2800, 6000, 251750, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_F13)

    def lambda_F2B():
        OP_67(0, 6330, -10000, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_F2B)

    def lambda_F43():
        OP_6B(1920, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_F43)

    def lambda_F53():
        OP_6E(370, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_F53)
    SetChrChipByIndex(0x11, 3)

    def lambda_F68():
        OP_8F(0xFE, 0xFFFFF0D8, 0x1B58, 0x3CD70, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_F68)

    def lambda_F83():

        label("loc_F83")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_F83")

    QueueWorkItem2(0x11, 3, lambda_F83)
    Sleep(50)
    SetChrChipByIndex(0x10, 1)

    def lambda_FA0():
        OP_8F(0xFE, 0xFFFFF0D8, 0x1964, 0x3CD70, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_FA0)

    def lambda_FBB():

        label("loc_FBB")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_FBB")

    QueueWorkItem2(0x10, 3, lambda_FBB)
    WaitChrThread(0x0, 0x3)
    Battle(0x333, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_FFA"),
        (2, "loc_10CB"),
        (1, "loc_11EE"),
        (SWITCH_DEFAULT, "loc_11F3"),
    )


    label("loc_FFA")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(-4240, 6000, 254970, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, -4240, 6000, 254970, 0)
    SetChrPos(0x1, -4240, 6000, 254970, 0)
    SetChrPos(0x2, -4240, 6000, 254970, 0)
    SetChrPos(0x3, -4240, 6000, 254970, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C33)
    Jump("loc_11F3")

    label("loc_10CB")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -4140, 6500, 260810, 180)

    def lambda_1102():

        label("loc_1102")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1102")

    QueueWorkItem2(0x10, 3, lambda_1102)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2570, 8500, 260230, 180)

    def lambda_112B():

        label("loc_112B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_112B")

    QueueWorkItem2(0x11, 3, lambda_112B)
    OP_6D(-4280, 6000, 247440, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, -4280, 6000, 247440, 0)
    SetChrPos(0x1, -4280, 6000, 247440, 0)
    SetChrPos(0x2, -4280, 6000, 247440, 0)
    SetChrPos(0x3, -4280, 6000, 247440, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C34)
    Jump("loc_11F3")

    label("loc_11EE")

    OP_B4(0x0)
    Jump("loc_11F3")

    label("loc_11F3")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_BBA end

    def Function_10_1204(): pass

    label("Function_10_1204")


    def lambda_120A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_120A)

    def lambda_121C():
        OP_8F(0xFE, 0xFFFFEFD4, 0x1964, 0x3FACA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_121C)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_10_1204 end

    def Function_11_1241(): pass

    label("Function_11_1241")


    def lambda_1247():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1247)

    def lambda_1259():
        OP_8F(0xFE, 0xFFFFF5F6, 0x2134, 0x3F886, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1259)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_11_1241 end

    SaveToFile()

Try(main)
