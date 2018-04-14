from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R0302   ._SN',
        MapName             = 'rolent',
        Location            = 'R0302.x',
        MapIndex            = 21,
        MapDefaultBGM       = "ed60022",
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
        '雾调整',                               # 9
        '洛连特方向',                           # 10
        '玛鲁加矿山方向',                       # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT09/CH11050 ._CH',             # 00
        'ED6_DT09/CH11051 ._CH',             # 01
        'ED6_DT09/CH10100 ._CH',             # 02
        'ED6_DT09/CH10101 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT09/CH11050P._CP',             # 00
        'ED6_DT09/CH11051P._CP',             # 01
        'ED6_DT09/CH10100P._CP',             # 02
        'ED6_DT09/CH10101P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x189,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -146110,
        Z                   = 10,
        Y                   = -9950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -163040,
        Z                   = 3920,
        Y                   = 102800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -156000,
        Z                   = 2000,
        Y                   = 18000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -146000,
        Z                   = 2100,
        Y                   = 27000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x68,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -130000,
        Z                   = 4100,
        Y                   = 26000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x64,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -117000,
        Z                   = 4100,
        Y                   = 31000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x67,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154000,
        Z                   = 2000,
        Y                   = 47000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x69,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -156000,
        Z                   = 4000,
        Y                   = 68000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x65,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -109910,
        TriggerZ            = 5850,
        TriggerY            = 62020,
        TriggerRange        = 1000,
        ActorX              = -109910,
        ActorZ              = 7350,
        ActorY              = 62020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_227",          # 01, 1
        "Function_2_30B",          # 02, 2
        "Function_3_3A1",          # 03, 3
        "Function_4_4B8",          # 04, 4
        "Function_5_A91",          # 05, 5
        "Function_6_E9D",          # 06, 6
        "Function_7_133E",         # 07, 7
        "Function_8_13DA",         # 08, 8
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_210")
    Event(0, 6)
    Jump("loc_226")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_222")
    Event(0, 5)
    Jump("loc_226")

    label("loc_222")

    Event(0, 4)

    label("loc_226")

    Return()

    # Function_0_1F6 end

    def Function_1_227(): pass

    label("Function_1_227")

    OP_16(0x2, 0xFA0, 0xFFFBF0F0, 0xFFFEB010, 0x230010)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x326, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B")
    OP_6F(0x0, 0)
    Jump("loc_252")

    label("loc_24B")

    OP_6F(0x0, 60)

    label("loc_252")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_289")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)
    Jump("loc_30A")

    label("loc_289")

    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_30A")

    Return()

    # Function_1_227 end

    def Function_2_30B(): pass

    label("Function_2_30B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A0")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33E")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_353")

    label("loc_33E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_353")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_353")

    OP_4F(0x38, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_IMUL), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_383")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_398")

    label("loc_383")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_398")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_398")

    Sleep(10)
    Jump("Function_2_30B")

    label("loc_3A0")

    Return()

    # Function_2_30B end

    def Function_3_3A1(): pass

    label("Function_3_3A1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x326, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_410")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1932)
    Jump("loc_476")

    label("loc_410")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_476")

    Jump("loc_4AA")

    label("loc_479")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4AA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3A1 end

    def Function_4_4B8(): pass

    label("Function_4_4B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E2")
    Call(0, 7)
    FadeToBright(0, 0)
    Call(0, 8)

    label("loc_4E2")

    OP_6D(-145490, -10, 2670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(134000, 0)
    OP_6E(243, 0)
    SetChrPos(0x101, -145500, -10, -3730, 0)
    SetChrPos(0x103, -146500, -10, -3730, 0)
    SetChrPos(0xF8, -145250, -10, -4730, 0)
    SetChrPos(0xF9, -146750, -10, -4730, 0)

    def lambda_569():
        OP_90(0xFE, 0x0, 0x0, 0x1B58, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_569)
    Sleep(100)

    def lambda_589():
        OP_90(0xFE, 0x0, 0x0, 0x1B58, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_589)
    Sleep(200)

    def lambda_5A9():
        OP_90(0xFE, 0x0, 0x0, 0x1B58, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5A9)
    Sleep(100)

    def lambda_5C9():
        OP_90(0xFE, 0x0, 0x0, 0x1B58, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5C9)
    FadeToBright(1000, 0)
    WaitChrThread(0xF9, 0x1)
    OP_0D()

    ChrTalk(    #3
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_608():
        OP_8E(0xFE, 0xFFFDC7A4, 0x3C, 0x204E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_608)
    Sleep(100)

    def lambda_628():
        OP_8E(0xFE, 0xFFFDC2EA, 0x1E, 0x1FFD, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_628)
    Sleep(200)

    def lambda_648():
        OP_8E(0xFE, 0xFFFDC86C, 0x3C, 0x1AA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_648)
    Sleep(100)

    def lambda_668():
        OP_8E(0xFE, 0xFFFDC2D6, 0x1E, 0x19FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_668)

    def lambda_683():
        OP_6D(-145700, 60, 7100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_683)

    def lambda_69B():
        OP_6B(3540, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_69B)
    OP_8C(0x101, 45, 400)
    Sleep(50)
    OP_8C(0x103, 0, 400)
    Sleep(30)
    OP_8C(0xF8, 0, 400)
    Sleep(50)
    OP_8C(0xF9, 320, 400)
    Sleep(300)
    OP_8C(0x101, 0, 400)
    Sleep(50)
    OP_8C(0x103, 45, 400)
    Sleep(30)
    OP_8C(0xF8, 320, 400)
    Sleep(50)
    OP_8C(0xF9, 0, 400)
    Sleep(300)
    OP_8C(0x101, 320, 400)
    Sleep(50)
    OP_8C(0x103, 320, 400)
    Sleep(30)
    OP_8C(0xF8, 0, 400)
    Sleep(50)
    OP_8C(0xF9, 45, 400)
    Sleep(300)
    OP_8C(0x101, 0, 400)
    Sleep(50)
    OP_8C(0x103, 45, 400)
    Sleep(30)
    OP_8C(0xF8, 45, 400)
    Sleep(50)
    OP_8C(0xF9, 320, 400)
    Sleep(300)
    OP_8C(0x101, 180, 400)
    Sleep(50)
    OP_8C(0x103, 180, 400)
    Sleep(30)
    OP_8C(0xF8, 0, 400)
    Sleep(50)
    OP_8C(0xF9, 0, 400)
    Sleep(300)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D3")

    ChrTalk(    #4
        0x107,
        (
            "#560F哇……\x01",
            "一下子就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C")

    label("loc_7D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_805")

    ChrTalk(    #5
        0x106,
        (
            "#051F嘿……\x01",
            "突然就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C")

    label("loc_805")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_839")

    ChrTalk(    #6
        0x104,
        (
            "#030F哦……\x01",
            "一下子就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C")

    label("loc_839")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86D")

    ChrTalk(    #7
        0x105,
        (
            "#048F呵呵……\x01",
            "忽然就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C")

    label("loc_86D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C")

    ChrTalk(    #8
        0x108,
        (
            "#070F呼……\x01",
            "突然就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D8")

    ChrTalk(    #9
        0x107,
        (
            "#061F雾的覆盖范围\x01",
            "似乎就到这里为止呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C5")

    label("loc_8D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_914")

    ChrTalk(    #10
        0x106,
        (
            "#051F雾的覆盖范围\x01",
            "似乎就到这里为止啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C5")

    label("loc_914")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_950")

    ChrTalk(    #11
        0x104,
        (
            "#030F雾的覆盖范围\x01",
            "似乎就到这里为止啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C5")

    label("loc_950")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98C")

    ChrTalk(    #12
        0x105,
        (
            "#048F雾的覆盖范围\x01",
            "似乎就到这里为止呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C5")

    label("loc_98C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C5")

    ChrTalk(    #13
        0x108,
        (
            "#070F雾的覆盖范围\x01",
            "似乎就到这里为止啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C5")


    ChrTalk(    #14
        0x103,
        (
            "#026F玛鲁加山道，距离洛连特市\x01",
            "大约１４０塞尔矩的地点……\x02\x03",

            "#022F不但浓雾的范围很广，\x01",
            "还有魔兽游荡，非常危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1015F#6P嗯，是啊。\x02\x03",

            "调查完其它地方后，\x01",
            "必须赶快向爱娜姐报告才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1810)
    OP_28(0x8F, 0x2, 0x40)
    OP_28(0x8F, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_4_4B8 end

    def Function_5_A91(): pass

    label("Function_5_A91")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABB")
    Call(0, 7)
    FadeToBright(0, 0)
    Call(0, 8)

    label("loc_ABB")

    OP_6D(-145490, -10, 2670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(134000, 0)
    OP_6E(243, 0)
    SetChrPos(0x101, -145500, -10, -730, 0)
    SetChrPos(0x103, -146500, -10, -730, 0)
    SetChrPos(0xF8, -145250, -10, -1730, 0)
    SetChrPos(0xF9, -146750, -10, -1730, 0)

    def lambda_B42():
        OP_8E(0xFE, 0xFFFDC7A4, 0x3C, 0x204E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B42)
    Sleep(100)

    def lambda_B62():
        OP_8E(0xFE, 0xFFFDC2EA, 0x1E, 0x1FFD, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B62)
    Sleep(200)

    def lambda_B82():
        OP_8E(0xFE, 0xFFFDC86C, 0x3C, 0x1AA4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_B82)
    Sleep(100)

    def lambda_BA2():
        OP_8E(0xFE, 0xFFFDC2D6, 0x1E, 0x19FA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_BA2)

    def lambda_BBD():
        OP_6D(-145700, 60, 7100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BBD)

    def lambda_BD5():
        OP_6B(3540, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BD5)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1E")

    ChrTalk(    #16
        0x107,
        "#061F嘿嘿，已经晴了⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_CDA")

    label("loc_C1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4E")

    ChrTalk(    #17
        0x106,
        (
            "#051F呼……\x01",
            "雾终于散了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CDA")

    label("loc_C4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7E")

    ChrTalk(    #18
        0x104,
        (
            "#030F嗯……\x01",
            "雾终于散了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CDA")

    label("loc_C7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAD")

    ChrTalk(    #19
        0x105,
        "#048F……似乎已经晴了哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CDA")

    label("loc_CAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDA")

    ChrTalk(    #20
        0x108,
        (
            "#070F嗯……\x01",
            "雾终于散了吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDA")


    ChrTalk(    #21
        0x103,
        (
            "#026F玛鲁加山道，距离洛连特市\x01",
            "大约１４０塞尔矩的地点……\x02\x03",

            "#022F不但浓雾的范围很广，\x01",
            "还有魔兽游荡，非常危险。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE8")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇调查过米尔西街道】\x01",      # 0
            "【◇调查过艾利兹街道】\x01",      # 1
            "【◇不变更】\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DD6"),
        (1, "loc_DDF"),
        (SWITCH_DEFAULT, "loc_DE8"),
    )


    label("loc_DD6")

    OP_A3(0x180E)
    OP_A2(0x180F)
    Jump("loc_DE8")

    label("loc_DDF")

    OP_A2(0x180E)
    OP_A3(0x180F)
    Jump("loc_DE8")

    label("loc_DE8")

    TurnDirection(0x101, 0x103, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_END)), "loc_E42")

    ChrTalk(    #22
        0x101,
        (
            "#1006F#5P嗯……\x01",
            "就向爱娜姐报告吧。\x02\x03",

            "接下来，只剩下\x01",
            "艾利兹街道了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8B")

    label("loc_E42")


    ChrTalk(    #23
        0x101,
        (
            "#1006F#5P嗯……\x01",
            "就向爱娜姐报告吧。\x02\x03",

            "接下来，只剩下\x01",
            "米尔西街道了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8B")

    OP_A2(0x1810)
    OP_28(0x8F, 0x2, 0x40)
    OP_28(0x8F, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_5_A91 end

    def Function_6_E9D(): pass

    label("Function_6_E9D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC7")
    Call(0, 7)
    FadeToBright(0, 0)
    Call(0, 8)

    label("loc_EC7")

    OP_6D(-145490, -10, 2670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(134000, 0)
    OP_6E(243, 0)
    SetChrPos(0x101, -145500, -10, -730, 0)
    SetChrPos(0x103, -146500, -10, -730, 0)
    SetChrPos(0xF8, -145250, -10, -1730, 0)
    SetChrPos(0xF9, -146750, -10, -1730, 0)

    def lambda_F4E():
        OP_8E(0xFE, 0xFFFDC7A4, 0x3C, 0x204E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F4E)
    Sleep(100)

    def lambda_F6E():
        OP_8E(0xFE, 0xFFFDC2EA, 0x1E, 0x1FFD, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F6E)
    Sleep(200)

    def lambda_F8E():
        OP_8E(0xFE, 0xFFFDC86C, 0x3C, 0x1AA4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_F8E)
    Sleep(100)

    def lambda_FAE():
        OP_8E(0xFE, 0xFFFDC2D6, 0x1E, 0x19FA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_FAE)

    def lambda_FC9():
        OP_6D(-145700, 60, 7100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FC9)

    def lambda_FE1():
        OP_6B(3540, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_FE1)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102E")

    ChrTalk(    #24
        0x107,
        "#061F嘿嘿，雾终于散了阿⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_10E4")

    label("loc_102E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105E")

    ChrTalk(    #25
        0x106,
        (
            "#051F呼……\x01",
            "雾终于散了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E4")

    label("loc_105E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108E")

    ChrTalk(    #26
        0x104,
        (
            "#030F嗯……\x01",
            "雾终于散了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E4")

    label("loc_108E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B7")

    ChrTalk(    #27
        0x105,
        "#048F雾终于散了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10E4")

    label("loc_10B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E4")

    ChrTalk(    #28
        0x108,
        (
            "#070F嗯……\x01",
            "雾终于散了吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E4")


    ChrTalk(    #29
        0x103,
        (
            "#026F玛鲁加山道，距离洛连特市\x01",
            "大约１４０塞尔矩的地点……\x02\x03",

            "#022F不但浓雾的范围很广，\x01",
            "还有魔兽游荡，非常危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1015F#6P嗯，的确。\x02\x03",

            "这样的话，三个地方\x01",
            "都调查过了…\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #31
        0x101,
        (
            "#1006F#5P我们应该回协会\x01",
            "向爱娜姐报告了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1257")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇没去过布莱特家】\x01",      # 0
            "【◇去过布莱特家】\x01",        # 1
            "【◇不变更】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_124B"),
        (1, "loc_1251"),
        (SWITCH_DEFAULT, "loc_1257"),
    )


    label("loc_124B")

    OP_A3(0x180D)
    Jump("loc_1257")

    label("loc_1251")

    OP_A2(0x180D)
    Jump("loc_1257")

    label("loc_1257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FD")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #32
        0x103,
        (
            "#023F那样也好……\x02\x03",

            "不过，好像还没\x01",
            "回家看看呢吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1004F#5P啊……都给忘了。\x02\x03",

            "#1008F回协会报告之前\x01",
            "先回去看一下吧。\x02",
        )
    )

    OP_28(0x8F, 0x2, 0x40)
    OP_28(0x8F, 0x1, 0x80)
    OP_28(0x8F, 0x1, 0x800)
    OP_28(0x8F, 0x1, 0x1000)
    CloseMessageWindow()
    Jump("loc_1338")

    label("loc_12FD")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #34
        0x103,
        (
            "#021F哎哎。\x01",
            "那样也好。\x02",
        )
    )

    OP_28(0x8F, 0x2, 0x40)
    OP_28(0x8F, 0x1, 0x80)
    OP_28(0x8F, 0x1, 0x200)
    OP_28(0x8F, 0x1, 0x400)
    CloseMessageWindow()

    label("loc_1338")

    OP_A2(0x1810)
    EventEnd(0x0)
    Return()

    # Function_6_E9D end

    def Function_7_133E(): pass

    label("Function_7_133E")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_13BB"),
        (1, "loc_13C1"),
        (SWITCH_DEFAULT, "loc_13C7"),
    )


    label("loc_13BB")

    OP_A2(0x1200)
    Jump("loc_13C7")

    label("loc_13C1")

    OP_A2(0x1201)
    Jump("loc_13C7")

    label("loc_13C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_13D5")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_13D9")

    label("loc_13D5")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_13D9")

    Return()

    # Function_7_133E end

    def Function_8_13DA(): pass

    label("Function_8_13DA")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_8_13DA end

    SaveToFile()

Try(main)
