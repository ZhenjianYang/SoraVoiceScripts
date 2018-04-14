from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4405   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4405.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '丹克',                                 # 9
        '菲利奥',                               # 10
        '特务兵',                               # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01460 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01330 ._CH',             # 02
        'ED6_DT27/CH04000 ._CH',             # 03
        'ED6_DT27/CH04001 ._CH',             # 04
        'ED6_DT07/CH00120 ._CH',             # 05
        'ED6_DT07/CH00121 ._CH',             # 06
        'ED6_DT07/CH00150 ._CH',             # 07
        'ED6_DT07/CH00151 ._CH',             # 08
        'ED6_DT27/CH04080 ._CH',             # 09
        'ED6_DT27/CH04081 ._CH',             # 0A
        'ED6_DT07/CH00340 ._CH',             # 0B
        'ED6_DT07/CH00341 ._CH',             # 0C
        'ED6_DT07/CH00344 ._CH',             # 0D
        'ED6_DT06/CH20042 ._CH',             # 0E
        'ED6_DT07/CH00440 ._CH',             # 0F
        'ED6_DT07/CH00441 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01460P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01330P._CP',             # 02
        'ED6_DT27/CH04000P._CP',             # 03
        'ED6_DT27/CH04001P._CP',             # 04
        'ED6_DT07/CH00120P._CP',             # 05
        'ED6_DT07/CH00121P._CP',             # 06
        'ED6_DT07/CH00150P._CP',             # 07
        'ED6_DT07/CH00151P._CP',             # 08
        'ED6_DT27/CH04080P._CP',             # 09
        'ED6_DT27/CH04081P._CP',             # 0A
        'ED6_DT07/CH00340P._CP',             # 0B
        'ED6_DT07/CH00341P._CP',             # 0C
        'ED6_DT07/CH00344P._CP',             # 0D
        'ED6_DT06/CH20042P._CP',             # 0E
        'ED6_DT07/CH00440P._CP',             # 0F
        'ED6_DT07/CH00441P._CP',             # 10
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 0,
        Y                   = 10870,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 450,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 1050,
        TriggerZ            = 0,
        TriggerY            = 10640,
        TriggerRange        = 800,
        ActorX              = 150,
        ActorZ              = 1700,
        ActorY              = 10640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_2BE",          # 01, 1
        "Function_2_2C4",          # 02, 2
        "Function_3_441",          # 03, 3
        "Function_4_52A",          # 04, 4
        "Function_5_58C",          # 05, 5
        "Function_6_C99",          # 06, 6
        "Function_7_1583",         # 07, 7
        "Function_8_15C7",         # 08, 8
        "Function_9_161F",         # 09, 9
        "Function_10_1663",        # 0A, 10
        "Function_11_167F",        # 0B, 11
        "Function_12_169B",        # 0C, 12
        "Function_13_1734",        # 0D, 13
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_202"),
        (SWITCH_DEFAULT, "loc_216"),
    )


    label("loc_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_213")

    Jump("loc_216")

    label("loc_216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 4)), scpexpr(EXPR_END)), "loc_2BD")
    SetChrPos(0x9, 4840, 0, -2540, 0)
    SetChrPos(0x8, 4250, 0, -210, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrFlags(0xA, 0x800)
    SetChrChipByIndex(0xA, 14)
    SetChrChipByIndex(0xB, 14)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xA, 5)
    SetChrSubChip(0xB, 6)
    SetChrSubChip(0xC, 0)
    SetChrPos(0xA, 4350, 0, -1320, 90)
    SetChrPos(0xB, 3100, 0, -2250, 90)
    SetChrPos(0xC, 2980, 0, 200, 90)

    label("loc_2BD")

    Return()

    # Function_0_1F6 end

    def Function_1_2BE(): pass

    label("Function_1_2BE")

    OP_71(0x1, 0x4)
    Return()

    # Function_1_2BE end

    def Function_2_2C4(): pass

    label("Function_2_2C4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E9")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_42B")

    label("loc_2E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_42B")

    label("loc_302")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_42B")

    label("loc_31B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_334")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_42B")

    label("loc_334")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34D")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_42B")

    label("loc_34D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_366")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_42B")

    label("loc_366")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_42B")

    label("loc_37F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_398")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_42B")

    label("loc_398")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_42B")

    label("loc_3B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CA")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_42B")

    label("loc_3CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E3")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_42B")

    label("loc_3E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FC")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_42B")

    label("loc_3FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_42B")

    label("loc_415")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_42B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_440")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_42B")

    label("loc_440")

    Return()

    # Function_2_2C4 end

    def Function_3_441(): pass

    label("Function_3_441")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 4)), scpexpr(EXPR_END)), "loc_526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4A3")

    ChrTalk(    #0
        0xFE,
        (
            "这、这些家伙\x01",
            "记得是情报部的特务兵吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "样品的引擎\x01",
            "到底打算怎样处理？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_526")

    label("loc_4A3")


    ChrTalk(    #2
        0xFE,
        (
            "样、样品在签字仪式之前\x01",
            "２４小时交替\x01",
            "换人监视的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "这些家伙从上了锁\x01",
            "的门突然破门而入……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "一转眼就把引擎\x01",
            "给抢走了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_526")

    TalkEnd(0xFE)
    Return()

    # Function_3_441 end

    def Function_4_52A(): pass

    label("Function_4_52A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 4)), scpexpr(EXPR_END)), "loc_588")

    ChrTalk(    #5
        0xFE,
        (
            "这些家伙，把引擎\x01",
            "运去码头方向了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "可恶，这可是女王陛下\x01",
            "寄存的重要物品啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_588")

    TalkEnd(0xFE)
    Return()

    # Function_4_52A end

    def Function_5_58C(): pass

    label("Function_5_58C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59F")
    Call(0, 12)

    label("loc_59F")

    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    OP_6D(2320, 0, 13530, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 3350, 0, 4000, 180)
    SetChrPos(0x9, 4390, 0, 4000, 180)
    SetChrPos(0xA, 3720, 0, 2280, 0)
    SetChrPos(0xB, 4770, 0, 960, 0)
    SetChrPos(0xC, 3440, 0, 750, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    def lambda_65D():
        OP_6D(3240, 0, 3110, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65D)

    def lambda_675():
        OP_67(0, 7500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_675)

    def lambda_68D():
        OP_6B(2740, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_68D)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #7
        0x8,
        (
            "#5P你、你们……\x01",
            "到底想怎样！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#5P做这种事\x01",
            "以为就这么完了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        "#6P呼，我们早已有所觉悟了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        (
            "#6P不想受伤的话，\x01",
            "还是乖乖待着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xB,
        (
            "#6P我们没有任何想要加害于\x01",
            "一般市民的意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xC,
        (
            "#6P只是……\x01",
            "在不阻挠我们的情况下。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #13
        0x9,
        (
            "#2P呜，呜。\x01",
            "就饶我一命吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EB")
    SetChrChipByIndex(0x106, 7)
    Jump("loc_7F0")

    label("loc_7EB")

    SetChrChipByIndex(0x103, 5)

    label("loc_7F0")

    SetChrChipByIndex(0x109, 9)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0xF7, 0x80)
    ClearChrFlags(0x109, 0x80)
    SetChrPos(0x101, 10400, 0, 0, 270)
    SetChrPos(0xF7, 11500, 0, 500, 270)
    SetChrPos(0x109, 11500, 0, -1000, 270)

    ChrTalk(    #14
        0x101,
        (
            "#1P一般市民以外的人\x01",
            "就不会留情了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_8DF():
        OP_6D(7050, 0, 1380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8DF)

    def lambda_8F7():
        OP_67(0, 7500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8F7)

    def lambda_90F():
        OP_6B(2740, 1500)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_90F)

    def lambda_91F():
        OP_6E(295, 1500)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_91F)

    def lambda_92F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_92F)
    Sleep(50)

    def lambda_942():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_942)
    Sleep(50)

    def lambda_955():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_955)
    Sleep(50)

    def lambda_968():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_968)
    Sleep(50)

    def lambda_97B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_97B)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF7, 0x2)
    WaitChrThread(0xF7, 0x3)

    ChrTalk(    #15
        0xA,
        "#4P什……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xB,
        "#6P你们……是游击士吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        "#1060F#5P虽然有一个不是… \x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A56")

    ChrTalk(    #18
        0x106,
        (
            "#053F#2P终于找到了……\x01",
            "找得好苦啊。\x02\x03",

            "#054F根据协会规定，\x01",
            "以骚乱破坏活动等的嫌疑\x01",
            "逮捕你们！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABA")

    label("loc_A56")


    ChrTalk(    #19
        0x103,
        (
            "#027F#2P终于找到了……\x01",
            "真是大费周章啊。\x02\x03",

            "#024F根据协会规约，\x01",
            "以骚乱破坏活动等的嫌疑\x01",
            "逮捕你们！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABA")


    ChrTalk(    #20
        0x101,
        (
            "#1006F#5P赶快\x01",
            "束手就擒吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xC,
        (
            "可恶……\x01",
            "怎么被发现的！？\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xB, 11)
    Sleep(500)

    ChrTalk(    #22
        0xB,
        "#6P算了，收拾他们！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xA, 15)
    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xC, 11)
    Sleep(500)

    ChrTalk(    #23
        0xA,
        "#2P#1K解决他们！\x02",
    )


    ChrTalk(    #24
        0xC,
        "#1P#1K解决他们！\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_B7C():
        OP_6D(7950, 0, 330, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B7C)

    def lambda_B94():
        OP_6B(2200, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B94)
    SetChrChipByIndex(0xA, 16)
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 12)

    def lambda_BB3():
        OP_8F(0xFE, 0x1AB8, 0x0, 0x208, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_BB3)

    def lambda_BCE():
        OP_8F(0xFE, 0x1FCC, 0x0, 0x122, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BCE)
    Sleep(50)

    def lambda_BEE():
        OP_8F(0xFE, 0x184C, 0x0, 0x654, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_BEE)

    def lambda_C09():
        OP_8F(0xFE, 0x23E6, 0x0, 0x316, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_C09)
    Sleep(50)

    def lambda_C29():
        OP_8F(0xFE, 0x168A, 0x0, 0xFFFFFF24, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_C29)

    def lambda_C44():
        OP_8F(0xFE, 0x22A6, 0x0, 0xFFFFFC54, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C44)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0xF7, 0xFF)
    OP_44(0x109, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x45C, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_C8F"),
        (SWITCH_DEFAULT, "loc_C94"),
    )


    label("loc_C8F")

    OP_B4(0x0)
    Jump("loc_C94")

    label("loc_C94")

    Call(0, 6)
    Return()

    # Function_5_58C end

    def Function_6_C99(): pass

    label("Function_6_C99")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_6D(4990, 0, -810, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(315000, 0)
    OP_6E(247, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x109, 65535)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0xB, 14)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xA, 3)
    SetChrSubChip(0xB, 6)
    SetChrSubChip(0xC, 0)
    SetChrPos(0x101, 6550, 0, -800, 270)
    SetChrPos(0xF7, 6580, 0, -2100, 270)
    SetChrPos(0x109, 7740, 0, -1420, 270)
    SetChrPos(0x8, 3350, 0, 4000, 180)
    SetChrPos(0x9, 4390, 0, 4000, 180)
    SetChrPos(0xA, 4350, 0, -1320, 90)
    SetChrPos(0xB, 3100, 0, -2250, 90)
    SetChrPos(0xC, 2980, 0, 200, 90)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #25
        0xA,
        (
            "#5P算、算了……\x01",
            "这样就能拖延时间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        (
            "#5P之后就全部交给\x01",
            "上尉殿下了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1004F#2P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xA,
        "#5P情、情报部荣光永存……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 14)
    SetChrSubChip(0xA, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(    #29
        0x101,
        "#1020F#2P慢，慢着！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        "#1068F糟糕，晕过去了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0D")

    ChrTalk(    #31
        0x101,
        (
            "#1019F#2P对了，阿加特。\x01",
            "『上尉』难道是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #32
        0x106,
        (
            "#552F#6P哼……\x01",
            "是那只母狐狸吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6F")

    label("loc_F0D")


    ChrTalk(    #33
        0x101,
        (
            "#1019F#2P对了，雪拉姐。\x01",
            "『上尉』难道是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #34
        0x103,
        (
            "#022F#6P嗯嗯……\x01",
            "是那个顽固的女人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6F")


    def lambda_F75():
        OP_6D(6450, 0, 120, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F75)

    def lambda_F8D():
        OP_8E(0xFE, 0x1B58, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F8D)
    Sleep(400)

    def lambda_FAD():
        OP_8E(0xFE, 0x1770, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FAD)
    Sleep(400)

    def lambda_FCD():

        label("loc_FCD")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_FCD")

    QueueWorkItem2(0x101, 2, lambda_FCD)

    def lambda_FDE():

        label("loc_FDE")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_FDE")

    QueueWorkItem2(0xF7, 2, lambda_FDE)

    def lambda_FEF():

        label("loc_FEF")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_FEF")

    QueueWorkItem2(0x109, 2, lambda_FEF)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 180, 400)
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0x109, 0x2)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #35
        0x8,
        (
            "#5P你们几位……\x01",
            "来得真是时候啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#2P谢谢……\x01",
            "你们是救命恩人啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1016F#6P嘿嘿……\x01",
            "这是我们应该做的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 315, 400)

    ChrTalk(    #38
        0x101,
        "#1004F#6P咦……\x02",
    )

    CloseMessageWindow()

    def lambda_10D5():
        OP_6D(-890, 0, 9800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10D5)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(6450, 0, 120, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(315000, 0)
    OP_6E(247, 0)
    OP_0D()

    ChrTalk(    #39
        0x101,
        "#1020F#6P#3S啊啊！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 600)

    def lambda_1159():

        label("loc_1159")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_1159")

    QueueWorkItem2(0x9, 1, lambda_1159)

    def lambda_116A():

        label("loc_116A")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_116A")

    QueueWorkItem2(0x8, 1, lambda_116A)
    OP_43(0x101, 0x1, 0x0, 0x7)
    Sleep(500)

    def lambda_1187():
        OP_6D(3120, 0, 9680, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1187)

    def lambda_119F():
        OP_6B(2760, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_119F)
    Sleep(2500)
    OP_43(0xF7, 0x1, 0x0, 0x8)
    Sleep(1000)
    OP_43(0x109, 0x1, 0x0, 0x9)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11FF")

    ChrTalk(    #40
        0x106,
        "#052F#6P什么……怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_121F")

    label("loc_11FF")


    ChrTalk(    #41
        0x103,
        "#023F#6P怎么了，艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    label("loc_121F")

    WaitChrThread(0x109, 0x1)

    ChrTalk(    #42
        0x109,
        (
            "#1064F#4P好大的\x01",
            "导力器装置啊。\x02\x03",

            "用来干什么的？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)

    ChrTalk(    #43
        0x101,
        (
            "#1020F#5P那是为埃尔赛尤\x01",
            "开发的高性能导力引擎哦！\x02\x03",

            "记得应该有两个……\x02",
        )
    )

    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_43(0x8, 0x1, 0x0, 0xA)
    Sleep(300)
    OP_43(0x9, 0x1, 0x0, 0xB)
    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    OP_6D(2660, 0, 7880, 1000)

    ChrTalk(    #44
        0x8,
        (
            "#5P啊啊，这些家伙的同伙\x01",
            "用搬运车将它载走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        "#5P载往前方的码头方向……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 180, 500)

    def lambda_1359():
        OP_8C(0xF7, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1359)
    OP_8C(0x109, 180, 400)

    ChrTalk(    #46
        0x101,
        "#1005F#6P你、你说什么～！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140F")

    ChrTalk(    #47
        0x106,
        "#552F#6P可恶，不好的预感。\x02",
    )

    CloseMessageWindow()

    def lambda_13BD():
        OP_6D(3120, 0, 9680, 1000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_13BD)
    OP_8C(0x106, 315, 400)
    WaitChrThread(0xF7, 0x1)

    ChrTalk(    #48
        0x106,
        (
            "#054F#6P艾丝蒂尔、凯文！\x01",
            "我们赶紧去码头吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1488")

    label("loc_140F")


    ChrTalk(    #49
        0x103,
        "#522F#6P有不好的预感呢……\x02",
    )

    CloseMessageWindow()

    def lambda_1435():
        OP_6D(3120, 0, 9680, 1000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1435)
    OP_8C(0x103, 315, 400)
    WaitChrThread(0xF7, 0x1)

    ChrTalk(    #50
        0x103,
        (
            "#024F#6P艾丝蒂尔、凯文先生！\x01",
            "我们赶紧去码头吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1488")

    OP_8C(0x101, 135, 500)

    ChrTalk(    #51
        0x101,
        "#1005F#5P明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        "#1062F#2P好！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(2990, 0, 9730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 2990, 0, 9730, 90)
    SetChrPos(0x1, 2990, 0, 9730, 90)
    SetChrPos(0x2, 2990, 0, 9730, 90)
    OP_69(0x0, 0x0)
    SetChrPos(0x9, 4840, 0, -2540, 0)
    SetChrPos(0x8, 4250, 0, -210, 270)
    OP_4B(0x9, 255)
    OP_4B(0x8, 255)
    OP_A2(0x163C)
    OP_28(0x8E, 0x1, 0x4)
    OP_28(0x8E, 0x1, 0x8)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_C99 end

    def Function_7_1583(): pass

    label("Function_7_1583")

    OP_8E(0xFE, 0x292C, 0x0, 0xB36, 0x1388, 0x0)
    OP_8E(0xFE, 0x2990, 0x0, 0x1A72, 0x1388, 0x0)
    OP_8E(0xFE, 0x8FC, 0x0, 0x2580, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_7_1583 end

    def Function_8_15C7(): pass

    label("Function_8_15C7")

    OP_8E(0xFE, 0x1946, 0x0, 0xFFFFFDA8, 0x1388, 0x0)
    OP_8E(0xFE, 0x292C, 0x0, 0xB36, 0x1388, 0x0)
    OP_8E(0xFE, 0x2990, 0x0, 0x1A72, 0x1388, 0x0)
    OP_8E(0xFE, 0xDFC, 0x0, 0x21AC, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_15C7 end

    def Function_9_161F(): pass

    label("Function_9_161F")

    OP_8E(0xFE, 0x292C, 0x0, 0xB36, 0x1388, 0x0)
    OP_8E(0xFE, 0x2990, 0x0, 0x1A72, 0x1388, 0x0)
    OP_8E(0xFE, 0xE2E, 0x0, 0x27BA, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_161F end

    def Function_10_1663(): pass

    label("Function_10_1663")

    OP_8E(0xFE, 0xDDE, 0x0, 0xBCC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_1663 end

    def Function_11_167F(): pass

    label("Function_11_167F")

    OP_8E(0xFE, 0x1220, 0x0, 0xAF0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_167F end

    def Function_12_169B(): pass

    label("Function_12_169B")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1715"),
        (1, "loc_171B"),
        (SWITCH_DEFAULT, "loc_1721"),
    )


    label("loc_1715")

    OP_A2(0x1200)
    Jump("loc_1721")

    label("loc_171B")

    OP_A2(0x1201)
    Jump("loc_1721")

    label("loc_1721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_172F")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_1733")

    label("loc_172F")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_1733")

    Return()

    # Function_12_169B end

    def Function_13_1734(): pass

    label("Function_13_1734")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x05有埃尔赛尤用的新型引擎。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_1734 end

    SaveToFile()

Try(main)
