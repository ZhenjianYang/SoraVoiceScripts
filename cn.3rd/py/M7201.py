from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7201   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60223",
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
        'ED6_DT29/CH14470 ._CH',             # 00
        'ED6_DT29/CH14471 ._CH',             # 01
        'ED6_DT29/CH15050 ._CH',             # 02
        'ED6_DT29/CH15051 ._CH',             # 03
        'ED6_DT29/CH15060 ._CH',             # 04
        'ED6_DT29/CH15061 ._CH',             # 05
        'ED6_DT29/CH14480 ._CH',             # 06
        'ED6_DT29/CH14481 ._CH',             # 07
        'ED6_DT29/CH14490 ._CH',             # 08
        'ED6_DT29/CH14491 ._CH',             # 09
        'ED6_DT29/CH14560 ._CH',             # 0A
        'ED6_DT29/CH14561 ._CH',             # 0B
        'ED6_DT29/CH14010 ._CH',             # 0C
        'ED6_DT29/CH14011 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH14470P._CP',             # 00
        'ED6_DT29/CH14471P._CP',             # 01
        'ED6_DT29/CH15050P._CP',             # 02
        'ED6_DT29/CH15051P._CP',             # 03
        'ED6_DT29/CH15060P._CP',             # 04
        'ED6_DT29/CH15061P._CP',             # 05
        'ED6_DT29/CH14480P._CP',             # 06
        'ED6_DT29/CH14481P._CP',             # 07
        'ED6_DT29/CH14490P._CP',             # 08
        'ED6_DT29/CH14491P._CP',             # 09
        'ED6_DT29/CH14560P._CP',             # 0A
        'ED6_DT29/CH14561P._CP',             # 0B
        'ED6_DT29/CH14010P._CP',             # 0C
        'ED6_DT29/CH14011P._CP',             # 0D
    )

    DeclMonster(
        X                   = -33960,
        Z                   = 750,
        Y                   = 20090,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 29720,
        Z                   = -7200,
        Y                   = 31730,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 29210,
        Z                   = -6800,
        Y                   = 44130,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1FA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -120,
        Z                   = -3200,
        Y                   = 34110,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -130,
        Z                   = 750,
        Y                   = 81960,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -140,
        TriggerZ            = 4800,
        TriggerY            = 131920,
        TriggerRange        = 1000,
        ActorX              = -140,
        ActorZ              = 6800,
        ActorY              = 131920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -34000,
        TriggerZ            = 750,
        TriggerY            = 20000,
        TriggerRange        = 1000,
        ActorX              = -34000,
        ActorZ              = 1750,
        ActorY              = 20000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = -2800,
        TriggerY            = 19000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -1800,
        ActorY              = 19000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41650,
        TriggerZ            = 750,
        TriggerY            = 81800,
        TriggerRange        = 1000,
        ActorX              = -41650,
        ActorZ              = 1750,
        ActorY              = 81800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_236",          # 00, 0
        "Function_1_2AB",          # 01, 1
        "Function_2_355",          # 02, 2
        "Function_3_47B",          # 03, 3
        "Function_4_5D2",          # 04, 4
        "Function_5_6F8",          # 05, 5
        "Function_6_804",          # 06, 6
        "Function_7_A9C",          # 07, 7
        "Function_8_B7A",          # 08, 8
        "Function_9_C58",          # 09, 9
        "Function_10_D36",         # 0A, 10
        "Function_11_E14",         # 0B, 11
        "Function_12_EF2",         # 0C, 12
        "Function_13_FD0",         # 0D, 13
        "Function_14_10AE",        # 0E, 14
        "Function_15_116A",        # 0F, 15
        "Function_16_1226",        # 10, 16
        "Function_17_12E2",        # 11, 17
        "Function_18_139E",        # 12, 18
        "Function_19_145A",        # 13, 19
        "Function_20_1516",        # 14, 20
        "Function_21_15D2",        # 15, 21
        "Function_22_16E8",        # 16, 22
    )


    def Function_0_236(): pass

    label("Function_0_236")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_297")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_266"),
        (101, "loc_26D"),
        (102, "loc_274"),
        (103, "loc_27B"),
        (104, "loc_282"),
        (105, "loc_289"),
        (106, "loc_290"),
        (SWITCH_DEFAULT, "loc_297"),
    )


    label("loc_266")

    Event(0, 7)
    Jump("loc_297")

    label("loc_26D")

    Event(0, 12)
    Jump("loc_297")

    label("loc_274")

    Event(0, 11)
    Jump("loc_297")

    label("loc_27B")

    Event(0, 8)
    Jump("loc_297")

    label("loc_282")

    Event(0, 9)
    Jump("loc_297")

    label("loc_289")

    Event(0, 10)
    Jump("loc_297")

    label("loc_290")

    Event(0, 13)
    Jump("loc_297")

    label("loc_297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2AA")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_2AA")

    Return()

    # Function_0_236 end

    def Function_1_2AB(): pass

    label("Function_1_2AB")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFF63C0, 0x23008C)
    OP_1B(0x0, 0x0, 0xE)
    OP_1B(0x1, 0x0, 0x13)
    OP_1B(0x2, 0x0, 0x12)
    OP_1B(0x3, 0x0, 0xF)
    OP_1B(0x4, 0x0, 0x10)
    OP_1B(0x5, 0x0, 0x11)
    OP_1B(0x6, 0x0, 0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_2ED")
    OP_71(0x402, 0x0)
    ExitThread()

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_2FE")

    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B")
    OP_6F(0x5, 0)
    Jump("loc_322")

    label("loc_31B")

    OP_6F(0x5, 60)

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_334")
    OP_6F(0x6, 0)
    Jump("loc_33B")

    label("loc_334")

    OP_6F(0x6, 60)

    label("loc_33B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34D")
    OP_6F(0x7, 0)
    Jump("loc_354")

    label("loc_34D")

    OP_6F(0x7, 60)

    label("loc_354")

    Return()

    # Function_1_2AB end

    def Function_2_355(): pass

    label("Function_2_355")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x581, 1)"), scpexpr(EXPR_END)), "loc_3C9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x81\x05\x07\x00。\x02",
    )

    Jump("loc_3AE")

    label("loc_3AE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A88)
    Jump("loc_437")

    label("loc_3C9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x81\x05\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x81\x05\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_418")

    label("loc_418")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_437")

    Jump("loc_46D")

    label("loc_43A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_46D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_355 end

    def Function_3_47B(): pass

    label("Function_3_47B")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x1E)
    OP_73(0x6)
    OP_6F(0x6, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #3
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×２００\x01",
            "\x07\x02#57I水之耀晶片×２００\x01",
            "\x07\x02#58I火之耀晶片×２００\x01",
            "\x07\x02#59I风之耀晶片×２００\x01",
            "\x07\x02#62I时之耀晶片×２００\x01",
            "\x07\x02#60I空之耀晶片×２００\x01",
            "\x07\x02#61I幻之耀晶片×２００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2A89)
    Jump("loc_5C0")

    label("loc_5A4")


    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5C0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_47B end

    def Function_4_5D2(): pass

    label("Function_4_5D2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x476, 1)"), scpexpr(EXPR_END)), "loc_646")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\x76\x04\x07\x00。\x02",
    )

    Jump("loc_62B")

    label("loc_62B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A8A)
    Jump("loc_6B4")

    label("loc_646")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\x76\x04\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x76\x04\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_695")

    label("loc_695")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_6B4")

    Jump("loc_6EA")

    label("loc_6B7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6EA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5D2 end

    def Function_5_6F8(): pass

    label("Function_5_6F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xEE, 0x80)
    SetChrFlags(0xEF, 0x80)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(1680, 5200, 138300, 0)
    OP_67(0, 8970, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(45000, 0)
    OP_6E(428, 0)

    def lambda_75B():
        OP_6D(-300, 8100, 157570, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_75B)

    def lambda_773():
        OP_67(0, 1570, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_773)

    def lambda_78B():
        OP_6B(3620, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_78B)

    def lambda_79B():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_79B)

    def lambda_7AB():
        OP_6E(398, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7AB)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)
    Fade(1000)

    def lambda_7CF():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_7CF)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2505)
    OP_A2(0x2506)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_6F8 end

    def Function_6_804(): pass

    label("Function_6_804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D3")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(4096)
    Sleep(500)
    Jump("loc_8D6")

    label("loc_8D3")

    TalkBegin(0xFF)

    label("loc_8D6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #8
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_900")

    label("loc_900")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_913")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A6B")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_965")

    label("loc_965")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_982"),
        (1, "loc_9FD"),
        (2, "loc_A2C"),
        (SWITCH_DEFAULT, "loc_A5B"),
    )


    label("loc_982")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A68")

    label("loc_9FD")

    OP_A9(0x22)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #9
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_A29")

    label("loc_A29")

    Jump("loc_A68")

    label("loc_A2C")

    OP_A9(0x8)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #10
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_A58")

    label("loc_A58")

    Jump("loc_A68")

    label("loc_A5B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A68")

    label("loc_A68")

    Jump("loc_913")

    label("loc_A6B")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A98")
    OP_A2(0x2593)
    EventEnd(0x1)
    Jump("loc_A9B")

    label("loc_A98")

    TalkEnd(0xFF)

    label("loc_A9B")

    Return()

    # Function_6_804 end

    def Function_7_A9C(): pass

    label("Function_7_A9C")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -120, 820, -220, 180)
    SetChrPos(0x1, -120, 820, -220, 180)
    SetChrPos(0x2, -120, 820, -220, 180)
    SetChrPos(0x3, -120, 820, -220, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -120, 820, -220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_7_A9C end

    def Function_8_B7A(): pass

    label("Function_8_B7A")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 37790, -3260, 81910, 270)
    SetChrPos(0x1, 37790, -3260, 81910, 270)
    SetChrPos(0x2, 37790, -3260, 81910, 270)
    SetChrPos(0x3, 37790, -3260, 81910, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 37790, -3260, 81910, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_8_B7A end

    def Function_9_C58(): pass

    label("Function_9_C58")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -40110, -3580, 110020, 90)
    SetChrPos(0x1, -40110, -3580, 110020, 90)
    SetChrPos(0x2, -40110, -3580, 110020, 90)
    SetChrPos(0x3, -40110, -3580, 110020, 90)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -40110, -3580, 110020, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_9_C58 end

    def Function_10_D36(): pass

    label("Function_10_D36")

    OP_DE(0x0, 0x5, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 41500, 420, 109700, 270)
    SetChrPos(0x1, 41500, 420, 109700, 270)
    SetChrPos(0x2, 41500, 420, 109700, 270)
    SetChrPos(0x3, 41500, 420, 109700, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 41500, 420, 109700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_10_D36 end

    def Function_11_E14(): pass

    label("Function_11_E14")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 25800, 4820, 131950, 270)
    SetChrPos(0x1, 25800, 4820, 131950, 270)
    SetChrPos(0x2, 25800, 4820, 131950, 270)
    SetChrPos(0x3, 25800, 4820, 131950, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 25800, 4820, 131950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_11_E14 end

    def Function_12_EF2(): pass

    label("Function_12_EF2")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -26000, 4820, 132000, 90)
    SetChrPos(0x1, -26000, 4820, 132000, 90)
    SetChrPos(0x2, -26000, 4820, 132000, 90)
    SetChrPos(0x3, -26000, 4820, 132000, 90)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -26000, 4820, 132000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_12_EF2 end

    def Function_13_FD0(): pass

    label("Function_13_FD0")

    OP_DE(0x0, 0x6, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 110, 5370, 171840, 180)
    SetChrPos(0x1, 110, 5370, 171840, 180)
    SetChrPos(0x2, 110, 5370, 171840, 180)
    SetChrPos(0x3, 110, 5370, 171840, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 5370, 172000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_13_FD0 end

    def Function_14_10AE(): pass

    label("Function_14_10AE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -120, 820, -220, 0)
    SetChrPos(0x2, -120, 820, -220, 0)
    SetChrPos(0x1, -120, 820, -220, 0)
    SetChrPos(0x0, -120, 820, -220, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -120, 820, -220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7200   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_14_10AE end

    def Function_15_116A(): pass

    label("Function_15_116A")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 37790, -3260, 81910, 90)
    SetChrPos(0x2, 37790, -3260, 81910, 90)
    SetChrPos(0x1, 37790, -3260, 81910, 90)
    SetChrPos(0x0, 37790, -3260, 81910, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 37790, -3260, 81910, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7201   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_15_116A end

    def Function_16_1226(): pass

    label("Function_16_1226")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -40110, -3580, 110020, 270)
    SetChrPos(0x2, -40110, -3580, 110020, 270)
    SetChrPos(0x1, -40110, -3580, 110020, 270)
    SetChrPos(0x0, -40110, -3580, 110020, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -40110, -3580, 110020, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7201   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1226 end

    def Function_17_12E2(): pass

    label("Function_17_12E2")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 41500, 420, 109700, 90)
    SetChrPos(0x2, 41500, 420, 109700, 90)
    SetChrPos(0x1, 41500, 420, 109700, 90)
    SetChrPos(0x0, 41500, 420, 109700, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 41500, 420, 109700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7200   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_17_12E2 end

    def Function_18_139E(): pass

    label("Function_18_139E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 25800, 4820, 131950, 90)
    SetChrPos(0x2, 25800, 4820, 131950, 90)
    SetChrPos(0x1, 25800, 4820, 131950, 90)
    SetChrPos(0x0, 25800, 4820, 131950, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 25800, 4820, 131950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7200   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_18_139E end

    def Function_19_145A(): pass

    label("Function_19_145A")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -26000, 4820, 132000, 270)
    SetChrPos(0x2, -26000, 4820, 132000, 270)
    SetChrPos(0x1, -26000, 4820, 132000, 270)
    SetChrPos(0x0, -26000, 4820, 132000, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -26000, 4820, 132000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7200   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_19_145A end

    def Function_20_1516(): pass

    label("Function_20_1516")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 110, 5370, 171840, 0)
    SetChrPos(0x2, 110, 5370, 171840, 0)
    SetChrPos(0x1, 110, 5370, 171840, 0)
    SetChrPos(0x0, 110, 5370, 171840, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 5370, 172000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7202   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_1516 end

    def Function_21_15D2(): pass

    label("Function_21_15D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FB")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_15EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_15EF)

    label("loc_15FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1624")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1618():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1618)

    label("loc_1624")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_164D")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1641():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1641)

    label("loc_164D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1676")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_166A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_166A)

    label("loc_1676")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16A2")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_16A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B9")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_16B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D0")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_16D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E7")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_16E7")

    Return()

    # Function_21_15D2 end

    def Function_22_16E8(): pass

    label("Function_22_16E8")


    def lambda_16EE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_16EE)

    def lambda_1700():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1700)

    def lambda_1712():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1712)

    def lambda_1724():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1724)
    Sleep(1000)
    Return()

    # Function_22_16E8 end

    SaveToFile()

Try(main)
