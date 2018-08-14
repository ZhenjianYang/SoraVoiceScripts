from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U2513   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U2513.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        'ED6_DT29/CH15140 ._CH',             # 00
        'ED6_DT29/CH15141 ._CH',             # 01
        'ED6_DT29/CH14650 ._CH',             # 02
        'ED6_DT29/CH14651 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT29/CH15140P._CP',             # 00
        'ED6_DT29/CH15141P._CP',             # 01
        'ED6_DT29/CH14650P._CP',             # 02
        'ED6_DT29/CH14651P._CP',             # 03
    )

    DeclMonster(
        X                   = 8070,
        Z                   = 4000,
        Y                   = 10260,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 11092,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36570,
        Z                   = 1000,
        Y                   = 9550,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x272,
        Unknown_18          = 11093,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -470,
        Z                   = 0,
        Y                   = 3310,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x270,
        Unknown_18          = 11094,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8070,
        Z                   = 4000,
        Y                   = 10260,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x270,
        Unknown_18          = 11092,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36570,
        Z                   = 1000,
        Y                   = 9550,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x270,
        Unknown_18          = 11093,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -470,
        Z                   = 0,
        Y                   = 3310,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x270,
        Unknown_18          = 11094,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x20,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -65519,
        TriggerZ            = 1000,
        TriggerY            = 10110,
        TriggerRange        = 1000,
        ActorX              = -65519,
        ActorZ              = 2000,
        ActorY              = 10110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1B6",          # 00, 0
        "Function_1_238",          # 01, 1
        "Function_2_2EB",          # 02, 2
        "Function_3_40B",          # 03, 3
        "Function_4_45A",          # 04, 4
        "Function_5_4B3",          # 05, 5
        "Function_6_50C",          # 06, 6
    )


    def Function_0_1B6(): pass

    label("Function_0_1B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1CB")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 6)

    label("loc_1CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_END)), "loc_1E4")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_217")

    label("loc_1E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_217")

    label("loc_1FE")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x12, 0x80)

    label("loc_217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_237")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 4)), scpexpr(EXPR_END)), "loc_22B")
    SetChrFlags(0x10, 0x80)

    label("loc_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 5)), scpexpr(EXPR_END)), "loc_237")
    SetChrFlags(0x11, 0x80)

    label("loc_237")

    Return()

    # Function_0_1B6 end

    def Function_1_238(): pass

    label("Function_1_238")

    OP_B1("U2513_n")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x271), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x272), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_273")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_273")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x270), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F")
    Event(0, 4)

    label("loc_29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 6)), scpexpr(EXPR_END)), "loc_2D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 7)), scpexpr(EXPR_END)), "loc_2B4")
    Event(0, 5)
    Jump("loc_2D1")

    label("loc_2B4")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_A3(0x2B54)
    OP_A3(0x2B55)
    OP_A3(0x2B56)

    label("loc_2D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x574, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E3")
    OP_6F(0x6, 0)
    Jump("loc_2EA")

    label("loc_2E3")

    OP_6F(0x6, 60)

    label("loc_2EA")

    Return()

    # Function_1_238 end

    def Function_2_2EB(): pass

    label("Function_2_2EB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x574, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4A6, 1)"), scpexpr(EXPR_END)), "loc_35D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xA6\x04\x07\x00。\x02",
    )

    Jump("loc_342")

    label("loc_342")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BA6)
    Jump("loc_3C9")

    label("loc_35D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xA6\x04\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xA6\x04\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3AA")

    label("loc_3AA")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_3C9")

    Jump("loc_3FD")

    label("loc_3CC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3FD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2EB end

    def Function_3_40B(): pass

    label("Function_3_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 7)), scpexpr(EXPR_END)), "loc_437")
    OP_C0(0x1F, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_459")

    label("loc_437")

    OP_C0(0x1F, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    label("loc_459")

    Return()

    # Function_3_40B end

    def Function_4_45A(): pass

    label("Function_4_45A")

    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A3(0x2B54)
    OP_A3(0x2B55)
    OP_A3(0x2B56)
    OP_A2(0x2B57)
    OP_28(0x37, 0x1, 0x20)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2513   ._SN", 100, 0, 1)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_4_45A end

    def Function_5_4B3(): pass

    label("Function_5_4B3")

    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A3(0x2B54)
    OP_A3(0x2B55)
    OP_A3(0x2B56)
    OP_A3(0x2B57)
    OP_28(0x37, 0x1, 0x40)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2513   ._SN", 100, 0, 1)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_4B3 end

    def Function_6_50C(): pass

    label("Function_6_50C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_551")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_551")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2506)
    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    label("loc_551")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D7")
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, 8070, 4000, 10260, 180)
    SetChrPos(0x1, 8070, 4000, 10260, 180)
    SetChrPos(0x2, 8070, 4000, 10260, 180)
    SetChrPos(0x3, 8070, 4000, 10260, 180)
    OP_69(0x0, 0x0)
    Jump("loc_6E0")

    label("loc_5D7")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65D")
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -36570, 1000, 9550, 180)
    SetChrPos(0x1, -36570, 1000, 9550, 180)
    SetChrPos(0x2, -36570, 1000, 9550, 180)
    SetChrPos(0x3, -36570, 1000, 9550, 180)
    OP_69(0x0, 0x0)
    Jump("loc_6E0")

    label("loc_65D")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E0")
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -470, 0, 3310, 180)
    SetChrPos(0x1, -470, 0, 3310, 180)
    SetChrPos(0x2, -470, 0, 3310, 180)
    SetChrPos(0x3, -470, 0, 3310, 180)
    OP_69(0x0, 0x0)

    label("loc_6E0")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_50C end

    SaveToFile()

Try(main)
