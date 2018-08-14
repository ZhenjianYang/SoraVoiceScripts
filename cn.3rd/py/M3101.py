from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3101   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3101.x',
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
        'ED6_DT09/CH10060 ._CH',             # 00
        'ED6_DT09/CH10061 ._CH',             # 01
        'ED6_DT09/CH11210 ._CH',             # 02
        'ED6_DT09/CH11211 ._CH',             # 03
        'ED6_DT09/CH11030 ._CH',             # 04
        'ED6_DT09/CH11031 ._CH',             # 05
        'ED6_DT09/CH11020 ._CH',             # 06
        'ED6_DT09/CH11021 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10060P._CP',             # 00
        'ED6_DT09/CH10061P._CP',             # 01
        'ED6_DT09/CH11210P._CP',             # 02
        'ED6_DT09/CH11211P._CP',             # 03
        'ED6_DT09/CH11030P._CP',             # 04
        'ED6_DT09/CH11031P._CP',             # 05
        'ED6_DT09/CH11020P._CP',             # 06
        'ED6_DT09/CH11021P._CP',             # 07
    )

    DeclMonster(
        X                   = 8500,
        Z                   = 0,
        Y                   = 28030,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22270,
        Z                   = 0,
        Y                   = 9030,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14650,
        Z                   = 0,
        Y                   = 30060,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x290,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -38720,
        Z                   = 0,
        Y                   = 14660,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x291,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -43020,
        Z                   = 0,
        Y                   = 37800,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17170,
        Z                   = 0,
        Y                   = 52830,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -50190,
        Z                   = 0,
        Y                   = 53970,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x290,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -52720,
        TriggerZ            = 500,
        TriggerY            = 17080,
        TriggerRange        = 1000,
        ActorX              = -52720,
        ActorZ              = 1000,
        ActorY              = 17080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -950,
        TriggerZ            = 500,
        TriggerY            = 36160,
        TriggerRange        = 1000,
        ActorX              = -950,
        ActorZ              = 1000,
        ActorY              = 36160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -35580,
        TriggerZ            = 120,
        TriggerY            = 37890,
        TriggerRange        = 1000,
        ActorX              = -35580,
        ActorZ              = 1120,
        ActorY              = 37890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_21A",          # 00, 0
        "Function_1_22E",          # 01, 1
        "Function_2_297",          # 02, 2
        "Function_3_3BD",          # 03, 3
        "Function_4_BB0",          # 04, 4
        "Function_5_CE3",          # 05, 5
        "Function_6_10EC",         # 06, 6
    )


    def Function_0_21A(): pass

    label("Function_0_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_22D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_22D")

    Return()

    # Function_0_21A end

    def Function_1_22E(): pass

    label("Function_1_22E")

    OP_16(0x2, 0xFA0, 0xFFFDFC60, 0xFFFE8130, 0x2300A6)
    OP_1B(0x1, 0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_END)), "loc_253")
    OP_6F(0x0, 450)

    label("loc_253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_264")
    OP_72(0x1002, 0x0)
    ExitThread()
    Jump("loc_268")

    label("loc_264")

    OP_64(0x0, 0x1)

    label("loc_268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279")
    OP_72(0x1001, 0x0)
    ExitThread()
    Jump("loc_27D")

    label("loc_279")

    OP_64(0x1, 0x1)

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F")
    OP_6F(0x2E, 0)
    Jump("loc_296")

    label("loc_28F")

    OP_6F(0x2E, 60)

    label("loc_296")

    Return()

    # Function_1_22E end

    def Function_2_297(): pass

    label("Function_2_297")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x176, 1)"), scpexpr(EXPR_END)), "loc_30B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x76\x01\x07\x00。\x02",
    )

    Jump("loc_2F0")

    label("loc_2F0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B83)
    Jump("loc_379")

    label("loc_30B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x76\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x76\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_35A")

    label("loc_35A")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2E, 60)
    OP_70(0x2E, 0x0)

    label("loc_379")

    Jump("loc_3AF")

    label("loc_37C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3AF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_297 end

    def Function_3_3BD(): pass

    label("Function_3_3BD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(238, 0x48, 0x2)
    OP_E0(238, 0x49, 0x3)
    OP_E0(239, 0x4A, 0x2)
    OP_E0(239, 0x4B, 0x3)
    OP_E0(240, 0x4C, 0x2)
    OP_E0(240, 0x4D, 0x3)
    OP_E0(241, 0x4E, 0x2)
    OP_E0(241, 0x4F, 0x3)
    SetChrPos(0x109, 37650, 400, 22330, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_446")
    SetChrPos(0x10C, 36700, 400, 23790, 270)
    SetChrPos(0xF0, 35510, 400, 22410, 270)
    SetChrPos(0xF1, 33730, 400, 23520, 270)
    Jump("loc_4CB")

    label("loc_446")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48A")
    SetChrPos(0x10C, 36700, 400, 23790, 270)
    SetChrPos(0xEF, 35510, 400, 22410, 270)
    SetChrPos(0xF1, 33730, 400, 23520, 270)
    Jump("loc_4CB")

    label("loc_48A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CB")
    SetChrPos(0x10C, 36700, 400, 23790, 270)
    SetChrPos(0xEF, 35510, 400, 22410, 270)
    SetChrPos(0xF0, 33730, 400, 23520, 270)

    label("loc_4CB")

    OP_6D(28800, 0, 24620, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(306, 0)
    SetChrChipByIndex(0xEE, 8)
    SetChrChipByIndex(0xEF, 10)
    SetChrChipByIndex(0xF0, 12)
    SetChrChipByIndex(0xF1, 14)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_583")

    def lambda_530():
        OP_8F(0xFE, 0x4FEC, 0x0, 0x5BC2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_530)

    def lambda_54B():
        OP_8F(0xFE, 0x50D2, 0x0, 0x54C4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_54B)
    Sleep(100)

    def lambda_56B():
        OP_8F(0xFE, 0x571C, 0x0, 0x5CB2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_56B)
    Jump("loc_64E")

    label("loc_583")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EA")

    def lambda_597():
        OP_8F(0xFE, 0x4FEC, 0x0, 0x5BC2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_597)

    def lambda_5B2():
        OP_8F(0xFE, 0x50D2, 0x0, 0x54C4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_5B2)
    Sleep(100)

    def lambda_5D2():
        OP_8F(0xFE, 0x571C, 0x0, 0x5CB2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_5D2)
    Jump("loc_64E")

    label("loc_5EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64E")

    def lambda_5FE():
        OP_8F(0xFE, 0x4FEC, 0x0, 0x5BC2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_5FE)

    def lambda_619():
        OP_8F(0xFE, 0x50D2, 0x0, 0x54C4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_619)
    Sleep(100)

    def lambda_639():
        OP_8F(0xFE, 0x571C, 0x0, 0x5CB2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_639)

    label("loc_64E")


    def lambda_654():
        OP_8F(0xFE, 0x57D0, 0x0, 0x56C2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_654)

    def lambda_66F():
        OP_6D(22650, 0, 23940, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_66F)

    def lambda_687():
        OP_67(0, 5840, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_687)

    def lambda_69F():
        OP_6B(2750, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_69F)

    def lambda_6AF():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6AF)

    def lambda_6BF():
        OP_6E(300, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_6BF)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)

    def lambda_6ED():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_6ED)
    Sleep(100)

    def lambda_700():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_700)
    Sleep(100)

    def lambda_713():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_713)
    Sleep(100)
    OP_8C(0xEE, 90, 400)
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
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #3
        0x109,
        (
            "#1841F#5P呼、呼……\x02\x03",

            "#1069F刚才那个\x01",
            "怎么说也太犯规了吧……！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_811")

    ChrTalk(    #4
        0x10F,
        (
            "#1445F#6P确实……\x01",
            "似乎不太正常呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_811")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_848")

    ChrTalk(    #5
        0x10E,
        "#175F#6P是啊……我也有同感。\x02",
    )

    CloseMessageWindow()

    label("loc_848")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87C")

    ChrTalk(    #6
        0x101,
        "#1019F#6P这也太乱来了……\x02",
    )

    CloseMessageWindow()

    label("loc_87C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B2")

    ChrTalk(    #7
        0x102,
        "#1502F#6P简直不由分说啊……\x02",
    )

    CloseMessageWindow()

    label("loc_8B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E3")

    ChrTalk(    #8
        0x10B,
        "#413F#6P不、不可能……\x02",
    )

    CloseMessageWindow()

    label("loc_8E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_916")

    ChrTalk(    #9
        0x107,
        "#562F#6P好、好可怕～……\x02",
    )

    CloseMessageWindow()

    label("loc_916")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_94E")

    ChrTalk(    #10
        0x10A,
        "#1316F#6P还、还以为要死了……\x02",
    )

    CloseMessageWindow()

    label("loc_94E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_984")

    ChrTalk(    #11
        0x105,
        "#1169F#6P真是吓了一大跳……\x02",
    )

    CloseMessageWindow()

    label("loc_984")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C1")

    ChrTalk(    #12
        0x103,
        (
            "#1533F#6P真是的……\x01",
            "开什么玩笑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F2")

    ChrTalk(    #13
        0x106,
        "#057F#6P竟敢小看人……\x02",
    )

    CloseMessageWindow()

    label("loc_9F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A31")

    ChrTalk(    #14
        0x104,
        (
            "#1544F#6P哎呀哎呀……\x01",
            "刺激过头了吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A6C")

    ChrTalk(    #15
        0x10D,
        "#276F#6P不愧是利贝尔的军用艇……\x02",
    )

    CloseMessageWindow()

    label("loc_A6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AAE")

    ChrTalk(    #16
        0x108,
        (
            "#075F#6P哎呀哎呀……\x01",
            "我还真不够成熟啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B08")

    ChrTalk(    #17
        0x110,
        (
            "#1300F#6P唔，\x01",
            "那种东西只要叫玛蒂尔·帕蒂尔来\x01",
            "瞬间就可以解决……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B08")


    ChrTalk(    #18
        0x10C,
        (
            "#115F#5P『前方禁止通行』……\x01",
            "大概是这么个规矩吧。\x02\x03",

            "#112F现在先去别的地方看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        (
            "#1840F#6P嗯……\x01",
            "留得青山在不怕没柴烧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B19)
    OP_28(0x39, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_3BD end

    def Function_4_BB0(): pass

    label("Function_4_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_BF7")
    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_BD5():
        OP_90(0x0, 0x1388, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_BD5)
    OP_0D()
    NewScene("ED6_DT21/M3102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_CE2")

    label("loc_BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 1)), scpexpr(EXPR_END)), "loc_CA5")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C16")
    TurnDirection(0x10C, 0x1, 400)
    Jump("loc_C1D")

    label("loc_C16")

    TurnDirection(0x10C, 0x0, 400)

    label("loc_C1D")


    ChrTalk(    #20
        0x10C,
        (
            "#115F要探索的话，\x01",
            "还是先去别处看看吧。\x02\x03",

            "#112F照现在这情况\x01",
            "去多少次都只会重蹈覆辙而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFF830, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_CE2")

    label("loc_CA5")

    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_CC3():
        OP_90(0x0, 0x1388, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_CC3)
    OP_0D()
    NewScene("ED6_DT21/M3102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_CE2")

    Return()

    # Function_4_BB0 end

    def Function_5_CE3(): pass

    label("Function_5_CE3")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #21
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10E8")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-51170, 0, 17930, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(314000, 0)
    OP_6E(237, 0)
    SetChrPos(0x109, -50030, 0, 16870, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD2")
    SetChrPos(0x10C, -48670, 0, 15640, 270)
    SetChrPos(0xF0, -48500, 0, 17280, 270)
    SetChrPos(0xF1, -47560, 0, 16210, 270)
    Jump("loc_E57")

    label("loc_DD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E16")
    SetChrPos(0x10C, -48670, 0, 15640, 270)
    SetChrPos(0xEF, -48500, 0, 17280, 270)
    SetChrPos(0xF1, -47560, 0, 16210, 270)
    Jump("loc_E57")

    label("loc_E16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E57")
    SetChrPos(0x10C, -48670, 0, 15640, 270)
    SetChrPos(0xEF, -48500, 0, 17280, 270)
    SetChrPos(0xF0, -47560, 0, 16210, 270)

    label("loc_E57")

    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x109,
        "#1079F#5P这扇门是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10C,
        (
            "#115F#6P这里是雷斯顿要塞的\x01",
            "第一兵营。\x02\x03",

            "#110F用之前中校交给我们的钥匙\x01",
            "应该就能打开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1060F#5P原来如此。\x01",
            "那就……\x02",
        )
    )

    Jump("loc_F1C")

    label("loc_F1C")

    CloseMessageWindow()
    OP_8E(0x109, 0xFFFF3616, 0x1F4, 0x41BE, 0x7D0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #25
        "\x07\x05凯文使用了兵营的钥匙。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x10C,
        (
            "#115F#6P这里不过是一座兵营，\x01",
            "里面应该不会很大。\x02\x03",

            "#110F尽快把这里搜个遍吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #27
        0x109,
        "#1060F#5P明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2B1B)
    OP_71(0x1002, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    OP_6D(-48260, 0, 16650, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -48260, 0, 16650, 270)
    SetChrPos(0x1, -48260, 0, 16650, 270)
    SetChrPos(0x2, -48260, 0, 16650, 270)
    SetChrPos(0x3, -48260, 0, 16650, 270)
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

    label("loc_10E8")

    TalkEnd(0xFF)
    Return()

    # Function_5_CE3 end

    def Function_6_10EC(): pass

    label("Function_6_10EC")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #28
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E65")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-200, 0, 33170, 0)
    OP_67(0, 5820, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(245, 0)
    SetChrPos(0x109, -2220, 0, 31530, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DB")
    SetChrPos(0x10C, -1250, 0, 33430, 180)
    SetChrPos(0xF0, -780, 0, 31700, 0)
    SetChrPos(0xF1, -1500, 0, 30440, 0)
    Jump("loc_1260")

    label("loc_11DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121F")
    SetChrPos(0x10C, -1250, 0, 33430, 180)
    SetChrPos(0xEF, -780, 0, 31700, 0)
    SetChrPos(0xF1, -1500, 0, 30440, 0)
    Jump("loc_1260")

    label("loc_121F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1260")
    SetChrPos(0x10C, -1250, 0, 33430, 180)
    SetChrPos(0xEF, -780, 0, 31700, 0)
    SetChrPos(0xF0, -1500, 0, 30440, 0)

    label("loc_1260")

    OP_0D()
    Sleep(500)

    ChrTalk(    #29
        0x10C,
        (
            "#110F#5P好了……\x01",
            "这里就是司令部。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        (
            "#1079F#6P哦～……\x01",
            "的确是够大的。\x02\x03",

            "差不多有三层吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1838")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1397")

    ChrTalk(    #31
        0x101,
        (
            "#1015F#12P记得之前潜入的时候\x01",
            "好像只有一层而已……\x02\x03",

            "#1006F对了，\x01",
            "这么说某处有通往上层的楼梯吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1588")

    label("loc_1397")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1410")

    ChrTalk(    #32
        0x102,
        (
            "#1505F#12P之前潜入的时候\x01",
            "应该只有一层……\x02\x03",

            "#1500F这么说，\x01",
            "某处会有通往上层的楼梯吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1588")

    label("loc_1410")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1489")

    ChrTalk(    #33
        0x106,
        (
            "#053F#12P之前潜入的时候\x01",
            "好像只有一层……\x02\x03",

            "#050F这么说在某个地方\x01",
            "有通往上层的楼梯吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1588")

    label("loc_1489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1503")

    ChrTalk(    #34
        0x107,
        (
            "#063F#4P之前潜入的时候\x01",
            "好像只有一层而已……\x02\x03",

            "#560F啊，这么说\x01",
            "还有通往上层的楼梯……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1588")

    label("loc_1503")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1588")

    ChrTalk(    #35
        0x10B,
        (
            "#215F#4P之前被关进牢房里的时候\x01",
            "记得这里只有一层来着……\x02\x03",

            "#210F对了，是不是哪里\x01",
            "还有通往上层的楼梯？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1588")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_161B")

    ChrTalk(    #36
        0x10E,
        (
            "#179F#12P为了对付入侵者，\x01",
            "这里故意设计成了容易迷路的样子。\x02\x03",

            "#170F并排的几个门之间\x01",
            "应该有一个是通往上层的楼梯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_172B")

    label("loc_161B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B0")

    ChrTalk(    #37
        0x105,
        (
            "#1383F#12P似乎是为了对付入侵者\x01",
            "而设计成十分迷惑人的样子。\x02\x03",

            "#1160F并排的几个门之间\x01",
            "说不定有一个是通往上层的楼梯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_172B")

    label("loc_16B0")


    ChrTalk(    #38
        0x10C,
        (
            "#119F#5P是为了对付入侵者\x01",
            "才设计成这么迷惑人的样子。\x02\x03",

            "#110F并排的几个门之间\x01",
            "应该有一个是通往上层的楼梯。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_172B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1762")

    ChrTalk(    #39
        0x10B,
        "#210F#12P哦，原来如此啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1835")

    label("loc_1762")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1797")

    ChrTalk(    #40
        0x107,
        "#060F#12P是、是这样吗～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1835")

    label("loc_1797")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17CC")

    ChrTalk(    #41
        0x106,
        "#051F#12P原来如此啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1835")

    label("loc_17CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1800")

    ChrTalk(    #42
        0x102,
        "#1500F#12P原来如此……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1835")

    label("loc_1800")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1835")

    ChrTalk(    #43
        0x101,
        "#1011F#12P原、原来如此……\x02",
    )

    CloseMessageWindow()

    label("loc_1835")

    Jump("loc_1B98")

    label("loc_1838")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18EB")

    ChrTalk(    #44
        0x10C,
        "#115F#5P啊啊，就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10E,
        (
            "#170F#12P为了对付入侵者，\x01",
            "这里故意设计成了容易迷路的样子。\x02\x03",

            "并排的几个门之间\x01",
            "应该有一个是通往上层的楼梯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A32")

    label("loc_18EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_199E")

    ChrTalk(    #46
        0x10C,
        "#115F#5P啊啊，就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x105,
        (
            "#1160F#4P似乎是为了对付入侵者\x01",
            "而设计成十分迷惑人的样子。\x02\x03",

            "并排的几个门之间\x01",
            "说不定有一个是通往上层的楼梯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A32")

    label("loc_199E")


    ChrTalk(    #48
        0x10C,
        (
            "#115F#5P啊啊，就是这样。\x02\x03",

            "#110F是为了对付入侵者\x01",
            "才设计成这么迷惑人的样子。\x02\x03",

            "并排的几个门之间\x01",
            "应该有一个是通往上层的楼梯。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A66")

    ChrTalk(    #49
        0x10F,
        "#1448F#12P原来如此……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B98")

    label("loc_1A66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A9C")

    ChrTalk(    #50
        0x10A,
        "#816F#4P原、原来如此……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B98")

    label("loc_1A9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AD4")

    ChrTalk(    #51
        0x103,
        "#1525F#12P唔，原来如此啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B98")

    label("loc_1AD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B07")

    ChrTalk(    #52
        0x108,
        "#070F#12P原来如此啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B98")

    label("loc_1B07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3F")

    ChrTalk(    #53
        0x104,
        "#1541F#12P呼，原来如此啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B98")

    label("loc_1B3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B76")

    ChrTalk(    #54
        0x10D,
        "#277F#12P……原来如此啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B98")

    label("loc_1B76")


    ChrTalk(    #55
        0x109,
        "#1060F#6P原来如此……\x02",
    )

    CloseMessageWindow()

    label("loc_1B98")


    ChrTalk(    #56
        0x10C,
        "#116F#5P……好吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10C, 0, 400)
    Sleep(300)

    def lambda_1BC9():
        OP_6D(400, 0, 34740, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1BC9)
    OP_8E(0x10C, 0xFFFFFBFA, 0x1F4, 0x8976, 0x7D0, 0x0)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #57
        "\x07\x05理查德使用了司令部的钥匙。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0x10C,
        (
            "#115F#5P……诸位。\x02\x03",

            "在这前方等待我们的，\x01",
            "想必是更加严峻的试炼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10C, 180, 400)
    Sleep(300)

    ChrTalk(    #59
        0x10C,
        (
            "#112F#5P然而，\x01",
            "即使如此我们也只能迎接挑战。\x02\x03",

            "#114F──上吧，诸位！\x02\x03",

            "穿越阻挡在前的屏障，\x01",
            "获取驱散阴影的光辉！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetMessageWindowPos(400, 200, -1, -1)
    SetChrName("伙伴们")

    AnonymousTalk(    #60
        "\x07\x00#4S是！\x02",
    )

    Jump("loc_1D70")

    label("loc_1D70")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2B1E)
    OP_71(0x1001, 0x0)
    ExitThread()
    OP_64(0x1, 0x1)
    OP_6D(-1110, 0, 33110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1110, 0, 33110, 0)
    SetChrPos(0x1, -1110, 0, 33110, 0)
    SetChrPos(0x2, -1110, 0, 33110, 0)
    SetChrPos(0x3, -1110, 0, 33110, 0)
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

    label("loc_1E65")

    TalkEnd(0xFF)
    Return()

    # Function_6_10EC end

    SaveToFile()

Try(main)
