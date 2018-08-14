from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5501   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5501.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60233",
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
        '',                                     # 9
        '',                                     # 10
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
        'ED6_DT29/CH14540 ._CH',             # 00
        'ED6_DT29/CH14541 ._CH',             # 01
        'ED6_DT29/CH14860 ._CH',             # 02
        'ED6_DT29/CH14861 ._CH',             # 03
        'ED6_DT29/CH15000 ._CH',             # 04
        'ED6_DT29/CH15000 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14540P._CP',             # 00
        'ED6_DT29/CH14541P._CP',             # 01
        'ED6_DT29/CH14860P._CP',             # 02
        'ED6_DT29/CH14861P._CP',             # 03
        'ED6_DT29/CH15000P._CP',             # 04
        'ED6_DT29/CH15000P._CP',             # 05
    )

    DeclMonster(
        X                   = 18160,
        Z                   = 0,
        Y                   = 91630,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x190,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 25870,
        Z                   = -2000,
        Y                   = 81210,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x192,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 44220,
        Z                   = -2000,
        Y                   = 77310,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x192,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 52390,
        Z                   = 0,
        Y                   = 54280,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x191,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 16750,
        TriggerZ            = 0,
        TriggerY            = 57710,
        TriggerRange        = 1700,
        ActorX              = 16750,
        ActorZ              = 2500,
        ActorY              = 57710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 46510,
        TriggerZ            = 0,
        TriggerY            = 67900,
        TriggerRange        = 1700,
        ActorX              = 46510,
        ActorZ              = 2500,
        ActorY              = 67900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53050,
        TriggerZ            = 0,
        TriggerY            = 92420,
        TriggerRange        = 1700,
        ActorX              = 53050,
        ActorZ              = 2500,
        ActorY              = 92420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 52950,
        TriggerZ            = 0,
        TriggerY            = 48400,
        TriggerRange        = 1000,
        ActorX              = 52990,
        ActorZ              = 1000,
        ActorY              = 47900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53600,
        TriggerZ            = -2000,
        TriggerY            = 82210,
        TriggerRange        = 1000,
        ActorX              = 54300,
        ActorZ              = -1000,
        ActorY              = 82210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 55000,
        TriggerZ            = 0,
        TriggerY            = 48210,
        TriggerRange        = 1000,
        ActorX              = 55000,
        ActorZ              = 1000,
        ActorY              = 48210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51000,
        TriggerZ            = 0,
        TriggerY            = 48210,
        TriggerRange        = 1000,
        ActorX              = 51000,
        ActorZ              = 1000,
        ActorY              = 48210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35000,
        TriggerZ            = 0,
        TriggerY            = 92000,
        TriggerRange        = 1000,
        ActorX              = 35000,
        ActorZ              = 1000,
        ActorY              = 92000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_26B",          # 01, 1
        "Function_2_3AF",          # 02, 2
        "Function_3_4D5",          # 03, 3
        "Function_4_5FB",          # 04, 4
        "Function_5_721",          # 05, 5
        "Function_6_847",          # 06, 6
        "Function_7_96D",          # 07, 7
        "Function_8_C11",          # 08, 8
        "Function_9_DC2",          # 09, 9
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Return()

    # Function_0_26A end

    def Function_1_26B(): pass

    label("Function_1_26B")

    OP_BE(0x0, 0x1, 0x3, 0x190, 0x0, 0x3, -1900, 0, 0, 0, 0, 0)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x85, 0x1, 0x4B)
    SetMapFlags(0x100000)
    OP_72(0x2800, 0x0)
    ExitThread()
    OP_72(0x2801, 0x0)
    ExitThread()
    OP_72(0x2802, 0x0)
    ExitThread()
    OP_72(0x2803, 0x0)
    ExitThread()
    OP_72(0x2804, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 4)), scpexpr(EXPR_END)), "loc_2E0")
    OP_6F(0x1, 120)
    OP_6F(0x2, 60)

    label("loc_2E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 5)), scpexpr(EXPR_END)), "loc_2EE")
    OP_6F(0x2, 160)

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 6)), scpexpr(EXPR_END)), "loc_303")
    OP_6F(0x0, 60)
    OP_6F(0x4, 260)

    label("loc_303")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31F")
    OP_6F(0x5, 0)
    Jump("loc_326")

    label("loc_31F")

    OP_6F(0x5, 60)

    label("loc_326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338")
    OP_6F(0x6, 0)
    Jump("loc_33F")

    label("loc_338")

    OP_6F(0x6, 60)

    label("loc_33F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351")
    OP_6F(0x7, 0)
    Jump("loc_358")

    label("loc_351")

    OP_6F(0x7, 60)

    label("loc_358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A")
    OP_6F(0x8, 0)
    Jump("loc_371")

    label("loc_36A")

    OP_6F(0x8, 60)

    label("loc_371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x532, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_383")
    OP_6F(0x9, 0)
    Jump("loc_38A")

    label("loc_383")

    OP_6F(0x9, 60)

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C")
    OP_64(0x3, 0x1)
    OP_71(0x405, 0x0)
    ExitThread()

    label("loc_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AE")
    OP_64(0x4, 0x1)
    OP_71(0x406, 0x0)
    ExitThread()

    label("loc_3AE")

    Return()

    # Function_1_26B end

    def Function_2_3AF(): pass

    label("Function_2_3AF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_494")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x74, 1)"), scpexpr(EXPR_END)), "loc_423")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x74\x00\x07\x00。\x02",
    )

    Jump("loc_408")

    label("loc_408")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2986)
    Jump("loc_491")

    label("loc_423")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x74\x00\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x74\x00\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_472")

    label("loc_472")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_491")

    Jump("loc_4C7")

    label("loc_494")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4C7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3AF end

    def Function_3_4D5(): pass

    label("Function_3_4D5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x171, 1)"), scpexpr(EXPR_END)), "loc_549")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x71\x01\x07\x00。\x02",
    )

    Jump("loc_52E")

    label("loc_52E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2987)
    Jump("loc_5B7")

    label("loc_549")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x71\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x71\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_598")

    label("loc_598")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_5B7")

    Jump("loc_5ED")

    label("loc_5BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5ED")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4D5 end

    def Function_4_5FB(): pass

    label("Function_4_5FB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_66F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    Jump("loc_654")

    label("loc_654")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2988)
    Jump("loc_6DD")

    label("loc_66F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFC\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_6BE")

    label("loc_6BE")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_6DD")

    Jump("loc_713")

    label("loc_6E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_713")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5FB end

    def Function_5_721(): pass

    label("Function_5_721")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_806")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_795")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    Jump("loc_77A")

    label("loc_77A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2989)
    Jump("loc_803")

    label("loc_795")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFE\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_7E4")

    label("loc_7E4")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_803")

    Jump("loc_839")

    label("loc_806")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_839")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_721 end

    def Function_6_847(): pass

    label("Function_6_847")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x532, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x74, 1)"), scpexpr(EXPR_END)), "loc_8BB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\x74\x00\x07\x00。\x02",
    )

    Jump("loc_8A0")

    label("loc_8A0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2996)
    Jump("loc_929")

    label("loc_8BB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\x74\x00\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x74\x00\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_90A")

    label("loc_90A")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_929")

    Jump("loc_95F")

    label("loc_92C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_95F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_847 end

    def Function_7_96D(): pass

    label("Function_7_96D")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05有一个看似可以拉动的控制杆。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B4D")

    Menu(
        0,
        10,
        100,
        1,
        (
            "拉到右边\x01",      # 0
            "拉到左边\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    Jump("loc_9F4")

    label("loc_9F4")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6B")
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x2964)
    Sleep(500)
    OP_6D(52660, -60, 67850, 1000)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_B4A")

    label("loc_A6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4A")
    OP_6F(0x2, 100)
    OP_70(0x2, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x2965)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B20")
    Sleep(500)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_6D(52800, 0, 47980, 1500)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0xFF, 52800, 0, 47980, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_72(0x405, 0x0)
    ExitThread()
    OP_A2(0x2970)
    OP_65(0x3, 0x1)
    Sleep(1500)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_B4A")

    label("loc_B20")

    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05什么也没有发生。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_B4A")

    Jump("loc_C09")

    label("loc_B4D")


    Menu(
        0,
        10,
        100,
        1,
        (
            "恢复到起始位置\x01",      # 0
            "放弃\x01",                # 1
        )
    )

    Jump("loc_B70")

    label("loc_B70")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 4)), scpexpr(EXPR_END)), "loc_BE9")
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_6D(52660, -60, 67850, 1000)
    OP_6F(0x1, 120)
    OP_70(0x1, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    OP_A3(0x2964)
    Jump("loc_C09")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 5)), scpexpr(EXPR_END)), "loc_C09")
    OP_6F(0x2, 160)
    OP_70(0x2, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A3(0x2965)

    label("loc_C09")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_7_96D end

    def Function_8_C11(): pass

    label("Function_8_C11")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05有一个看似可以拉动的控制杆。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D60")

    Menu(
        0,
        10,
        100,
        1,
        (
            "拉下控制杆\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    Jump("loc_C74")

    label("loc_C74")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5D")
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    OP_A2(0x2967)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D33")
    Sleep(500)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_6D(53600, -2000, 82210, 1000)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0xFF, 53600, -2000, 82210, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_A2(0x2971)
    OP_65(0x4, 0x1)
    Sleep(1500)
    Fade(500)
    Jump("loc_D5D")

    label("loc_D33")

    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05什么也没有发生。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_D5D")

    Jump("loc_DBA")

    label("loc_D60")


    Menu(
        0,
        10,
        100,
        1,
        (
            "恢复到起始位置\x01",      # 0
            "放弃\x01",                # 1
        )
    )

    Jump("loc_D83")

    label("loc_D83")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBA")
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    OP_A3(0x2967)

    label("loc_DBA")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_8_C11 end

    def Function_9_DC2(): pass

    label("Function_9_DC2")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05有一个看似可以拉动的控制杆。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E75")

    Menu(
        0,
        10,
        100,
        1,
        (
            "拉下控制杆\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    Jump("loc_E25")

    label("loc_E25")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E72")
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x104)
    OP_22(0x6C, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x2966)

    label("loc_E72")

    Jump("loc_EE5")

    label("loc_E75")


    Menu(
        0,
        10,
        100,
        1,
        (
            "恢复到起始位置\x01",      # 0
            "放弃\x01",                # 1
        )
    )

    Jump("loc_E98")

    label("loc_E98")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE5")
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x0)
    OP_6F(0x4, 260)
    OP_70(0x4, 0x0)
    OP_22(0x6C, 0x0, 0x64)
    OP_73(0x4)
    OP_A3(0x2966)

    label("loc_EE5")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_9_DC2 end

    SaveToFile()

Try(main)
