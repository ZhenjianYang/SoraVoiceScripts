from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5513   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5513.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        '阿加特',                               # 9
        '马面兽王',                             # 10
        '马面兽王',                             # 11
        '封印石? ',                             # 12
        ' ',                                    # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT06/CH20137 ._CH',             # 00
        'ED6_DT07/CH00151 ._CH',             # 01
        'ED6_DT29/CH14750 ._CH',             # 02
        'ED6_DT29/CH14751 ._CH',             # 03
        'ED6_DT29/CH14530 ._CH',             # 04
        'ED6_DT29/CH14531 ._CH',             # 05
        'ED6_DT29/CH14540 ._CH',             # 06
        'ED6_DT29/CH14541 ._CH',             # 07
        'ED6_DT29/CH14770 ._CH',             # 08
        'ED6_DT29/CH14771 ._CH',             # 09
        'ED6_DT26/CH20621 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT06/CH20137P._CP',             # 00
        'ED6_DT07/CH00151P._CP',             # 01
        'ED6_DT29/CH14750P._CP',             # 02
        'ED6_DT29/CH14751P._CP',             # 03
        'ED6_DT29/CH14530P._CP',             # 04
        'ED6_DT29/CH14531P._CP',             # 05
        'ED6_DT29/CH14540P._CP',             # 06
        'ED6_DT29/CH14541P._CP',             # 07
        'ED6_DT29/CH14770P._CP',             # 08
        'ED6_DT29/CH14771P._CP',             # 09
        'ED6_DT26/CH20621P._CP',             # 0A
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x49,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 10370,
        Z                   = 0,
        Y                   = -15200,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32070,
        Z                   = 1250,
        Y                   = -36200,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22310,
        Z                   = 0,
        Y                   = -34560,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 73450,
        TriggerZ            = 0,
        TriggerY            = -73160,
        TriggerRange        = 1000,
        ActorX              = 73450,
        ActorZ              = 2000,
        ActorY              = -73160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 32950,
        TriggerZ            = 0,
        TriggerY            = -13410,
        TriggerRange        = 1000,
        ActorX              = 32950,
        ActorZ              = 1000,
        ActorY              = -13410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71300,
        TriggerZ            = 0,
        TriggerY            = 13500,
        TriggerRange        = 1000,
        ActorX              = 71500,
        ActorZ              = 3000,
        ActorY              = 14500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_262",          # 00, 0
        "Function_1_297",          # 01, 1
        "Function_2_33E",          # 02, 2
        "Function_3_464",          # 03, 3
        "Function_4_650",          # 04, 4
        "Function_5_6A9",          # 05, 5
        "Function_6_6C0",          # 06, 6
        "Function_7_6D1",          # 07, 7
        "Function_8_1111",         # 08, 8
        "Function_9_1933",         # 09, 9
        "Function_10_1957",        # 0A, 10
        "Function_11_1980",        # 0B, 11
        "Function_12_19A9",        # 0C, 12
        "Function_13_19D2",        # 0D, 13
        "Function_14_1A27",        # 0E, 14
        "Function_15_1A8F",        # 0F, 15
        "Function_16_1AF7",        # 10, 16
        "Function_17_1D8F",        # 11, 17
        "Function_18_1E03",        # 12, 18
        "Function_19_2007",        # 13, 19
        "Function_20_20C0",        # 14, 20
    )


    def Function_0_262(): pass

    label("Function_0_262")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_296")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_296")

    Return()

    # Function_0_262 end

    def Function_1_297(): pass

    label("Function_1_297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A8")
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x8A, 0x0)

    label("loc_2A8")

    OP_82(0x8B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2BB")
    OP_82(0x8C, 0x0)
    Jump("loc_2BE")

    label("loc_2BB")

    OP_82(0x8D, 0x0)

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D0")
    OP_6F(0x1B, 0)
    Jump("loc_2D7")

    label("loc_2D0")

    OP_6F(0x1B, 60)

    label("loc_2D7")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31D")
    OP_43(0x14, 0x0, 0x0, 0x3)
    Jump("loc_33D")

    label("loc_31D")

    OP_44(0x14, 0x3)
    OP_24(0x10D, 0x0)
    OP_23(0x10D)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)

    label("loc_33D")

    Return()

    # Function_1_297 end

    def Function_2_33E(): pass

    label("Function_2_33E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_423")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15F, 1)"), scpexpr(EXPR_END)), "loc_3B2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x5F\x01\x07\x00。\x02",
    )

    Jump("loc_397")

    label("loc_397")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29D8)
    Jump("loc_420")

    label("loc_3B2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x5F\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x5F\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_401")

    label("loc_401")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1B, 60)
    OP_70(0x1B, 0x0)

    label("loc_420")

    Jump("loc_456")

    label("loc_423")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_456")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_33E end

    def Function_3_464(): pass

    label("Function_3_464")

    OP_44(0x14, 0x3)
    OP_24(0x10D, 0x0)
    OP_23(0x10D)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    Call(0, 4)
    OP_43(0x14, 0x3, 0x0, 0x5)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x80, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x81, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x82, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x83, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x84, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x85, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x86, 0x1, 0x44C)
    Call(0, 4)
    Return()

    # Function_3_464 end

    def Function_4_650(): pass

    label("Function_4_650")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_675"),
        (1, "loc_678"),
        (2, "loc_680"),
        (3, "loc_688"),
        (4, "loc_690"),
        (5, "loc_698"),
        (SWITCH_DEFAULT, "loc_6A0"),
    )


    label("loc_675")

    Jump("loc_6A8")

    label("loc_678")

    Sleep(500)
    Jump("loc_6A8")

    label("loc_680")

    Sleep(1000)
    Jump("loc_6A8")

    label("loc_688")

    Sleep(1500)
    Jump("loc_6A8")

    label("loc_690")

    Sleep(2000)
    Jump("loc_6A8")

    label("loc_698")

    Sleep(2500)
    Jump("loc_6A8")

    label("loc_6A0")

    Sleep(3000)
    Jump("loc_6A8")

    label("loc_6A8")

    Return()

    # Function_4_650 end

    def Function_5_6A9(): pass

    label("Function_5_6A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BF")
    OP_22(0x10D, 0x0, 0x64)
    Sleep(7000)
    Jump("Function_5_6A9")

    label("loc_6BF")

    Return()

    # Function_5_6A9 end

    def Function_6_6C0(): pass

    label("Function_6_6C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 5)), scpexpr(EXPR_END)), "loc_6C8")
    Return()

    label("loc_6C8")

    Call(0, 7)
    Call(0, 8)
    Return()

    # Function_6_6C0 end

    def Function_7_6D1(): pass

    label("Function_7_6D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    OP_E0(238, 0x4B, 0x2)
    OP_E0(238, 0x4C, 0x3)
    OP_E0(239, 0x4D, 0x2)
    OP_E0(239, 0x4E, 0x3)
    OP_E0(240, 0x4F, 0x2)
    OP_E0(240, 0x50, 0x3)
    OP_E0(241, 0x51, 0x2)
    OP_E0(241, 0x52, 0x3)
    SetChrPos(0x109, 70870, 0, -30370, 0)
    SetChrPos(0x102, 72150, 0, -30500, 0)
    SetChrPos(0xF0, 70630, 0, -31920, 0)
    SetChrPos(0xF1, 72050, 0, -31950, 0)
    OP_6D(72310, 0, -29470, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(45000, 0)
    OP_6E(279, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81B")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_882")

    label("loc_81B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_843")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_882")

    label("loc_843")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_882")

    label("loc_86B")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_882")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AF")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_916")

    label("loc_8AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D7")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_916")

    label("loc_8D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_916")

    label("loc_8FF")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_916")

    Sleep(1000)

    def lambda_921():
        OP_6D(72800, 2200, -17770, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_921)

    def lambda_939():
        OP_67(0, 5700, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_939)

    def lambda_951():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_951)

    def lambda_961():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_961)

    def lambda_971():
        OP_6E(299, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_971)
    WaitChrThread(0xEE, 0x2)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 71340, 2100, -19250, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 69800, 2000, -17200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, 73320, 2000, -17200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_A48():
        OP_6B(2420, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A48)
    OP_22(0x85, 0x1, 0x64)

    def lambda_A5D():

        label("loc_A5D")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_A5D")

    QueueWorkItem2(0x109, 0, lambda_A5D)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x20)
    SetChrPos(0x10, 71340, -1000, -19250, 180)
    SetChrSubChip(0x10, 0)
    OP_43(0x10, 0x0, 0x0, 0xD)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 69800, -2000, -17200, 180)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x11, 0x0, 0x0, 0xE)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 73320, -2000, -17200, 180)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x12, 0x0, 0x0, 0xF)
    WaitChrThread(0x10, 0x0)
    OP_1D(0xC4)
    Fade(1000)
    OP_44(0x109, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    ClearChrFlags(0x10, 0x20)
    Sleep(500)
    OP_23(0x85)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #3
        0x10,
        "#557F#5P………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6E")

    ChrTalk(    #4
        0x107,
        "#065F#1P啊……！\x02",
    )

    CloseMessageWindow()

    label("loc_B6E")


    ChrTalk(    #5
        0x102,
        "#1506F#1P阿加特兄……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(72600, 1250, -22740, 0)
    OP_67(0, 3720, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)
    OP_43(0x109, 0x0, 0x0, 0x9)
    OP_43(0x102, 0x0, 0x0, 0xA)
    OP_43(0xF0, 0x0, 0x0, 0xB)
    OP_43(0xF1, 0x0, 0x0, 0xC)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C41")

    ChrTalk(    #6
        0x105,
        "#1163F#12P阿加特大哥……\x02",
    )

    CloseMessageWindow()

    label("loc_C41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C90")

    ChrTalk(    #7
        0x10A,
        (
            "#1316F#12P唉……\x01",
            "这次的对手竟然是阿加特前辈吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD5")

    label("loc_C90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD5")

    ChrTalk(    #8
        0x10B,
        (
            "#413F#12P呜呜……\x01",
            "对手是那个重剑男子吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D17")

    ChrTalk(    #9
        0x108,
        (
            "#070F#12P呵呵……\x01",
            "看来这可是强敌啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5B")

    label("loc_D17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5B")

    ChrTalk(    #10
        0x103,
        (
            "#1534F#12P哎呀哎呀……\x01",
            "出现麻烦人物了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D99")

    ChrTalk(    #11
        0x104,
        (
            "#1541F#12P呼……\x01",
            "浑身散发着野性呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEB")

    ChrTalk(    #12
        0x10D,
        (
            "#277F#12P『重剑』阿加特……\x01",
            "看来是相当了得的对手啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E30")

    label("loc_DEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E30")

    ChrTalk(    #13
        0x10E,
        (
            "#178F#12P『重剑』阿加特……\x01",
            "当对手足够了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EEC")

    ChrTalk(    #14
        0x109,
        (
            "#1065F#5P……看来，\x01",
            "会是一场相当艰苦的战斗啊。\x02\x03",

            "#1069F提妲！\x01",
            "加油哦！\x02\x03",

            "要打赢他，\x01",
            "亲手将阿加特夺回来！\x02",
        )
    )

    Jump("loc_ECA")

    label("loc_ECA")

    CloseMessageWindow()

    ChrTalk(    #15
        0x107,
        "#062F#12P是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_F9F")

    label("loc_EEC")


    ChrTalk(    #16
        0x109,
        (
            "#1065F#5P……看来，\x01",
            "会是一场相当艰苦的战斗啊。\x02\x03",

            "#1069F大家都要鼓足劲头哦！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(430, 240, -1, -1)
    SetChrName("伙伴们")

    AnonymousTalk(    #17
        "\x07\x00#4S是！\x02",
    )

    Jump("loc_F82")

    label("loc_F82")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_F9F")

    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_FB3():
        OP_6D(72200, 1050, -23340, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FB3)

    def lambda_FCB():
        OP_67(0, 5330, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FCB)

    def lambda_FE3():
        OP_6B(2440, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_FE3)

    def lambda_FF3():
        OP_6E(300, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FF3)
    SetChrChipByIndex(0x10, 1)

    def lambda_1008():
        OP_8F(0xFE, 0x117B0, 0x0, 0xFFFF9FAC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1008)

    def lambda_1023():
        OP_8F(0xFE, 0x1162A, 0x1F4, 0xFFFFA628, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1023)
    Sleep(10)

    def lambda_1043():
        OP_8F(0xFE, 0x11B3E, 0xFA, 0xFFFFA4B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1043)
    Sleep(10)
    SetChrChipByIndex(0x11, 9)

    def lambda_1068():

        label("loc_1068")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_1068")

    QueueWorkItem2(0x11, 3, lambda_1068)

    def lambda_107B():
        OP_8F(0xFE, 0x1121A, 0x3E8, 0xFFFFA9AC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_107B)

    def lambda_1096():
        OP_8F(0xFE, 0x1162A, 0x1F4, 0xFFFFA628, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1096)
    Sleep(10)
    SetChrChipByIndex(0x12, 9)

    def lambda_10BB():

        label("loc_10BB")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_10BB")

    QueueWorkItem2(0x12, 3, lambda_10BB)

    def lambda_10CE():
        OP_8F(0xFE, 0x11AF8, 0x3E8, 0xFFFFA8C6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_10CE)

    def lambda_10E9():
        OP_8F(0xFE, 0x11B3E, 0xFA, 0xFFFFA4B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_10E9)
    WaitChrThread(0x109, 0x1)
    Battle(0x1A5, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_7_6D1 end

    def Function_8_1111(): pass

    label("Function_8_1111")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x109, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    OP_E0(238, 0x4B, 0x2)
    OP_E0(238, 0x4C, 0x3)
    OP_E0(239, 0x4D, 0x2)
    OP_E0(239, 0x4E, 0x3)
    OP_E0(240, 0x4F, 0x2)
    OP_E0(240, 0x50, 0x3)
    OP_E0(241, 0x51, 0x2)
    OP_E0(241, 0x52, 0x3)
    SetChrPos(0xEE, 70690, 0, -24800, 0)
    SetChrPos(0xEF, 72070, 0, -25030, 0)
    SetChrPos(0xF0, 70250, 0, -26400, 0)
    SetChrPos(0xF1, 71930, 0, -26490, 0)
    SetChrChipByIndex(0xEE, 11)
    SetChrSubChip(0xEE, 0)
    SetChrChipByIndex(0xEF, 13)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 15)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 17)
    SetChrSubChip(0xF1, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    OP_6D(73050, 1000, -21630, 0)
    OP_67(0, 3960, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(315, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, 71340, 3200, -19250, 0)
    PlayEffect(0x7, 0x7, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)

    def lambda_1353():
        OP_6D(71930, 1550, -21000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1353)

    def lambda_136B():
        OP_67(0, 3460, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_136B)

    def lambda_1383():
        OP_6B(2820, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1383)

    def lambda_1393():
        OP_6E(347, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1393)
    OP_8E(0x109, 0x11648, 0x7D0, 0xFFFFB028, 0x7D0, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x13, 0x11684, 0xCE4, 0xFFFFB1CC, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x13, 0x80)
    OP_0D()
    Sleep(150)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00得到了\x1F\x5C\x03\x07\x00。\x02",
    )

    Jump("loc_142B")

    label("loc_142B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x35C, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #19
        0x109,
        (
            "#1075F#5P呼……\x01",
            "这样就行啦。\x02\x03",

            "#1840F话说回来……\x01",
            "实在是很强啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1571")

    ChrTalk(    #20
        0x107,
        (
            "#560F#11P这、这样阿加特大哥哥就……\x02\x03",

            "#067F凯文哥哥！\x01",
            "赶快回庭院吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #21
        0x109,
        "#1066F#5P知道啦知道啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#1501F#11P哈哈……\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185E")

    label("loc_1571")


    ChrTalk(    #23
        0x102,
        (
            "#1513F#11P嗯……\x01",
            "实在是难对付呢。\x02\x03",

            "#1500F不过这样……\x01",
            "就能解放阿加特兄了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1624")

    ChrTalk(    #24
        0x10A,
        (
            "#819F#11P嘿嘿……\x01",
            "提妲还在等着呢，\x01",
            "得赶快回庭院才行啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185E")

    label("loc_1624")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1678")

    ChrTalk(    #25
        0x103,
        (
            "#1536F#11P呵呵……\x01",
            "提妲还在等着呢，\x01",
            "得赶快回庭院才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185E")

    label("loc_1678")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C8")

    ChrTalk(    #26
        0x105,
        (
            "#1168F#11P呵呵……\x01",
            "提妲还在等着呢，\x01",
            "赶快回庭院吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185E")

    label("loc_16C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1717")

    ChrTalk(    #27
        0x10E,
        (
            "#171F#11P呵呵……\x01",
            "提妲还在等着呢，\x01",
            "赶快回庭院吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185E")

    label("loc_1717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1767")

    ChrTalk(    #28
        0x104,
        (
            "#1541F#11P呼……\x01",
            "小提妲还在等着呢，\x01",
            "赶快回庭院吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185E")

    label("loc_1767")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17BC")

    ChrTalk(    #29
        0x108,
        (
            "#071F#11P哈哈……　\x01",
            "小姑娘也在等着呢，\x01",
            "咱们快回庭院吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185E")

    label("loc_17BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1812")

    ChrTalk(    #30
        0x10B,
        (
            "#211F#11P哎呀，那个小不点还在等着呢，\x01",
            "咱们马上回庭院吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185E")

    label("loc_1812")

    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #31
        0x109,
        (
            "#1065F#5P嗯……\x01",
            "提妲也在等着呢，\x01",
            "我们马上回庭院吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185E")

    OP_A2(0x290D)
    OP_28(0x34, 0x1, 0x4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(71500, 2000, -20000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 71500, 2000, -20000, 180)
    SetChrPos(0x1, 71500, 2000, -20000, 180)
    SetChrPos(0x2, 71500, 2000, -20000, 180)
    SetChrPos(0x3, 71500, 2000, -20000, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_8_1111 end

    def Function_9_1933(): pass

    label("Function_9_1933")

    OP_8E(0xFE, 0x11418, 0x0, 0xFFFF973C, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_9_1933 end

    def Function_10_1957(): pass

    label("Function_10_1957")

    Sleep(100)
    OP_8E(0xFE, 0x119C2, 0x0, 0xFFFF96E2, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_10_1957 end

    def Function_11_1980(): pass

    label("Function_11_1980")

    Sleep(24)
    OP_8E(0xFE, 0x11288, 0x0, 0xFFFF9048, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_11_1980 end

    def Function_12_19A9(): pass

    label("Function_12_19A9")

    Sleep(330)
    OP_8E(0xFE, 0x11A62, 0x0, 0xFFFF90CA, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_19A9 end

    def Function_13_19D2(): pass

    label("Function_13_19D2")

    PlayEffect(0x1, 0x3, 0xFF, 71340, 2100, -19250, 0, 0, 0, 600, 700, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x3, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_19D2 end

    def Function_14_1A27(): pass

    label("Function_14_1A27")

    PlayEffect(0x1, 0x4, 0xFF, 69800, 2000, -17200, 0, 0, 0, 800, 900, 800, 0xFF, 0, 0, 0, 0)

    def lambda_1A62():

        label("loc_1A62")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1A62")

    QueueWorkItem2(0xFE, 3, lambda_1A62)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x578, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_14_1A27 end

    def Function_15_1A8F(): pass

    label("Function_15_1A8F")

    PlayEffect(0x1, 0x5, 0xFF, 73320, 2000, -17200, 0, 0, 0, 800, 900, 800, 0xFF, 0, 0, 0, 0)

    def lambda_1ACA():

        label("loc_1ACA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1ACA")

    QueueWorkItem2(0xFE, 3, lambda_1ACA)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x578, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_15_1A8F end

    def Function_16_1AF7(): pass

    label("Function_16_1AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC6")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(3584)
    Sleep(500)
    Jump("loc_1BC9")

    label("loc_1BC6")

    TalkBegin(0xFF)

    label("loc_1BC9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #32
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_1BF3")

    label("loc_1BF3")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D5E")

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

    Jump("loc_1C58")

    label("loc_1C58")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C75"),
        (1, "loc_1CF0"),
        (2, "loc_1D1F"),
        (SWITCH_DEFAULT, "loc_1D4E"),
    )


    label("loc_1C75")

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
    OP_1D(0xE8)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D5B")

    label("loc_1CF0")

    OP_A9(0x21)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #33
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_1D1C")

    label("loc_1D1C")

    Jump("loc_1D5B")

    label("loc_1D1F")

    OP_A9(0x7)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #34
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_1D4B")

    label("loc_1D4B")

    Jump("loc_1D5B")

    label("loc_1D4E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D5B")

    label("loc_1D5B")

    Jump("loc_1C06")

    label("loc_1D5E")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8B")
    OP_A2(0x2591)
    EventEnd(0x1)
    Jump("loc_1D8E")

    label("loc_1D8B")

    TalkEnd(0xFF)

    label("loc_1D8E")

    Return()

    # Function_16_1AF7 end

    def Function_17_1D8F(): pass

    label("Function_17_1D8F")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_1DEC")

    label("loc_1DEC")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_17_1D8F end

    def Function_18_1E03(): pass

    label("Function_18_1E03")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 72240, 0, 12500, 0)
    SetChrPos(0x1, 70570, 0, 12430, 0)
    SetChrPos(0x2, 71940, 0, 10790, 0)
    SetChrPos(0x3, 70470, 0, 10730, 0)
    OP_6D(71160, 0, 12790, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3780, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED9")
    OP_28(0xC, 0x4, 0x2)
    OP_82(0x8C, 0x2)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_1ED9")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #36
        (
            "\x07\x05#40W    『食』乃万物之本……\x01",
            "　　  若要踏上正途\x01",
            "    『食』亦不可或缺。\x01",
            "#500W\x01",
            "#40W   汝等所掌握之『食之形态』\x01",
            "　  　  达２０种时，\x01",
            " 　   则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x25, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1FFB")
    Call(0, 17)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FF8")
    Call(0, 19)

    label("loc_1FF8")

    Jump("loc_1FFB")

    label("loc_1FFB")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_18_1E03 end

    def Function_19_2007(): pass

    label("Function_19_2007")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x8B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1D, 0)
    OP_70(0x1D, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1D)
    Sleep(500)

    def lambda_2070():
        OP_6B(3280, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2070)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_23(0x85)
    OP_E3(0x0, 0xD, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_2007 end

    def Function_20_20C0(): pass

    label("Function_20_20C0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 72240, 0, 12500, 0)
    SetChrPos(0x1, 70570, 0, 12430, 0)
    SetChrPos(0x2, 71940, 0, 10790, 0)
    SetChrPos(0x3, 70470, 0, 10730, 0)
    OP_6D(71160, 0, 12790, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3780, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_20_20C0 end

    SaveToFile()

Try(main)
