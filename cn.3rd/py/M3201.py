from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3201   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3201.x',
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
        '凯诺娜',                               # 9
        '机枪特务兵',                           # 10
        '机枪特务兵',                           # 11
        '钩爪特务兵',                           # 12
        '钩爪特务兵',                           # 13
        '重装甲特务兵',                         # 14
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
        'ED6_DT27/CH03120 ._CH',             # 00
        'ED6_DT27/CH04120 ._CH',             # 01
        'ED6_DT06/CH20027 ._CH',             # 02
        'ED6_DT27/CH04124 ._CH',             # 03
        'ED6_DT27/CH04125 ._CH',             # 04
        'ED6_DT27/CH04126 ._CH',             # 05
        'ED6_DT07/CH00340 ._CH',             # 06
        'ED6_DT07/CH00342 ._CH',             # 07
        'ED6_DT07/CH00440 ._CH',             # 08
        'ED6_DT07/CH00441 ._CH',             # 09
        'ED6_DT07/CH00500 ._CH',             # 0A
        'ED6_DT07/CH00508 ._CH',             # 0B
        'ED6_DT07/CH00320 ._CH',             # 0C
        'ED6_DT07/CH00321 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT27/CH03120P._CP',             # 00
        'ED6_DT27/CH04120P._CP',             # 01
        'ED6_DT06/CH20027P._CP',             # 02
        'ED6_DT27/CH04124P._CP',             # 03
        'ED6_DT27/CH04125P._CP',             # 04
        'ED6_DT27/CH04126P._CP',             # 05
        'ED6_DT07/CH00340P._CP',             # 06
        'ED6_DT07/CH00342P._CP',             # 07
        'ED6_DT07/CH00440P._CP',             # 08
        'ED6_DT07/CH00441P._CP',             # 09
        'ED6_DT07/CH00500P._CP',             # 0A
        'ED6_DT07/CH00508P._CP',             # 0B
        'ED6_DT07/CH00320P._CP',             # 0C
        'ED6_DT07/CH00321P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -15320,
        Z                   = 0,
        Y                   = 870,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 43940,
        Z                   = 0,
        Y                   = 35180,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -42100,
        TriggerZ            = 0,
        TriggerY            = 15050,
        TriggerRange        = 1000,
        ActorX              = -42100,
        ActorZ              = 800,
        ActorY              = 15050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_236",          # 00, 0
        "Function_1_25C",          # 01, 1
        "Function_2_272",          # 02, 2
        "Function_3_375",          # 03, 3
        "Function_4_37E",          # 04, 4
        "Function_5_1C47",         # 05, 5
        "Function_6_1C96",         # 06, 6
        "Function_7_1CE5",         # 07, 7
        "Function_8_1D34",         # 08, 8
        "Function_9_1D83",         # 09, 9
        "Function_10_1DD2",        # 0A, 10
        "Function_11_2786",        # 0B, 11
    )


    def Function_0_236(): pass

    label("Function_0_236")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_25B")

    Return()

    # Function_0_236 end

    def Function_1_25C(): pass

    label("Function_1_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D")
    OP_72(0x1001, 0x0)
    ExitThread()
    Jump("loc_271")

    label("loc_26D")

    OP_64(0x0, 0x1)

    label("loc_271")

    Return()

    # Function_1_25C end

    def Function_2_272(): pass

    label("Function_2_272")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 0)), scpexpr(EXPR_END)), "loc_371")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_371")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "使用Ｂ－０１钥匙\x01",      # 0
            "不使用\x01",                # 1
        )
    )

    Jump("loc_317")

    label("loc_317")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_33D"),
        (SWITCH_DEFAULT, "loc_361"),
    )


    label("loc_33D")

    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_A2(0x2B1C)
    OP_71(0x1001, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36E")

    label("loc_361")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36E")

    label("loc_36E")

    Jump("loc_2E0")

    label("loc_371")

    TalkEnd(0xFF)
    Return()

    # Function_2_272 end

    def Function_3_375(): pass

    label("Function_3_375")

    Call(0, 4)
    Call(0, 10)
    Return()

    # Function_3_375 end

    def Function_4_37E(): pass

    label("Function_4_37E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x4E, 0x2)
    OP_E0(238, 0x4F, 0x3)
    OP_E0(239, 0x50, 0x2)
    OP_E0(239, 0x51, 0x3)
    OP_E0(240, 0x52, 0x2)
    OP_E0(240, 0x53, 0x3)
    OP_E0(241, 0x54, 0x2)
    OP_E0(241, 0x55, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 830, 0, 48770, 180)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, 450, 0, 38370, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45E")
    SetChrPos(0xEF, 1770, 0, 38220, 0)
    SetChrPos(0xF0, 0, 0, 36840, 0)
    SetChrPos(0xF1, 1800, 0, 36800, 0)
    Jump("loc_4E3")

    label("loc_45E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A2")
    SetChrPos(0xF0, 1770, 0, 38220, 0)
    SetChrPos(0xEF, 0, 0, 36840, 0)
    SetChrPos(0xF1, 1800, 0, 36800, 0)
    Jump("loc_4E3")

    label("loc_4A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E3")
    SetChrPos(0xF1, 1770, 0, 38220, 0)
    SetChrPos(0xEF, 0, 0, 36840, 0)
    SetChrPos(0xF0, 1800, 0, 36800, 0)

    label("loc_4E3")

    OP_6D(1970, 0, 38740, 0)
    OP_67(0, 6350, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(260, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #1
        0x10,
        "女人的声音",
        (
            "#4P阁下……\x01",
            "我正在等着您呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A7")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_60E")

    label("loc_5A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CF")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_60E")

    label("loc_5CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F7")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_60E")

    label("loc_5F7")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_60E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63B")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6A2")

    label("loc_63B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_663")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6A2")

    label("loc_663")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6A2")

    label("loc_68B")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6A2")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CF")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_736")

    label("loc_6CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F7")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_736")

    label("loc_6F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_736")

    label("loc_71F")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_736")

    Sleep(1000)
    Fade(500)
    OP_6D(2210, 0, 50140, 0)
    OP_67(0, 4660, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(45000, 0)
    OP_6E(264, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #2
        0x109,
        "#1064F#1P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10C,
        "#115F#1P是你吗……凯诺娜。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_7D1():
        OP_6D(2390, 0, 46240, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_7D1)

    def lambda_7E9():
        OP_67(0, 5010, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_7E9)

    def lambda_801():
        OP_6B(2310, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_801)

    def lambda_811():
        OP_6E(367, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_811)
    Sleep(1000)

    def lambda_826():
        OP_8F(0xFE, 0xD2, 0x0, 0xA69A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_826)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AC")

    def lambda_854():
        OP_8F(0xFE, 0x640, 0x0, 0xA668, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_854)
    Sleep(100)

    def lambda_874():
        OP_8F(0xFE, 0xFFFFFF1A, 0x0, 0x9FE2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_874)
    Sleep(100)

    def lambda_894():
        OP_8F(0xFE, 0x622, 0x0, 0xA032, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_894)
    Jump("loc_981")

    label("loc_8AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_918")

    def lambda_8C0():
        OP_8F(0xFE, 0x640, 0x0, 0xA668, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_8C0)
    Sleep(100)

    def lambda_8E0():
        OP_8F(0xFE, 0xFFFFFF1A, 0x0, 0x9FE2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_8E0)
    Sleep(100)

    def lambda_900():
        OP_8F(0xFE, 0x622, 0x0, 0xA032, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_900)
    Jump("loc_981")

    label("loc_918")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_981")

    def lambda_92C():
        OP_8F(0xFE, 0x640, 0x0, 0xA668, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_92C)
    Sleep(100)

    def lambda_94C():
        OP_8F(0xFE, 0xFFFFFF1A, 0x0, 0x9FE2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_94C)
    Sleep(100)

    def lambda_96C():
        OP_8F(0xFE, 0x622, 0x0, 0xA032, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_96C)

    label("loc_981")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #4
        0x10,
        (
            "#1321F#5P啊啊……\x01",
            "这真是命运弄人啊。\x02\x03",

            "竟然偏偏让我担当\x01",
            "与阁下敌对的角色……\x02\x03",

            "#1185F可是，请相信我！\x01",
            "与您开战\x01",
            "绝对不是我的愿望！\x02",
        )
    )

    Jump("loc_A44")

    label("loc_A44")

    CloseMessageWindow()

    ChrTalk(    #5
        0x10C,
        (
            "#119F#12P啊啊，我很明白。\x02\x03",

            "#111F但是……\x01",
            "请你不要再叫我『阁下』了。\x02\x03",

            "原本也不是对军官\x01",
            "必须使用的敬称……\x02\x03",

            "而且我也已经很习惯\x01",
            "你称呼我『所长』啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#1323F#5P可是，阁下……\x02\x03",

            "#1189F那么，至少在这里\x01",
            "请您允许我用『阁下』称呼您！\x02\x03",

            "在这里出现的我\x01",
            "是被对过去的留恋束缚住的象征……\x02\x03",

            "#1185F请阁下您把我一刀两断，\x01",
            "这样就可以让我获得重生！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10C,
        (
            "#113F#12P凯诺娜……\x02\x03",

            "#115F我明白了，你高兴就好。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E05")
    Sleep(500)

    ChrTalk(    #8
        0x10,
        (
            "#1182F#5P……话说回来。\x01",
            "真是可恨啊，尤莉亚。\x02\x03",

            "为什么没有选中我，\x01",
            "而偏偏是你待在那边呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10E,
        (
            "#176F#12P唉……\x01",
            "你的心情我十分了解……\x02\x03",

            "#178F先不提这次的灾祸，\x01",
            "我能亲自保卫殿下\x01",
            "就要对女神千恩万谢了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3E")

    ChrTalk(    #10
        0x105,
        "#1382F#12P尤莉亚小姐……\x02",
    )

    CloseMessageWindow()

    label("loc_D3E")


    ChrTalk(    #11
        0x10,
        (
            "#1180F#5P哼，算了。\x02\x03",

            "#1183F反正站在你的对立面\x01",
            "对我来说一点也\x01",
            "感觉不到罪恶感。\x02\x03",

            "#1181F我会把你狠揍一番的，\x01",
            "你可不要手下留情哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10E,
        (
            "#179F#4P呵……\x01",
            "那是我要说的话啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_109E")
    Sleep(500)

    ChrTalk(    #13
        0x10,
        (
            "#1180F#5P艾丝蒂尔·布莱特……\x01",
            "跟你也有说不清的纠葛呢。\x02\x03",

            "据说你好像正在利贝尔之外修行，\x01",
            "怎么觉得还是没有什么变化啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1016F#12P啊哈哈……\x01",
            "嗯，算是吧……\x02\x03",

            "#1015F那个……\x01",
            "你好像和理查德上校一起\x01",
            "开了一家调查公司？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#1183F#5P是啊……\x01",
            "从某种意义上来说，\x01",
            "也会和游击士协会进行竞争呢。\x02\x03",

            "#1181F这次就当作是事先打个照面，\x01",
            "让我好好招呼你一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1016F#4P请、请手下留情啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF8")

    ChrTalk(    #17
        0x102,
        "#1514F#12P哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_102A")

    label("loc_FF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_102A")

    ChrTalk(    #18
        0x107,
        "#067F#12P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_102A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1062")

    ChrTalk(    #19
        0x106,
        (
            "#051F#12P哼……\x01",
            "正合我意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109E")

    label("loc_1062")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_109E")

    ChrTalk(    #20
        0x103,
        (
            "#1527F#12P呵呵……\x01",
            "这不是正好吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1234")
    Sleep(500)

    ChrTalk(    #21
        0x10,
        (
            "#1322F#5P可、可是再怎么说……\x02\x03",

            "#1182F为什么\x01",
            "你也会出现在这里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x110,
        (
            "#261F#12P呵呵。\x01",
            "大姐姐，好久不见呢。\x02\x03",

            "#265F我们上次见面还是在准备茶会时\x01",
            "把『福音』作为礼物送给你的时候吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#1189F#5P厚、厚颜无耻……\x02\x03",

            "#1187F我对你也是一肚子火，\x01",
            "就让我好好教训教训你吧！\x02\x03",

            "你可要准备好了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x110,
        (
            "#1306F#12P嘻嘻……\x01",
            "那我就稍微期待一下了⊙\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1234")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1300")

    ChrTalk(    #25
        0x109,
        (
            "#1066F#6P唔……\x01",
            "虽然很有活力，\x01",
            "不过还是那么盛气凌人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12DB")

    ChrTalk(    #26
        0x108,
        (
            "#071F#12P哈哈……\x01",
            "我认为这点很好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DB")


    ChrTalk(    #27
        0x10,
        "#1182F#5P你、你住嘴！\x02",
    )

    CloseMessageWindow()
    Jump("loc_13B6")

    label("loc_1300")


    ChrTalk(    #28
        0x109,
        (
            "#1066F#6P唔……\x01",
            "总觉得是个比想象中\x01",
            "还要有活力的大姐啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137F")

    ChrTalk(    #29
        0x108,
        (
            "#071F#12P哈哈……\x01",
            "正如我所料呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137F")


    ChrTalk(    #30
        0x10,
        (
            "#1185F#5P『比想象中』那个词\x01",
            "就不必说了吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B6")

    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x10, 4)

    def lambda_13E0():

        label("loc_13E0")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_13E0")

    QueueWorkItem2(0x10, 3, lambda_13E0)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -2009, 100, 47910, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 3190, 100, 48160, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFF, -3530, 100, 43250, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0xFF, 4900, 100, 43000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0xFF, 810, 100, 46670, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1562")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15C9")

    label("loc_1562")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158A")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15C9")

    label("loc_158A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B2")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15C9")

    label("loc_15B2")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_15C9")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F6")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_165D")

    label("loc_15F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161E")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_165D")

    label("loc_161E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1646")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_165D")

    label("loc_1646")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_165D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_168A")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16F1")

    label("loc_168A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B2")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16F1")

    label("loc_16B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16DA")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16F1")

    label("loc_16DA")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_16F1")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_171E")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1785")

    label("loc_171E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1746")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1785")

    label("loc_1746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176E")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1785")

    label("loc_176E")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1785")

    Sleep(1000)

    def lambda_1790():
        OP_6D(1930, 0, 46370, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1790)

    def lambda_17A8():
        OP_67(0, 5540, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_17A8)

    def lambda_17C0():
        OP_6B(2920, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_17C0)

    def lambda_17D0():
        OP_6E(303, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_17D0)

    def lambda_17E0():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_17E0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x11, -2009, -3000, 47910, 180)
    SetChrPos(0x12, 3190, -3000, 48160, 180)
    SetChrPos(0x13, -3530, -3000, 43250, 90)
    SetChrPos(0x14, 4900, -3000, 43000, 270)
    SetChrPos(0x15, 810, -3000, 46670, 180)
    OP_22(0x85, 0x1, 0x64)

    def lambda_1863():

        label("loc_1863")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1863")

    QueueWorkItem2(0x109, 3, lambda_1863)
    OP_43(0x11, 0x0, 0x0, 0x5)
    OP_43(0x12, 0x0, 0x0, 0x6)
    OP_43(0x13, 0x0, 0x0, 0x7)
    OP_43(0x14, 0x0, 0x0, 0x8)
    OP_43(0x15, 0x0, 0x0, 0x9)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F8")

    def lambda_18B4():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_18B4)
    Sleep(50)

    def lambda_18C7():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_18C7)
    Sleep(50)

    def lambda_18DA():
        OP_8C(0xFE, 315, 600)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_18DA)
    Sleep(50)

    def lambda_18ED():
        OP_8C(0xFE, 45, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_18ED)
    Jump("loc_19A5")

    label("loc_18F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1950")

    def lambda_190C():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_190C)
    Sleep(50)

    def lambda_191F():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_191F)
    Sleep(50)

    def lambda_1932():
        OP_8C(0xFE, 315, 600)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1932)
    Sleep(50)

    def lambda_1945():
        OP_8C(0xFE, 45, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1945)
    Jump("loc_19A5")

    label("loc_1950")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A5")

    def lambda_1964():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1964)
    Sleep(50)

    def lambda_1977():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1977)
    Sleep(50)

    def lambda_198A():
        OP_8C(0xFE, 315, 600)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_198A)
    Sleep(50)

    def lambda_199D():
        OP_8C(0xFE, 45, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_199D)

    label("loc_19A5")

    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 14)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 16)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 18)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 20)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x15, 0x0)
    OP_44(0x109, 0x3)
    OP_44(0x10, 0x3)
    OP_23(0x85)
    OP_1D(0xC4)
    Fade(1000)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\mp250_00.eff")
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #31
        0x10,
        (
            "#1186F#5P那么阁下……\x01",
            "请让我全力向您挑战吧。\x02\x03",

            "准备好了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10C,
        (
            "#112F#12P好啊……\x01",
            "放马过来吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1AF5():
        OP_6D(1600, 0, 44760, 280)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1AF5)

    def lambda_1B0D():
        OP_67(0, 5830, -10000, 280)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1B0D)

    def lambda_1B25():
        OP_6B(2200, 280)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1B25)

    def lambda_1B35():
        OP_6E(323, 280)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_1B35)
    Sleep(100)
    SetChrChipByIndex(0x11, 9)

    def lambda_1B4F():
        OP_8F(0xFE, 0xFFFFFDE4, 0x0, 0xA9B0, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1B4F)
    SetChrChipByIndex(0x12, 9)

    def lambda_1B6F():
        OP_8F(0xFE, 0x546, 0x0, 0xAB72, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1B6F)
    OP_7D(0x0, 0x13, 0x32, 0x1F4)
    SetChrFlags(0x13, 0x20)
    SetChrChipByIndex(0x13, 7)
    SetChrSubChip(0x13, 6)

    def lambda_1BA1():
        OP_8F(0xFE, 0xFFFFFCC2, 0x0, 0xA47E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1BA1)
    OP_7D(0x0, 0x14, 0x32, 0x1F4)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 7)
    SetChrSubChip(0x14, 6)

    def lambda_1BD3():
        OP_8F(0xFE, 0x7D0, 0x0, 0xA4E2, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1BD3)
    SetChrChipByIndex(0x15, 11)
    SetChrSubChip(0x15, 0)

    def lambda_1BF8():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1BF8)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1C0D():
        OP_96(0xFE, 0x442, 0x0, 0xA604, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1C0D)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A8, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_4_37E end

    def Function_5_1C47(): pass

    label("Function_5_1C47")

    PlayEffect(0x1, 0xFF, 0xFF, -2009, 100, 47910, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_1C47 end

    def Function_6_1C96(): pass

    label("Function_6_1C96")

    PlayEffect(0x1, 0xFF, 0xFF, 3190, 100, 48160, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_1C96 end

    def Function_7_1CE5(): pass

    label("Function_7_1CE5")

    PlayEffect(0x1, 0xFF, 0xFF, -3530, 100, 43250, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_1CE5 end

    def Function_8_1D34(): pass

    label("Function_8_1D34")

    PlayEffect(0x1, 0xFF, 0xFF, 4900, 100, 43000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_1D34 end

    def Function_9_1D83(): pass

    label("Function_9_1D83")

    PlayEffect(0x1, 0xFF, 0xFF, 810, 100, 46670, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_1D83 end

    def Function_10_1DD2(): pass

    label("Function_10_1DD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 740, 0, 47860, 180)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 3)
    OP_43(0x10, 0x3, 0x0, 0xB)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    LoadEffect(0x2, "map\\mp257_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 50, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -500, 0, 43300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F08")
    SetChrPos(0xEF, 780, 0, 44800, 0)
    SetChrPos(0xF0, 1600, 0, 43500, 0)
    SetChrPos(0xF1, 320, 0, 42300, 0)
    Jump("loc_1F8D")

    label("loc_1F08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F4C")
    SetChrPos(0xF0, 780, 0, 44800, 0)
    SetChrPos(0xEF, 1600, 0, 43500, 1)
    SetChrPos(0xF1, 320, 0, 42300, 0)
    Jump("loc_1F8D")

    label("loc_1F4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F8D")
    SetChrPos(0xF1, 780, 0, 44800, 0)
    SetChrPos(0xEF, 1600, 0, 43500, 1)
    SetChrPos(0xF0, 320, 0, 42300, 0)

    label("loc_1F8D")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(1810, 0, 46710, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(45000, 0)
    OP_6E(292, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #33
        0x10,
        (
            "#1183F#5P呵呵……\x01",
            "不愧是理查德阁下。\x02\x03",

            "#1180F……除此之外的人\x01",
            "也很强嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1066F#6P哈哈，谢啦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20B6")

    ChrTalk(    #35
        0x10E,
        (
            "#171F#12P呼……\x01",
            "彼此彼此。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_216F")

    label("loc_20B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20F0")

    ChrTalk(    #36
        0x106,
        (
            "#051F#12P哼……\x01",
            "你也不赖啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_216F")

    label("loc_20F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_212D")

    ChrTalk(    #37
        0x103,
        (
            "#1536F#12P呵呵……\x01",
            "你也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_216F")

    label("loc_212D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_216F")

    ChrTalk(    #38
        0x102,
        (
            "#1513F#12P你也是……\x01",
            "招数应对的不错呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_216F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21B1")

    ChrTalk(    #39
        0x101,
        (
            "#1017F#12P啊哈哈……\x01",
            "是场不错的较量呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21F2")

    ChrTalk(    #40
        0x110,
        (
            "#261F#12P嘻嘻……\x01",
            "我这次玩得很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_222D")

    ChrTalk(    #41
        0x108,
        (
            "#071F#12P哈哈……\x01",
            "辛苦了辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_222D")


    ChrTalk(    #42
        0x10,
        (
            "#1322F#5P哼、哼……\x02\x03",

            "#1182F在前面等候的是\x01",
            "利贝尔的武神们……\x02\x03",

            "你们可给我注意好了，\x01",
            "别拖阁下的后腿。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22DF")

    ChrTalk(    #43
        0x10F,
        "#1447F#12P……明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22FD")

    label("loc_22DF")


    ChrTalk(    #44
        0x109,
        "#1075F#6P知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_22FD")


    ChrTalk(    #45
        0x10C,
        (
            "#115F#12P凯诺娜……\x02\x03",

            "看来我还有\x01",
            "未完成的任务。\x02\x03",

            "#116F前方的试炼\x01",
            "也是其中的一部分。\x02\x03",

            "#111F……多亏了你，\x01",
            "我终于坚定了决心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "#1323F#5P阁、阁下……\x02\x03",

            "#1183F既然您这么说，\x01",
            "我就不再多嘴了……\x02\x03",

            "#1320F请一定要通过试炼，\x01",
            "平安地回来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10C,
        "#119F#12P啊，那是当然。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, -100, -600, 0, 0, 0, 0, 1750, 1750, 1750, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_249A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_249A)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    PlayEffect(0x2, 0x0, 0xFF, 740, 300, 47860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    SetChrFlags(0x10, 0x80)

    ChrTalk(    #48
        0x10C,
        "#116F#12P……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_252D():
        OP_6D(2000, 0, 47710, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_252D)
    OP_8F(0x10C, 0x302, 0x0, 0xB798, 0x7D0, 0x0)
    Sleep(500)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10C, 2)
    SetChrSubChip(0x10C, 0)
    OP_0D()
    Sleep(500)
    OP_82(0x0, 0x2)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #49
        "\x07\x00得到了\x1F\x34\x03\x07\x00。\x02",
    )

    Jump("loc_25AB")

    label("loc_25AB")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x334, 1)
    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10C, 65535)
    SetChrSubChip(0x10C, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x109,
        (
            "#1075F#12P好了……\x01",
            "终于要到核心部分了呢。\x02\x03",

            "#1060F是这个要塞的司令部吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10C, 180, 400)
    Sleep(300)

    ChrTalk(    #51
        0x10C,
        (
            "#115F#5P是啊……\x01",
            "就是院子正面的建筑物。\x02\x03",

            "#110F我们已经有了钥匙，\x01",
            "马上去开门吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B1D)
    OP_28(0x39, 0x1, 0x40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(760, 0, 43590, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, 760, 0, 43590, 180)
    SetChrPos(0x1, 760, 0, 43590, 180)
    SetChrPos(0x2, 760, 0, 43590, 180)
    SetChrPos(0x3, 760, 0, 43590, 180)
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
    OP_1D(0xE8)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_1DD2 end

    def Function_11_2786(): pass

    label("Function_11_2786")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A7")
    Sleep(100)
    Jump("loc_2822")

    label("loc_27A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27BC")
    Sleep(200)
    Jump("loc_2822")

    label("loc_27BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D1")
    Sleep(300)
    Jump("loc_2822")

    label("loc_27D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27E6")
    Sleep(400)
    Jump("loc_2822")

    label("loc_27E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27FB")
    Sleep(500)
    Jump("loc_2822")

    label("loc_27FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2810")
    Sleep(600)
    Jump("loc_2822")

    label("loc_2810")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2822")
    Sleep(700)

    label("loc_2822")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2844")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_2822")

    label("loc_2844")

    Return()

    # Function_11_2786 end

    SaveToFile()

Try(main)
