from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5415   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5415.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60114",
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
        'Loewe',                                # 9
        'Schwarzritter',                        # 10
        'Dragion Type-1',                       # 11
        'Dragion Type-2',                       # 12
        'Rufina',                               # 13
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
        'ED6_DT27/CH03440 ._CH',             # 00
        'ED6_DT27/CH04450 ._CH',             # 01
        'ED6_DT27/CH04454 ._CH',             # 02
        'ED6_DT27/CH04455 ._CH',             # 03
        'ED6_DT26/CH20710 ._CH',             # 04
        'ED6_DT26/CH20711 ._CH',             # 05
        'ED6_DT27/CH03940 ._CH',             # 06
        'ED6_DT26/CH20733 ._CH',             # 07
        'ED6_DT27/CH04082 ._CH',             # 08
        'ED6_DT27/CH04080 ._CH',             # 09
        'ED6_DT26/CH20731 ._CH',             # 0A
        'ED6_DT26/CH20734 ._CH',             # 0B
        'ED6_DT26/CH20735 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT27/CH03440P._CP',             # 00
        'ED6_DT27/CH04450P._CP',             # 01
        'ED6_DT27/CH04454P._CP',             # 02
        'ED6_DT27/CH04455P._CP',             # 03
        'ED6_DT26/CH20710P._CP',             # 04
        'ED6_DT26/CH20711P._CP',             # 05
        'ED6_DT27/CH03940P._CP',             # 06
        'ED6_DT26/CH20733P._CP',             # 07
        'ED6_DT27/CH04082P._CP',             # 08
        'ED6_DT27/CH04080P._CP',             # 09
        'ED6_DT26/CH20731P._CP',             # 0A
        'ED6_DT26/CH20734P._CP',             # 0B
        'ED6_DT26/CH20735P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0xC5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -4250,
        Y                   = 14000,
        Z                   = -17850,
        Range               = 3950,
        Unknown_10          = 0x4650,
        Unknown_14          = 0xFFFFC84C,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    ScpFunction(
        "Function_0_1D2",          # 00, 0
        "Function_1_223",          # 01, 1
        "Function_2_258",          # 02, 2
        "Function_3_269",          # 03, 3
        "Function_4_2EDB",         # 04, 4
        "Function_5_5471",         # 05, 5
        "Function_6_54A8",         # 06, 6
        "Function_7_54CB",         # 07, 7
        "Function_8_6212",         # 08, 8
        "Function_9_8F86",         # 09, 9
    )


    def Function_0_1D2(): pass

    label("Function_0_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_1EC")
    OP_A3(0x2506)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_222")

    label("loc_1EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_206")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_222")

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_222")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_222")

    Return()

    # Function_0_1D2 end

    def Function_1_223(): pass

    label("Function_1_223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248")
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_248")

    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x89, 0x0)
    OP_82(0x8A, 0x0)
    Return()

    # Function_1_223 end

    def Function_2_258(): pass

    label("Function_2_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_260")
    Return()

    label("loc_260")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_258 end

    def Function_3_269(): pass

    label("Function_3_269")

    EventBegin(0x0)
    LoadEffect(0x0, "monster\\ms30803a.eff")
    LoadEffect(0x1, "map\\mp021_00.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    LoadEffect(0x3, "scraft\\sc000_33.eff")
    LoadEffect(0x4, "monster\\ms30803c.eff")
    LoadEffect(0x5, "monster\\ms30803d.eff")
    LoadEffect(0x6, "map\\mpM54_02")
    OP_E0(238, 0x4D, 0x2)
    OP_E0(238, 0x4E, 0x3)
    OP_E0(239, 0x4F, 0x2)
    OP_E0(239, 0x50, 0x3)
    OP_E0(240, 0x51, 0x2)
    OP_E0(240, 0x52, 0x3)
    OP_E0(241, 0x53, 0x2)
    OP_E0(241, 0x54, 0x3)
    Sleep(500)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 0, 15550, 3500, 180)
    SetChrSubChip(0x10, 0)

    NpcTalk(    #0
        0x10,
        "Man's Voice",
        (
            "\x07\x05#4PWelcome, orphan of a lost village.\x02\x03",

            "Greetings also to you, one who seeks atonement\x01",
            "for his past transgressions, a Stigma forever at\x01",
            "his back.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_486")

    label("loc_41F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_447")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_486")

    label("loc_447")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46F")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_486")

    label("loc_46F")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_486")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B3")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51A")

    label("loc_4B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DB")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51A")

    label("loc_4DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_503")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51A")

    label("loc_503")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_51A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_547")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5AE")

    label("loc_547")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56F")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5AE")

    label("loc_56F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_597")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5AE")

    label("loc_597")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5AE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DB")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_642")

    label("loc_5DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_603")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_642")

    label("loc_603")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_642")

    label("loc_62B")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_642")

    Sleep(1000)

    def lambda_64D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_64D)

    def lambda_65F():
        OP_6D(0, 15550, 4000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_65F)

    def lambda_677():
        OP_67(0, 2960, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_677)

    def lambda_68F():
        OP_6B(1930, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_68F)

    def lambda_69F():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_69F)

    def lambda_6AF():
        OP_6E(444, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_6AF)

    def lambda_6BF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_6BF)

    def lambda_6CD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_6CD)

    def lambda_6DB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_6DB)

    def lambda_6E9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_6E9)
    WaitChrThread(0xEE, 0x0)
    SetChrPos(0x109, 500, 15550, -8540, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_729")
    SetChrPos(0xEF, -300, 15550, -8540, 0)
    Jump("loc_76A")

    label("loc_729")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74B")
    SetChrPos(0xF0, -300, 15550, -8540, 0)
    Jump("loc_76A")

    label("loc_74B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76A")
    SetChrPos(0xF1, -300, 15550, -8540, 0)

    label("loc_76A")

    Sleep(300)

    ChrTalk(    #1
        0x102,
        "#1502F#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        "#1069F#5PSorry for the wait!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(660, 15550, -130, 0)
    OP_67(0, 4750, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(485, 0)
    SetChrPos(0x109, 910, 15550, -9540, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_840")
    SetChrPos(0xEF, -590, 15550, -8650, 0)
    SetChrPos(0xF0, 830, 15550, -11370, 0)
    SetChrPos(0xF1, -1590, 15550, -11870, 0)
    Jump("loc_8C5")

    label("loc_840")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_884")
    SetChrPos(0xF0, -590, 15550, -8650, 0)
    SetChrPos(0xEF, 830, 15550, -11370, 0)
    SetChrPos(0xF1, -1590, 15550, -11870, 0)
    Jump("loc_8C5")

    label("loc_884")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C5")
    SetChrPos(0xF1, -590, 15550, -8650, 0)
    SetChrPos(0xEF, 830, 15550, -11370, 0)
    SetChrPos(0xF0, -1590, 15550, -11870, 0)

    label("loc_8C5")


    def lambda_8CB():
        OP_6B(2100, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_8CB)
    SetChrPos(0x10, 0, 15550, 3800, 180)

    def lambda_8EC():
        OP_8F(0xFE, 0xFFFFFFF6, 0x3CBE, 0xFFFFEF5C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8EC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_963")

    def lambda_915():
        OP_8F(0xFE, 0xFFFFFA2E, 0x3CBE, 0xFFFFEFFC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_915)

    def lambda_930():
        OP_8F(0xFE, 0xFFFFFF6A, 0x3CBE, 0xFFFFE980, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_930)

    def lambda_94B():
        OP_8F(0xFE, 0xFFFFF84E, 0x3CBE, 0xFFFFE96C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_94B)
    Jump("loc_A24")

    label("loc_963")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C5")

    def lambda_977():
        OP_8F(0xFE, 0xFFFFFA2E, 0x3CBE, 0xFFFFEFFC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_977)

    def lambda_992():
        OP_8F(0xFE, 0xFFFFFF6A, 0x3CBE, 0xFFFFE980, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_992)

    def lambda_9AD():
        OP_8F(0xFE, 0xFFFFF84E, 0x3CBE, 0xFFFFE96C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_9AD)
    Jump("loc_A24")

    label("loc_9C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A24")

    def lambda_9D9():
        OP_8F(0xFE, 0xFFFFFA2E, 0x3CBE, 0xFFFFEFFC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_9D9)

    def lambda_9F4():
        OP_8F(0xFE, 0xFFFFFF6A, 0x3CBE, 0xFFFFE980, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_9F4)

    def lambda_A0F():
        OP_8F(0xFE, 0xFFFFF84E, 0x3CBE, 0xFFFFE96C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_A0F)

    label("loc_A24")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(500)

    NpcTalk(    #3
        0x10,
        "Schwarzritter",
        (
            "\x07\x05#1590F#5PCongratulations on moving your pieces this far\x01",
            "across the game board.\x02\x03",

            "Should you defeat me, the final guardian, the end\x01",
            "of this plane will finally be in sight.\x02\x03",

            "#1591FHeh. Of course, that is a very big 'if.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#1502F#6P...\x02\x03",

            "#1505FCan I ask you one thing before we begin?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(    #5
        0x10,
        "Schwarzritter",
        "\x07\x05#1592F#5POh?\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1503F#6P...\x02\x03",

            "#1505FWhy?\x02\x03",

            "#1502FWhy do you wear that mask and hide your face\x01",
            "from us?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x10,
        "Schwarzritter",
        (
            "\x07\x05#1591F#5PHaha... What a foolish question.\x02\x03",

            "Because that is the will of my lord. What other\x01",
            "reason could there possibly be?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #8
        0x102,
        "#1506F#6PThe real one!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #9
        0x102,
        (
            "#1505F#6PYour reason for being here is that the Lord of\x01",
            "Phantasma wanted you to be, I don't doubt that...\x02\x03",

            "#1506F...but you hiding your face from us isn't their will\x01",
            "at all!\x02\x03",

            "Enough with the lies!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #10
        0x10,
        "Schwarzritter",
        "\x07\x05#1590F#5P...\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        "#1067F#12PJoshua...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E21")

    ChrTalk(    #12
        0x101,
        "#1003F#12PJoshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_E21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E4A")

    ChrTalk(    #13
        0x10B,
        "#215F#12PJoshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_E4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E74")

    ChrTalk(    #14
        0x105,
        "#1169F#12PJoshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_E74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9D")

    ChrTalk(    #15
        0x107,
        "#063F#12PJoshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_E9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC7")

    ChrTalk(    #16
        0x103,
        "#1532F#12PJoshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_EC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF1")

    ChrTalk(    #17
        0x104,
        "#1551F#12PJoshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_EF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F1F")

    ChrTalk(    #18
        0x106,
        "#552F#12PJoshua, you...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_F1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4D")

    ChrTalk(    #19
        0x108,
        "#572F#12PJoshua, you...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_F4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F7B")

    ChrTalk(    #20
        0x10E,
        "#175F#12PJoshua, you...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_F7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA4")

    ChrTalk(    #21
        0x10D,
        "#276F#12PJoshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_FA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FCD")

    ChrTalk(    #22
        0x10C,
        "#116F#12PJoshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_FCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF7")

    ChrTalk(    #23
        0x110,
        "#1300F#12PJoshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_FF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101D")

    ChrTalk(    #24
        0x10A,
        "#1317F#12PU-Umm...\x02",
    )

    CloseMessageWindow()

    label("loc_101D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1052")

    ChrTalk(    #25
        0x10F,
        "#1802F#12P(What does he mean?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_1052")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_107D")

    ChrTalk(    #26
        0x10A,
        "#1317F#12P(U-Umm...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_107D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A1")

    ChrTalk(    #27
        0x110,
        "#1300F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_10A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C4")

    ChrTalk(    #28
        0x10C,
        "#115F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_10C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E7")

    ChrTalk(    #29
        0x10D,
        "#272F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_10E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110A")

    ChrTalk(    #30
        0x10E,
        "#176F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_110A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112D")

    ChrTalk(    #31
        0x108,
        "#074F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_112D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1150")

    ChrTalk(    #32
        0x106,
        "#552F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_1150")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1174")

    ChrTalk(    #33
        0x104,
        "#1551F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_1174")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1198")

    ChrTalk(    #34
        0x103,
        "#1532F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_1198")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C1")

    ChrTalk(    #35
        0x107,
        "#063F#12PJoshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_11C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E5")

    ChrTalk(    #36
        0x105,
        "#1169F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_11E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1205")

    ChrTalk(    #37
        0x10B,
        "#215F#12P...\x02",
    )

    CloseMessageWindow()

    label("loc_1205")


    ChrTalk(    #38
        0x102,
        (
            "#1505F#6PYou all knew, huh?\x02\x03",

            "#1514FSorry... My own inability to face reality has\x01",
            "only made things harder for everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        (
            "#1075F#12PHey! Don't try and shoulder all the blame for\x01",
            "this yourself.\x02\x03",

            "#1840FI think we all had our doubts. I know I did.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1336")

    ChrTalk(    #40
        0x101,
        "#1025F#12PYeah. Kevin's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DB")

    label("loc_1336")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1361")

    ChrTalk(    #41
        0x10B,
        "#413F#12PHe's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DB")

    label("loc_1361")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138C")

    ChrTalk(    #42
        0x105,
        "#1382F#12P...Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DB")

    label("loc_138C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B3")

    ChrTalk(    #43
        0x107,
        "#562F#12PYeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DB")

    label("loc_13B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DC")

    ChrTalk(    #44
        0x103,
        "#1534F#12P...Yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DB")

    label("loc_13DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1409")

    ChrTalk(    #45
        0x104,
        "#1545F#12PHeh. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DB")

    label("loc_1409")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1438")

    ChrTalk(    #46
        0x106,
        "#556F#12P...Pretty much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DB")

    label("loc_1438")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1460")

    ChrTalk(    #47
        0x108,
        "#573F#12P...Yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DB")

    label("loc_1460")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_148A")

    ChrTalk(    #48
        0x10E,
        "#170F#12P...Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DB")

    label("loc_148A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14B4")

    ChrTalk(    #49
        0x10D,
        "#277F#12P...Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DB")

    label("loc_14B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14DB")

    ChrTalk(    #50
        0x10C,
        "#119F#12P...Indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_14DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1551")

    ChrTalk(    #51
        0x110,
        (
            "#268F#12PI figured it out from the moment we met.\x02\x03",

            "#1300FI just...couldn't bring myself to say it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1551")


    NpcTalk(    #52
        0x10,
        "Schwarzritter",
        (
            "\x07\x05#1590F#5PYou seem to think you've worked something out,\x01",
            "but I haven't got the faintest idea as to what.\x02\x03",

            "#1591FIf you're so sure you're right, why not go ahead\x01",
            "and say it?\x02\x03",

            "That is, if you feel you honestly have the resolve\x01",
            "to do so.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#1505F#6PI won't.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #54
        0x10,
        "Schwarzritter",
        "\x07\x05#1592F#5P...You won't?\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#1514F#6PWhy state the obvious when I'll see for myself\x01",
            "after cracking that mask to bits, anyway?\x02\x03",

            "What matters most right now is that if we can't\x01",
            "defeat you, there's no future for any of us.\x02\x03",

            "#1513FSo right now, I'm just going to leave who you\x01",
            "really are out of the equation.\x02\x03",

            "Not because I'm afraid to face up to the truth\x01",
            "or because I don't know what to do in the face\x01",
            "of it...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)

    def lambda_1845():
        OP_6B(2000, 500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1845)
    OP_22(0x1F5, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186F")
    SetChrChipByIndex(0x102, 15)
    SetChrSubChip(0x102, 0)
    Jump("loc_18A2")

    label("loc_186F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_188A")
    SetChrChipByIndex(0x102, 17)
    SetChrSubChip(0x102, 0)
    Jump("loc_18A2")

    label("loc_188A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A2")
    SetChrChipByIndex(0x102, 19)
    SetChrSubChip(0x102, 0)

    label("loc_18A2")

    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x102,
        (
            "#1506F#6P#2S...but because I must--and will--defeat you and\x01",
            "overcome this trial before me!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #57
        0x109,
        (
            "#1840F#12P...You're a hell of a standup guy,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A6")

    ChrTalk(    #58
        0x101,
        (
            "#1012F#12PI'm so proud of you...\x02\x03",

            "#1006FHeck yeah! I'm in!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E5")

    ChrTalk(    #59
        0x108,
        "#071F#12PHaha. Glad to see you so fired up.\x02",
    )

    CloseMessageWindow()

    label("loc_19E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A19")

    ChrTalk(    #60
        0x10D,
        "#275F#12PHeh. That's the spirit.\x02",
    )

    CloseMessageWindow()

    label("loc_1A19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A75")

    ChrTalk(    #61
        0x106,
        (
            "#051F#12PHeh. Same here. I've still got an unpaid debt\x01",
            "to this guy, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AEC")

    ChrTalk(    #62
        0x10E,
        (
            "#179F#12PYou have my sword, so that we might once\x01",
            "more drive away the shadow that threatens\x01",
            "Liberl!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3F")

    ChrTalk(    #63
        0x10F,
        (
            "#1447F#12PI, too, intend to fight so that we may see \x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B97")

    ChrTalk(    #64
        0x10C,
        (
            "#118F#12PIt's time to pay you back for your role in the\x01",
            "coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BFE")

    ChrTalk(    #65
        0x103,
        (
            "#1521F#12PI wouldn't be much of a big sister if\x01",
            "I didn't back you up here, would I?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C52")

    ChrTalk(    #66
        0x104,
        (
            "#1541F#12PI shall stand by your side and support you--\x01",
            "for love!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA7")

    ChrTalk(    #67
        0x105,
        (
            "#1168F#12PHeehee. I'll be more than happy to fight\x01",
            "alongside you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CDF")

    ChrTalk(    #68
        0x107,
        "#066F#12PI'm going to help you, too!\x02",
    )

    CloseMessageWindow()

    label("loc_1CDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D36")

    ChrTalk(    #69
        0x10B,
        (
            "#415F#12PHaha. Don't forget about me. I'll back you up\x01",
            "all the way!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D81")

    ChrTalk(    #70
        0x110,
        "#261F#12PHeehee. I suppose I don't mind playing backup.\x02",
    )

    CloseMessageWindow()

    label("loc_1D81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE6")

    ChrTalk(    #71
        0x10A,
        (
            "#819F#12PI-I'm not really sure what's going on,\x01",
            "but I've obviously got your back!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE6")

    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 13)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E38")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 17)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 19)
    SetChrSubChip(0xF1, 0)
    Jump("loc_1E9D")

    label("loc_1E38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6C")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 15)
    SetChrSubChip(0xEF, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 19)
    SetChrSubChip(0xF1, 0)
    Jump("loc_1E9D")

    label("loc_1E6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E9D")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 15)
    SetChrSubChip(0xEF, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 17)
    SetChrSubChip(0xF0, 0)

    label("loc_1E9D")

    OP_0D()
    Sleep(500)

    NpcTalk(    #72
        0x10,
        "Schwarzritter",
        "\x07\x05#1590F#5PHaha...\x07\x00\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #73
        0x10,
        "Schwarzritter",
        "\x07\x05#1591F#5P#4SHahahahaha!\x07\x00\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    Fade(500)

    def lambda_1F20():
        OP_6D(800, 15550, 1000, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1F20)

    def lambda_1F38():
        OP_6B(1950, 500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1F38)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #74
        0x10,
        "Schwarzritter",
        (
            "\x07\x05#1591F#5PI didn't think that was all it took to get your\x01",
            "fighting spirit back!\x02\x03",

            "#1593FVery well, then--do as you will! Defeat me,\x01",
            "and break this mask!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_20(0x5DC)
    Fade(500)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)

    def lambda_2024():

        label("loc_2024")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2024")

    QueueWorkItem2(0x10, 3, lambda_2024)
    PlayEffect(0x2, 0x7, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x158, 0x1, 0x64)

    def lambda_2077():

        label("loc_2077")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2077")

    QueueWorkItem2(0x12, 3, lambda_2077)

    def lambda_2092():
        OP_6D(660, 15550, -130, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2092)

    def lambda_20AA():
        OP_67(0, 5700, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_20AA)

    def lambda_20C2():
        OP_6B(2590, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_20C2)

    def lambda_20D2():
        OP_6C(45000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_20D2)

    def lambda_20E2():
        OP_6E(508, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_20E2)
    Sleep(1000)
    OP_1D(0x77)
    Fade(500)
    OP_6D(660, 15550, -130, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(45000, 0)
    OP_6E(508, 0)

    def lambda_213B():

        label("loc_213B")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_213B")

    QueueWorkItem2(0x12, 3, lambda_213B)

    def lambda_2156():
        OP_6D(-4430, 30000, -5500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2156)

    def lambda_216E():
        OP_67(0, 6670, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_216E)

    def lambda_2186():
        OP_6B(8990, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2186)

    def lambda_2196():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2196)

    def lambda_21A6():
        OP_6E(543, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_21A6)
    Sleep(1500)
    PlayEffect(0x6, 0x6, 0xFF, 90890, 0, -133260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_2203():

        label("loc_2203")

        OP_7C(0x12C, 0x12C, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2203")

    QueueWorkItem2(0x12, 3, lambda_2203)
    OP_6D(-4430, 30000, -5500, 0)
    OP_67(0, 6670, -10000, 0)
    OP_6B(8990, 0)
    OP_6C(47000, 0)
    OP_6E(543, 0)

    def lambda_225B():
        OP_6D(-4430, 100000, -5500, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_225B)

    def lambda_2273():
        OP_67(0, -1670, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2273)

    def lambda_228B():
        OP_6B(9300, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_228B)

    def lambda_229B():
        OP_6C(25000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_229B)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -80850, 90000, -65000, 90)
    OP_A1(0x13, 0x1)
    OP_D1(19, 10000, 90000, 30000, 0)
    OP_72(0x401, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 320)
    OP_70(0x1, 0x140)
    OP_22(0x159, 0x0, 0x64)
    OP_22(0x2D3, 0x0, 0x64)

    def lambda_22FD():
        OP_D1(254, 30000, 80000, 90000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_22FD)
    OP_98(0x0, 0x13)
    OP_98(0x1, 0x7530, 0x7530, 0xFFFFC568)
    OP_98(0x1, 0xFFFFD8F0, 0xC350, 0x9C40)

    def lambda_2337():
        OP_98(0x2, 0xFE, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2337)
    WaitChrThread(0x13, 0x3)

    def lambda_234C():
        OP_D1(254, -20000, -80000, 80000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_234C)
    WaitChrThread(0x13, 0x3)

    def lambda_236B():
        OP_D1(254, -60000, -140000, 60000, 500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_236B)
    WaitChrThread(0x13, 0x3)
    Fade(250)
    OP_82(0x80, 0x0)
    PlayEffect(0x3, 0x5, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0xEE, 0x0)
    OP_44(0xEE, 0x1)
    OP_44(0xEE, 0x2)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x1)
    OP_44(0x13, 0x0)

    def lambda_23DF():

        label("loc_23DF")

        OP_7C(0x96, 0x96, 0xBB8, 0x64)
        OP_48()
        Jump("loc_23DF")

    QueueWorkItem2(0x12, 3, lambda_23DF)
    OP_6D(92670, 20560, -131770, 0)
    OP_67(0, -77060, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(180000, 0)
    OP_6E(856, 0)
    SetChrPos(0x13, 90890, 70000, -133260, 90)
    OP_D1(19, 90000, 90000, 130000, 0)

    def lambda_245B():
        OP_D1(254, 90000, 90000, 30000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_245B)

    def lambda_2475():
        OP_8F(0xFE, 0x15F90, 0xFFFDB610, 0xFFFE320C, 0x15F90, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2475)

    def lambda_2490():
        OP_6B(800, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2490)
    Sleep(600)
    OP_22(0x2D3, 0x0, 0x64)
    Sleep(700)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x5, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEE, 0x1)
    OP_44(0xEE, 0x2)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x1)
    OP_44(0x13, 0x0)
    OP_44(0x12, 0x3)
    OP_6D(-120, 24500, 10100, 0)
    OP_67(0, -1000, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(0, 0)
    OP_6E(360, 0)

    def lambda_2540():
        OP_6D(0, 18000, 8000, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2540)

    def lambda_2558():
        OP_67(0, 3300, -10000, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2558)

    def lambda_2570():
        OP_6B(2900, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2570)

    def lambda_2580():
        OP_6E(380, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_2580)
    SetChrPos(0x10, 0, 15550, 4000, 180)
    SetChrPos(0x109, 900, 15550, -3420, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F0")
    SetChrPos(0xEF, -550, 15550, -3310, 0)
    SetChrPos(0xF1, -1220, 15550, -5140, 0)
    SetChrPos(0xF0, 1500, 15550, -5350, 0)
    Jump("loc_2675")

    label("loc_25F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2634")
    SetChrPos(0xF0, -550, 15550, -3310, 0)
    SetChrPos(0xF1, -1220, 15550, -5140, 0)
    SetChrPos(0xEF, 1500, 15550, -5350, 0)
    Jump("loc_2675")

    label("loc_2634")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2675")
    SetChrPos(0xF1, -550, 15550, -3310, 0)
    SetChrPos(0xF0, -1220, 15550, -5140, 0)
    SetChrPos(0xEF, 1500, 15550, -5350, 0)

    label("loc_2675")

    Sleep(500)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, 20000, 9090, 180)
    OP_A1(0x12, 0x0)
    OP_72(0x400, 0x0)
    ExitThread()
    OP_6F(0x0, 160)

    def lambda_26A8():
        OP_8F(0xFE, 0x0, 0x3CBE, 0x2382, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_26A8)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x23)
    OP_6F(0x0, 160)
    OP_70(0x0, 0x96)
    WaitChrThread(0x12, 0x0)
    OP_23(0x158)
    OP_22(0xEC, 0x0, 0x64)
    OP_22(0xC8, 0x0, 0x64)

    def lambda_26ED():

        label("loc_26ED")

        OP_7C(0x0, 0x5DC, 0x3E8, 0x12C)
        OP_48()
        Jump("loc_26ED")

    QueueWorkItem2(0x12, 3, lambda_26ED)
    PlayEffect(0x1, 0x0, 0x12, 0, -500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_2742():

        label("loc_2742")

        OP_7C(0x0, 0x3E8, 0x3E8, 0x12C)
        OP_48()
        Jump("loc_2742")

    QueueWorkItem2(0x12, 3, lambda_2742)
    Sleep(300)

    def lambda_2762():

        label("loc_2762")

        OP_7C(0x0, 0x1F4, 0x3E8, 0x12C)
        OP_48()
        Jump("loc_2762")

    QueueWorkItem2(0x12, 3, lambda_2762)
    Sleep(300)

    def lambda_2782():

        label("loc_2782")

        OP_7C(0x0, 0x12C, 0x3E8, 0x12C)
        OP_48()
        Jump("loc_2782")

    QueueWorkItem2(0x12, 3, lambda_2782)
    Sleep(300)

    def lambda_27A2():

        label("loc_27A2")

        OP_7C(0x0, 0x0, 0x3E8, 0x12C)
        OP_48()
        Jump("loc_27A2")

    QueueWorkItem2(0x12, 3, lambda_27A2)
    OP_44(0x12, 0x3)
    WaitChrThread(0xEE, 0x0)
    OP_82(0x0, 0x2)
    Fade(1000)
    OP_22(0xF3, 0x0, 0x64)
    Play3DEffect(0x0, 0x4, 0x0, "Frame14_Bone__13_", 0x0, 0xF0, 0xFFFFFFBA, 0xB4, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x4, 0x5, 0x0, "Frame79_Bone__78_", 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x258, 0x258, 0x258, 0x0)
    Play3DEffect(0x5, 0x6, 0x0, "Frame82_Bone__81_", 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x258, 0x258, 0x258, 0x0)
    OP_0D()
    OP_43(0x12, 0x0, 0x0, 0x5)
    WaitChrThread(0xEE, 0x0)
    Sleep(1500)

    def lambda_288D():
        OP_6D(0, 16500, 5660, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_288D)

    def lambda_28A5():
        OP_67(0, 2000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_28A5)

    def lambda_28BD():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_28BD)

    def lambda_28CD():
        OP_6E(380, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_28CD)
    OP_82(0x7, 0x2)
    OP_44(0x10, 0x3)
    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_290B")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2972")

    label("loc_290B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2933")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2972")

    label("loc_2933")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295B")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2972")

    label("loc_295B")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2972")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299F")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A06")

    label("loc_299F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29C7")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A06")

    label("loc_29C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29EF")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A06")

    label("loc_29EF")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2A06")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A33")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A9A")

    label("loc_2A33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A5B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A9A")

    label("loc_2A5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A83")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A9A")

    label("loc_2A83")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2A9A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC7")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B2E")

    label("loc_2AC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AEF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B2E")

    label("loc_2AEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B17")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B2E")

    label("loc_2B17")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2B2E")

    Sleep(1000)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #75
        0x102,
        "#1506F#6PBlack Dragion!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x109,
        "#1063F#6PHere we go!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)

    def lambda_2B84():
        OP_6E(400, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2B84)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #77
        0x10,
        "Schwarzritter",
        (
            "\x07\x05#1591F#5PMy name is Schwarzritter, rider of the black\x01",
            "Dragion and guardian of the abyss.\x02\x03",

            "...And in accordance to my pact with the Lord\x01",
            "of Phantasma, I shall act as your next trial!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #78
        0x10,
        "Schwarzritter",
        "\x07\x05#1593F#5P#4SLet the battle begin!\x07\x00\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #79
        0x102,
        "#1506F#6PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x109,
        "#1069F#6PYou got it!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xEE, 0x0)
    PlayEffect(0x3, 0x0, 0xFF, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_2D31():
        OP_6D(0, 16600, 5610, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2D31)

    def lambda_2D49():
        OP_67(0, 2480, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2D49)

    def lambda_2D61():
        OP_6B(1780, 300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2D61)

    def lambda_2D71():
        OP_6E(465, 300)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_2D71)

    def lambda_2D81():
        OP_8F(0xFE, 0x212, 0x3CBE, 0x139C, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D81)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF8")

    def lambda_2DAA():
        OP_8F(0xFE, 0xFFFFFE98, 0x3CBE, 0x12CA, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2DAA)

    def lambda_2DC5():
        OP_8F(0xFE, 0x41A, 0x3CBE, 0x1072, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2DC5)

    def lambda_2DE0():
        OP_8F(0xFE, 0xFFFFFC54, 0x3CBE, 0xF5A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2DE0)
    Jump("loc_2EB9")

    label("loc_2DF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E5A")

    def lambda_2E0C():
        OP_8F(0xFE, 0xFFFFFE98, 0x3CBE, 0x12CA, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2E0C)

    def lambda_2E27():
        OP_8F(0xFE, 0x41A, 0x3CBE, 0x1072, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2E27)

    def lambda_2E42():
        OP_8F(0xFE, 0xFFFFFC54, 0x3CBE, 0xF5A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2E42)
    Jump("loc_2EB9")

    label("loc_2E5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB9")

    def lambda_2E6E():
        OP_8F(0xFE, 0xFFFFFE98, 0x3CBE, 0x12CA, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2E6E)

    def lambda_2E89():
        OP_8F(0xFE, 0x41A, 0x3CBE, 0x1072, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2E89)

    def lambda_2EA4():
        OP_8F(0xFE, 0xFFFFFC54, 0x3CBE, 0xF5A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2EA4)

    label("loc_2EB9")

    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2AE, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_269 end

    def Function_4_2EDB(): pass

    label("Function_4_2EDB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    Sleep(1000)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    LoadEffect(0x0, "map\\mp306_00.eff")
    LoadEffect(0x1, "map\\mp285_00.eff")
    LoadEffect(0x2, "map\\mp275_00.eff")
    OP_D2(0x70573, 0x70578, 0x6)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x400, 0x0)
    ExitThread()
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 15550, 0, 180)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 0)
    SetChrFlags(0x10, 0x800)
    SetChrFlags(0x10, 0x2)
    OP_43(0x10, 0x3, 0x0, 0x6)
    SetChrPos(0x14, 950, 15550, 650, 180)
    SetChrChipByIndex(0x14, 6)
    ClearChrFlags(0x14, 0x80)

    def lambda_2FAA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2FAA)
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 0, 0, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -600, 15550, -10410, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3045")
    SetChrPos(0xEF, 600, 15550, -10150, 0)
    SetChrPos(0xF0, -1100, 15550, -12150, 0)
    SetChrPos(0xF1, 1200, 15550, -12250, 0)
    Jump("loc_30CA")

    label("loc_3045")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3089")
    SetChrPos(0xF0, 600, 15550, -10150, 0)
    SetChrPos(0xEF, -1100, 15550, -12150, 0)
    SetChrPos(0xF1, 1200, 15550, -12250, 0)
    Jump("loc_30CA")

    label("loc_3089")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30CA")
    SetChrPos(0xF1, 600, 15550, -10150, 0)
    SetChrPos(0xEF, -1100, 15550, -12150, 0)
    SetChrPos(0xF0, 1200, 15550, -12250, 0)

    label("loc_30CA")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(0, 15550, -160, 0)
    OP_67(0, 4420, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(0, 0)
    OP_6E(400, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #81
        0x10,
        "Schwarzritter",
        "\x07\x0C#1605F#5P#40WHaha...\x07\x00\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(0, 15550, 340, 0)
    OP_67(0, 4330, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(0, 0)
    OP_6E(400, 0)
    Sleep(500)
    OP_99(0x10, 0x0, 0x5, 0x5DC)
    OP_22(0x12C, 0x0, 0x64)
    OP_0D()
    Sleep(1000)

    def lambda_31D0():
        OP_99(0xFE, 0x8, 0x15, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_31D0)
    Sleep(400)
    OP_22(0x179, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #82
        0x102,
        "#1504F#5P...!!\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    OP_1D(0x72)

    def lambda_3328():
        OP_6D(0, 15550, 1340, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3328)

    def lambda_3340():
        OP_67(0, 3900, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3340)

    def lambda_3358():
        OP_6B(1950, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3358)

    def lambda_3368():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3368)

    def lambda_3378():
        OP_6E(400, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3378)
    Sleep(1000)
    OP_99(0x10, 0x18, 0x1E, 0x5DC)
    OP_99(0x10, 0x1E, 0x21, 0x5DC)
    WaitChrThread(0xEE, 0x0)

    NpcTalk(    #83
        0x10,
        "Schwarzritter",
        (
            "\x07\x0C#1596F#5P#40WCongratulations. You did as you said you would.\x01",
            "You broke my mask.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x109,
        "#1840F#5PWe were right, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        "#1501F#5PIt really is you...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-330, 15550, -2570, 0)
    OP_67(0, 3600, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(315000, 0)
    OP_6E(490, 0)
    SetChrPos(0x10, 620, 15550, 0, 180)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 40)
    SetChrPos(0x109, 340, 15550, -6310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3503")
    SetChrPos(0xEF, 960, 15550, -5310, 0)
    SetChrPos(0xF0, 2090, 15550, -6550, 0)
    SetChrPos(0xF1, 1310, 15550, -7380, 0)
    Jump("loc_3588")

    label("loc_3503")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3547")
    SetChrPos(0xF0, 960, 15550, -5310, 0)
    SetChrPos(0xEF, 2090, 15550, -6550, 0)
    SetChrPos(0xF1, 1310, 15550, -7380, 0)
    Jump("loc_3588")

    label("loc_3547")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3588")
    SetChrPos(0xF1, 960, 15550, -5310, 0)
    SetChrPos(0xEF, 2090, 15550, -6550, 0)
    SetChrPos(0xF0, 1310, 15550, -7380, 0)

    label("loc_3588")


    def lambda_358E():
        OP_6D(-900, 15550, -250, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_358E)

    def lambda_35A6():
        OP_67(0, 4000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_35A6)

    def lambda_35BE():
        OP_6B(1900, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_35BE)

    def lambda_35CE():
        OP_6E(520, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_35CE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3604")

    def lambda_35EC():
        OP_8F(0xFE, 0x26C, 0x3CBE, 0xFFFFF4A2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_35EC)
    Jump("loc_3659")

    label("loc_3604")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3630")

    def lambda_3618():
        OP_8F(0xFE, 0x26C, 0x3CBE, 0xFFFFF4A2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3618)
    Jump("loc_3659")

    label("loc_3630")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3659")

    def lambda_3644():
        OP_8F(0xFE, 0x26C, 0x3CBE, 0xFFFFF4A2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3644)

    label("loc_3659")

    Sleep(200)

    def lambda_3664():
        OP_8F(0xFE, 0xFFFFFF38, 0x3CBE, 0xFFFFF0BA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3664)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36CA")
    Sleep(300)

    def lambda_3692():
        OP_8F(0xFE, 0x71C, 0x3CBE, 0xFFFFEE62, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3692)
    Sleep(100)

    def lambda_36B2():
        OP_8F(0xFE, 0x37A, 0x3CBE, 0xFFFFEB6A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_36B2)
    Jump("loc_3769")

    label("loc_36CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_371B")
    Sleep(300)

    def lambda_36E3():
        OP_8F(0xFE, 0x71C, 0x3CBE, 0xFFFFEE62, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_36E3)
    Sleep(100)

    def lambda_3703():
        OP_8F(0xFE, 0x37A, 0x3CBE, 0xFFFFEB6A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3703)
    Jump("loc_3769")

    label("loc_371B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3769")
    Sleep(300)

    def lambda_3734():
        OP_8F(0xFE, 0x71C, 0x3CBE, 0xFFFFEE62, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3734)
    Sleep(100)

    def lambda_3754():
        OP_8F(0xFE, 0x37A, 0x3CBE, 0xFFFFEB6A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3754)

    label("loc_3769")

    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(500)

    ChrTalk(    #86
        0x10,
        (
            "\x07\x0C#1599F#11P#40WI never thought I'd be so lucky to see you again.\x02\x03",

            "#1596FNot that I can imagine this reunion has much\x01",
            "meaning for you at this point.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#1513F#6PHaha... You have no idea...\x02\x03",

            "#1503F...\x02\x03",

            "I was...scared, I think.\x02\x03",

            "#1505FI might have been given the chance to meet you\x01",
            "again, but I knew from the start it was going to\x01",
            "be short lived.\x02\x03",

            "I knew I'd have to go through the pain of losing\x01",
            "you a second time...so I tried to pretend I had no\x01",
            "idea who you were to avoid it.\x02\x03",

            "That's why you ended up with that mask--it was\x01",
            "my own weakness and inability to face up to the\x01",
            "truth.\x02\x03",

            "#1514F...Right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x10,
        (
            "\x07\x0C#1597F#11P#40WPrecisely that.\x02\x03",

            "#1594FI was summoned within this world to act as the\x01",
            "final, strongest guardian. That much you already\x01",
            "know.\x02\x03",

            "It was the Lord of Phantasma who called me.\x02\x03",

            "#1597FBut they weren't the one who decided I should\x01",
            "wear this thing. That was likely all of you.\x02\x03",

            "This world changes as a result of one's thoughts\x01",
            "and desires; it's not at all impossible for that to\x01",
            "be the case.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        "#1503F#6PI thought so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10,
        (
            "\x07\x0C#1599F#11P#40WNow, thanks to your efforts, my job here is\x01",
            "finally done.\x02\x03",

            "#1596FHeh. To tell you the truth, with that Dragion to\x01",
            "support me, I didn't actually expect you to win.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        (
            "#1513F#6PHaha... I barely did.\x02\x03",

            "#1501FWith everyone here by my side, at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x10,
        (
            "\x07\x0C#1599F#11P#40WWell, working with others to achieve a goal isn't\x01",
            "a sign of weakness.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40CF")
    Sleep(500)

    ChrTalk(    #93
        0x10,
        (
            "\x07\x0C#1596F#11P#40WYou've become a lot stronger, too, Estelle Bright.\x01",
            "I'm impressed.\x02\x03",

            "You've still got some way to go before you can\x01",
            "equal your father, though.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#1016F#6PAhaha... No doubt. I won't get there by\x01",
            "rushing things.\x02\x03",

            "#1017FJust gotta keep at it one step at a time.\x02\x03",

            "And as long as I have Joshua, I'm sure\x01",
            "I'll get there eventually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        "#1501F#5PEstelle...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ECF")

    ChrTalk(    #96
        0x10,
        "\x07\x0C#1599F#11P#40WHaha... I hope you will.\x07\x00\x02",
    )

    CloseMessageWindow()
    Jump("loc_40CF")

    label("loc_3ECF")


    ChrTalk(    #97
        0x10,
        (
            "\x07\x0C#1599F#11P#40WHaha... I hope you will.\x02\x03",

            "#1594FLet me take this chance to thank you for all\x01",
            "you've done for Renne, too.\x02\x03",

            "I have to admit, I was a little concerned about\x01",
            "how she would fare without me...but I see I had\x01",
            "no reason to worry on that front.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1025F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10,
        (
            "\x07\x0C#1597F#11P#40WI can't imagine achieving what you want to\x01",
            "will be an easy task...\x02\x03",

            "#1596F...but I believe that the two of you can do it\x01",
            "if you put your minds to it. \x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x102,
        "#1514F#6PThanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1017F#6PWe won't let you down!\x02",
    )

    CloseMessageWindow()

    label("loc_40CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4440")
    Sleep(500)

    ChrTalk(    #102
        0x10,
        (
            "\x07\x0C#1596F#11P#40WSo, Agate Crosner...I see you've been able\x01",
            "to improve leaps and bounds since we last\x01",
            "crossed swords.\x02\x03",

            "You're actually swinging that heavy blade of\x01",
            "yours with a fair bit of skill now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x106,
        (
            "#051F#6PHaha. I don't think I'll ever get used to hearing\x01",
            "compliments come outta your mouth.\x02\x03",

            "#053FStill, I've got a long way to go as a swordsman,\x01",
            "just like I've got a long way to go as a guy.\x02\x03",

            "#556FI'll keep at it, though. Bit by bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10,
        (
            "\x07\x0C#1598F#11P#40W...That definitely wasn't the response I was\x01",
            "expecting.\x02\x03",

            "#1596FHeh. You were once so reckless, but now you\x01",
            "have all the composure of a man who's settled\x01",
            "down and started a family.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x106,
        "#055F#6PTh-The hell's that supposed to mean?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4440")

    ChrTalk(    #106
        0x107,
        "#064F#6P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        "\x07\x0C#1599F#11P#40W...Now I see why, too.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #108
        0x106,
        "#055F#6PWait a minute! What IS that supposed to mean?!\x02",
    )

    CloseMessageWindow()

    label("loc_4440")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_465E")
    Sleep(500)

    ChrTalk(    #109
        0x10,
        (
            "\x07\x0C#1596F#11P#40WAs for you, Tita Russell...I'm pleased to see\x01",
            "you seem to have found a path of your own,\x01",
            "too.\x02\x03",

            "I'm looking forward to seeing how well you\x01",
            "can compare to the Thirteen Factories.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x107,
        (
            "#067F#6PI-I'll try my best!\x02\x03",

            "#066FTh-Though I feel like my reason for working on\x01",
            "the Orbal Gear is kinda selfish...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10,
        (
            "\x07\x0C#1599F#11P#40WHeh. Deep down, everyone is selfish to at least\x01",
            "some degree. That's nothing to be ashamed of.\x02\x03",

            "#1596FJust follow your heart and do what you believe\x01",
            "in.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x107,
        "#560F#6P...Thank you.\x02",
    )

    CloseMessageWindow()

    label("loc_465E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4885")
    Sleep(500)

    ChrTalk(    #113
        0x10,
        (
            "\x07\x0C#1596F#11P#40WI can't say I ever expected to have the chance\x01",
            "to meet you again, either, Colonel Richard.\x02\x03",

            "Fate truly is a funny thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x10C,
        (
            "#119F#6PI quite agree, 2nd Lieutenant.\x02\x03",

            "#111FStill, I'm happy to have been able to come and\x01",
            "fight you.\x02\x03",

            "If nothing else, at least I now finally know what\x01",
            "you're truly capable of, and not just when you're\x01",
            "holding back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        (
            "\x07\x0C#1599F#11P#40WHaha. I hope you won't walk away disappointed.\x02\x03",

            "#1596FI certainly wasn't disappointed with your skills.\x01",
            "You learned from the Divine Blade well.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4885")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B2F")
    Sleep(500)

    ChrTalk(    #116
        0x110,
        "#1300F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x10,
        (
            "\x07\x0C#1597F#11P#40WAs for you, Renne...I never even had the chance\x01",
            "to say goodbye to you the first time, did I?\x02\x03",

            "#1594FI'm sorry. I wouldn't have chosen to leave you\x01",
            "that way.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x110,
        (
            "#268F#6PIt's not your fault.\x02\x03",

            "#265FBesides, if you and Joshua hadn't stepped in\x01",
            "and saved me, I'd still be alone today.\x02\x03",

            "#261FSo I'm not mad. I'll always be grateful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10,
        "\x07\x0C#1596F#11P#40W...Thank you.\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x110,
        (
            "#260F#6PHeehee. Under any other circumstances, I'd ask\x01",
            "for you to pat my head one last time...\x02\x03",

            "#263F...but those claws of yours look like they'd kinda\x01",
            "hurt, so maybe it's better if you don't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x10,
        "\x07\x0C#1599F#11P#40WHaha. I'm sorry there, too.\x07\x00\x02",
    )

    CloseMessageWindow()

    label("loc_4B2F")

    Sleep(500)

    ChrTalk(    #122
        0x10,
        (
            "\x07\x0C#1595F#11P#40WSo, Kevin Graham.\x02\x03",

            "Can you finally have complete confidence\x01",
            "in your theory?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x109,
        (
            "#1065F#6PYep. Every last shred of doubt in my mind is gone.\x02\x03",

            "#1840FI'll make sure everyone you care about gets home\x01",
            "safe and sound.\x02\x03",

            "You can count on it, Loewe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x10,
        (
            "\x07\x0C#1597F#11P#40W...In that case, count on you I shall.\x02\x03",

            "#1594FI think this goes without saying, but the Lord\x01",
            "of Phantasma is no ordinary foe.\x02\x03",

            "This won't be easy for you...but don't mistake\x01",
            "what you need to do.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x109,
        "#1075F#6PThanks. I'll take the warning to heart.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EB6")

    ChrTalk(    #126
        0x10F,
        (
            "#1802F#6PW-Wait... What are you both talking about?\x02\x03",

            "And I still haven't had the chance to ask you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x10,
        (
            "\x07\x0C#1597F#11P#40W...My apologies, Ries Argent.\x02\x03",

            "I know what you want to ask, but the rules I am\x01",
            "still bound by forbid me from answering.\x02\x03",

            "#1596FYou'll have your answer soon enough. You can\x01",
            "rest assured of that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x10F,
        "#1444F#6PWhat...?\x02",
    )

    CloseMessageWindow()

    label("loc_4EB6")

    Sleep(300)
    Fade(500)

    def lambda_4EC6():
        OP_6B(1850, 500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4EC6)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, 0, 0, 100, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    WaitChrThread(0xEE, 0x2)

    def lambda_4F1A():
        OP_6B(1700, 20000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4F1A)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F51")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4FB8")

    label("loc_4F51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F79")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4FB8")

    label("loc_4F79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FA1")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4FB8")

    label("loc_4FA1")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4FB8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FE5")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_504C")

    label("loc_4FE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_500D")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_504C")

    label("loc_500D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5035")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_504C")

    label("loc_5035")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_504C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5079")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_50E0")

    label("loc_5079")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50A1")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_50E0")

    label("loc_50A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50C9")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_50E0")

    label("loc_50C9")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_50E0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_510D")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5174")

    label("loc_510D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5135")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5174")

    label("loc_5135")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_515D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5174")

    label("loc_515D")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5174")

    Sleep(1500)

    ChrTalk(    #129
        0x102,
        "#1503F#6P...I guess this is it, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x10,
        (
            "\x07\x0C#1599F#11P#40WHaha... I'm afraid so.\x02\x03",

            "#1596FI can finally return to where I belong.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x102,
        (
            "#1513F#6P#40WYeah...\x02\x03",

            "#1514FI delivered your sword to Karin, by the way.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)

    ChrTalk(    #132
        0x10,
        (
            "\x07\x0C#1599F#11P#40WThank you...\x02\x03",

            "Don't worry about us. We'll be resting in peace\x01",
            "together.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    Sleep(300)

    ChrTalk(    #133
        0x10,
        "\x07\x0C#1604F#11P#60WWell...Joshua...\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x102,
        "#1516F#6P#40W...Yeah.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #135
        0x102,
        "#1501F#6P#40WGoodbye, Loewe.\x02",
    )

    CloseMessageWindow()

    def lambda_5382():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5382)
    Sleep(1000)
    Sleep(300)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Fade(500)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x2, 0x2, 0x10, 0, 500, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x3C)
    OP_22(0x1B0, 0x0, 0x64)

    def lambda_5407():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5407)
    Sleep(500)

    def lambda_541E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_541E)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x2)

    def lambda_5436():
        OP_6B(3000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_5436)
    OP_0D()
    OP_44(0x10, 0x3)
    Sleep(1000)
    Sleep(3000)
    SetChrFlags(0x10, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M4111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_2EDB end

    def Function_5_5471(): pass

    label("Function_5_5471")

    OP_73(0x0)
    Sleep(1500)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 150)
    OP_70(0x0, 0x8C)
    OP_D8(0x0, 0x5DC)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x14)
    Return()

    # Function_5_5471 end

    def Function_6_54A8(): pass

    label("Function_6_54A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54CA")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("Function_6_54A8")

    label("loc_54CA")

    Return()

    # Function_6_54A8 end

    def Function_7_54CB(): pass

    label("Function_7_54CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -200, 15550, -3910, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5635")
    SetChrPos(0xEF, 810, 15550, -1890, 0)
    SetChrPos(0xF0, 1820, 15550, -4510, 0)
    SetChrPos(0xF1, 890, 15550, -5270, 0)
    Jump("loc_56BA")

    label("loc_5635")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5679")
    SetChrPos(0xF0, 810, 15550, -1890, 0)
    SetChrPos(0xEF, 1820, 15550, -4510, 0)
    SetChrPos(0xF1, 890, 15550, -5270, 0)
    Jump("loc_56BA")

    label("loc_5679")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56BA")
    SetChrPos(0xF1, 810, 15550, -1890, 0)
    SetChrPos(0xEF, 1820, 15550, -4510, 0)
    SetChrPos(0xF0, 890, 15550, -5270, 0)

    label("loc_56BA")

    OP_6D(-70, 15550, 2000, 0)
    OP_67(0, 5180, -10000, 0)
    OP_6B(1630, 0)
    OP_6C(315000, 0)
    OP_6E(520, 0)
    Sleep(2000)

    def lambda_5702():
        OP_6D(-70, 15550, -1200, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5702)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(150)

    ChrTalk(    #136
        0x102,
        "#1516F#5P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5762")

    ChrTalk(    #137
        0x110,
        "#1309F#6P...Loewe...\x02",
    )

    CloseMessageWindow()

    label("loc_5762")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5782")

    ChrTalk(    #138
        0x10F,
        "#1445F#6P...\x02",
    )

    CloseMessageWindow()

    label("loc_5782")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57A1")

    ChrTalk(    #139
        0x106,
        "#552F#6P...\x02",
    )

    CloseMessageWindow()

    label("loc_57A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57D1")

    ChrTalk(    #140
        0x101,
        "#1027F#6PJoshua... Umm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_57D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_580A")

    ChrTalk(    #141
        0x10B,
        "#212F#6PYou gonna be okay, Joshua?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_580A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5839")

    ChrTalk(    #142
        0x107,
        "#562F#6PUmm... Joshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_5839")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5869")

    ChrTalk(    #143
        0x105,
        "#1169F#6PJoshua... Umm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_5869")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5899")

    ChrTalk(    #144
        0x103,
        "#1532F#6PJoshua... Umm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_5899")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58D3")

    ChrTalk(    #145
        0x104,
        "#1542F#6PAre you all right, Joshua?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_58D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5902")

    ChrTalk(    #146
        0x10A,
        "#813F#6PJoshua... Umm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_5902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_593B")

    ChrTalk(    #147
        0x108,
        "#072F#6PAre you all right, Joshua?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_593B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5974")

    ChrTalk(    #148
        0x10E,
        "#178F#6PAre you all right, Joshua?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_5974")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59A5")

    ChrTalk(    #149
        0x10D,
        "#270F#6PAre you all right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_59A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59DE")

    ChrTalk(    #150
        0x10C,
        "#112F#6PAre you all right, Joshua?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_59DE")


    ChrTalk(    #151
        0x109,
        "#1063F#6PYou gonna be okay, Joshua?\x02",
    )

    CloseMessageWindow()

    label("loc_5A07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B38")

    ChrTalk(    #152
        0x102,
        (
            "#1501F#5PI'm fine. This was always how this was going\x01",
            "to end.\x02\x03",

            "#1513FBesides, the last time I lost him, all I did was\x01",
            "act like a child who couldn't let go and worry\x01",
            "him in his final moments...\x02\x03",

            "This time, I was actually able to properly say\x01",
            "goodbye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C35")

    label("loc_5B38")


    ChrTalk(    #153
        0x102,
        (
            "#1501F#5PI'm fine. This was always how this was going\x01",
            "to end.\x02\x03",

            "#1513FBesides, the last time I lost him, all I did was\x01",
            "act like a child who couldn't let go and worry\x01",
            "him in his final moments.\x02\x03",

            "This time, I was actually able to properly say\x01",
            "goodbye.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C59")

    ChrTalk(    #154
        0x110,
        "#260F#6P...Yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_5C59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C7E")

    ChrTalk(    #155
        0x105,
        "#1382F#6P...Yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_5C7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CA2")

    ChrTalk(    #156
        0x107,
        "#066F#6P...Yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_5CA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CD2")

    ChrTalk(    #157
        0x101,
        "#1017F#6PI'm really glad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D95")

    label("loc_5CD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D04")

    ChrTalk(    #158
        0x106,
        "#556F#6PI'm glad you could.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D95")

    label("loc_5D04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D34")

    ChrTalk(    #159
        0x103,
        "#1534F#6PI'm really glad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D95")

    label("loc_5D34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D66")

    ChrTalk(    #160
        0x10C,
        "#111F#6PI'm glad you could.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D95")

    label("loc_5D66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D95")

    ChrTalk(    #161
        0x10D,
        "#275F#6PI'm glad you could.\x02",
    )

    CloseMessageWindow()

    label("loc_5D95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DEF")

    ChrTalk(    #162
        0x10B,
        (
            "#415F#6PAs long as you feel good about it,\x01",
            "that's all that matters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9A")

    label("loc_5DEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E3F")

    ChrTalk(    #163
        0x10F,
        "#1447F#6PIf you feel better now, that's all that matters.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F9A")

    label("loc_5E3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E96")

    ChrTalk(    #164
        0x104,
        (
            "#1545F#6PIf it turned out well for you,\x01",
            "that's all that matters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9A")

    label("loc_5E96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EEC")

    ChrTalk(    #165
        0x108,
        (
            "#573F#6PIf it turned out well for you,\x01",
            "that's all that matters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9A")

    label("loc_5EEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F42")

    ChrTalk(    #166
        0x10E,
        (
            "#179F#6PIf it turned out well for you,\x01",
            "that's all that matters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9A")

    label("loc_5F42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F9A")

    ChrTalk(    #167
        0x10A,
        (
            "#1314F#6PAs long as you feel good about it,\x01",
            "that's all that matters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F9A")


    def lambda_5FA0():
        OP_6D(-70, 15550, -2440, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5FA0)
    OP_8C(0x102, 180, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #168
        0x102,
        (
            "#1505F#11PWell, I've done what I needed to now.\x02\x03",

            "#1502FI'll leave everything to you now, Kevin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x109,
        (
            "#1065F#6PNo problem.\x02\x03",

            "#1060FNow that we've defeated the final guardian,\x01",
            "that path along the scenic route should now\x01",
            "be open.\x02\x03",

            "Let's head on over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x102,
        (
            "#1500F#11PThe one leading to the royal villa, right? \x01",
            "Got it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-340, 15550, -480, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(480, 0)
    SetChrPos(0x0, -340, 15550, -480, 180)
    SetChrPos(0x1, -340, 15550, -480, 180)
    SetChrPos(0x2, -340, 15550, -480, 180)
    SetChrPos(0x3, -340, 15550, -480, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61CE")
    OP_A2(0x2644)

    label("loc_61CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61DF")
    OP_A2(0x2645)

    label("loc_61DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61F0")
    OP_A2(0x2646)

    label("loc_61F0")

    OP_28(0x3B, 0x1, 0x2)
    OP_28(0x3B, 0x1, 0x4)
    OP_F7(0xC, 0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_54CB end

    def Function_8_6212(): pass

    label("Function_8_6212")

    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    OP_20(0x0)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x89, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    Sleep(1000)
    OP_AE(0x5DC)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 350, 15550, 2800, 180)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x109, -30, 15550, -4600, 0)
    SetChrPos(0x10F, -1350, 15550, -4550, 0)
    OP_51(0x10F, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3CA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFC, 0x80)
    SetChrFlags(0xFD, 0x80)
    OP_6D(-5140, 35650, -5290, 0)
    OP_67(0, 0, -10000, 0)
    OP_6B(4760, 0)
    OP_6C(45000, 0)
    OP_6E(443, 0)

    def lambda_6409():
        OP_6D(-5140, 19250, -5290, 7000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6409)

    def lambda_6421():
        OP_67(0, 5850, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6421)

    def lambda_6439():
        OP_6B(4760, 7000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6439)

    def lambda_6449():
        OP_6E(443, 7000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6449)
    LoadEffect(0x1, "map\\mp121_00.eff")
    LoadEffect(0x2, "battle\\btgun10.eff")
    LoadEffect(0x3, "map\\mp274_00.eff")
    LoadEffect(0x4, "map\\mp275_00.eff")
    LoadEffect(0x5, "map\\mp275_01.eff")
    LoadEffect(0x6, "map\\mp306_00.eff")
    LoadEffect(0x7, "map\\mp285_00.eff")
    FadeToBright(4000, 16777215)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(500)
    OP_6D(600, 15550, -3200, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(360, 0)
    OP_82(0x86, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x8A, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #171
        0x10F,
        "#1934F#6PH-How did we get here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x109,
        "#1063F#12PThis is where we fought the Schwarzritter...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #173
        (
            "\x07\x0C#40WThis is a place I made with his input for saying\x01",
            "farewell.\x02\x03",

            "Heh. I'm glad it ended up proving to be useful.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0xD3)
    Sleep(500)

    def lambda_6697():
        OP_6D(1300, 15550, 600, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6697)

    def lambda_66AF():
        OP_67(0, 4500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_66AF)

    def lambda_66C7():
        OP_6B(2820, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_66C7)

    def lambda_66D7():
        OP_6E(326, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_66D7)
    Sleep(2000)
    Fade(500)
    OP_22(0x99, 0x0, 0x50)
    PlayEffect(0x6, 0x0, 0x14, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x1, 0x14, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_6760():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6760)
    OP_22(0x146, 0x1, 0x3C)
    WaitChrThread(0x14, 0x1)
    Sleep(800)
    OP_82(0x1, 0x2)

    ChrTalk(    #174
        0x109,
        "#1079F#4POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x10F,
        "#1932F#6PR-Rufina...\x02",
    )

    CloseMessageWindow()

    def lambda_67B2():
        OP_6D(1200, 15550, 1800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_67B2)

    def lambda_67CA():
        OP_8E(0xFE, 0x0, 0x3CBE, 0xFFFFF8D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_67CA)
    Sleep(400)

    def lambda_67EA():
        OP_8E(0xFE, 0xFFFFFA56, 0x3CBE, 0xFFFFF7CC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_67EA)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #176
        0x109,
        (
            "#1840F#12PBack in your old knight getup, huh?\x02\x03",

            "You're finally free of the Stigma's influence,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x14,
        (
            "\x07\x0C#1475F#5P#30WI owe that to you two and your friends.\x02\x03",

            "#1471FYou deserve a lot of praise for overcoming so\x01",
            "much on your way here.\x02\x03",

            "You knew what you were up against. You could\x01",
            "have given up at any time...but you never did.\x02\x03",

            "#1479FHeehee. I'm so proud of you. ♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x10F,
        "#1952F#6PRufina...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x109,
        (
            "#1846F#12P...Haha. You really are just like I remember.\x02\x03",

            "#1840FSo...is the Stigma completely gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x14,
        (
            "\x07\x0C#1474F#5P#30WI'm afraid not... It still exists inside of me.\x02\x03",

            "#1477FYour victory earlier has allowed me to\x01",
            "suppress it in there for the time being...\x02\x03",

            "#1472F...but I won't be able to do so indefinitely. \x01",
            "It'll recover its power before long if it isn't\x01",
            "completely destroyed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x109,
        "#1067F#12POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x10F,
        "#1942F#6PB-But how do we...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x14,
        (
            "\x07\x0C#1475F#5P#30WI'm afraid someone is going to have to\x01",
            "destroy it.\x02\x03",

            "#1476FI want that someone to be you, Kevin.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #184
        0x109,
        "#1079F#12PHey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x10F,
        "#1934F#6PYou can't mean you'll have him kill you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x14,
        (
            "\x07\x0C#1476F#5P#30WThat's right. By killing me, the copy of your \x01",
            "Stigma will be destroyed as well.\x02\x03",

            "#1475FThat's the only way to get rid of it for good\x01",
            "and bring all of this to an end.\x02\x03",

            "#1471FDoing so should restore Celeste's power.\x02\x03",

            "After that, I believe she should be able to \x01",
            "return all of you safely to the real world.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x10F,
        "#1935F#6PB-But... But...!\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    Sleep(500)

    ChrTalk(    #188
        0x109,
        (
            "#1075F#12PLet me just make sure...\x02\x03",

            "#1840FThere's no other option, is there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x14,
        (
            "\x07\x0C#1475F#5P#30WNone. This is truly the only way.\x02\x03",

            "#1476FLast time you had to do this, you were barely\x01",
            "aware of what you were doing.\x02\x03",

            "This time, you won't have such a luxury.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x109,
        "#1067F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x10F,
        (
            "#1950F#6PHow could you ask that of him?!\x02\x03",

            "How could you make him do that again\x01",
            "knowing how much he suffered the first\x01",
            "time?!\x02\x03",

            "#1953FAnd if he does that, you'll...you'll...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x14,
        (
            "\x07\x0C#1477F#5P#30WI'm sorry, Ries.\x02\x03",

            "#1475FBut this is the reality, and I need to be\x01",
            "the one to tell him.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #193
        0x14,
        (
            "\x07\x0C#1472F#5P#30WI'll say it once more, Kevin.\x02\x03",

            "Kill me, and go back to the real world with\x01",
            "your friends.\x02\x03",

            "#1474FAs your sister, as a fellow knight, and as a\x01",
            "mother...\x02\x03",

            "#1471F...this is the last thing I'll ever ask you to do.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x10F,
        "#1950F#6P#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x109,
        (
            "#1845F#12P#40W...Haha...\x02\x03",

            "#1846FIt's amazing how someone can be so kind and\x01",
            "yet so cruel at the same time.\x02\x03",

            "#1844FBut that's how you've always been, I guess...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 8)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    def lambda_71DE():
        OP_6D(1100, 15550, 1900, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_71DE)

    def lambda_71F6():
        OP_67(0, 4490, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_71F6)

    def lambda_720E():
        OP_6C(38000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_720E)
    OP_99(0x109, 0x0, 0x7, 0x9C4)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(300)
    OP_8C(0x10F, 90, 600)
    Sleep(200)

    ChrTalk(    #196
        0x10F,
        "#1955F#6PNo, Kevin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x109,
        (
            "#1076F#11P#40WSorry, Ries...\x02\x03",

            "#1844FI'm gonna have to take your sister\x01",
            "from you not once, but twice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x10F,
        "#1950F#6P#40WI-If that's what you've got to do...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #199
        0x10F,
        "#1951F#6P#3S...then I'm doing it with you!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #200
        0x109,
        "#1847F#11PWhat...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x14,
        "\x07\x0C#1473F#5P#30W...Ries?\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x10F,
        (
            "#1950F#6P#40WI-I don't want to be left behind by you two\x01",
            "any more!\x02\x03",

            "I don't want to just stand aside and watch \x01",
            "anymore! I've had enough of just waiting!\x02\x03",

            "#1953FSo if this is something that has to be done...\x02\x03",

            "...then I'm going to do it with you! I'm going\x01",
            "to carry your sin with you this time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x109,
        "#1067F#11P...Thanks, Ries.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x14,
        (
            "\x07\x0C#1476F#5P#30WHeehee. It's hard to believe you're the same\x01",
            "little glutton from five years ago.\x02\x03",

            "#1475FYou've grown so much while I've been away.\x02\x03",

            "#1471FYou ended up studying under Ein, too, right?\x02\x03",

            "I apparently have plenty to thank her for.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)

    ChrTalk(    #205
        0x10F,
        "#1955F#6PR-Rufina, please...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x14,
        (
            "\x07\x0C#1475F#5P#30WWell, if you're sure that's what you want to do,\x01",
            "I have no objections.\x02\x03",

            "#1470FI'll leave the decision to you, Kevin.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #207
        0x109,
        (
            "#1847F#12PHow can you be okay with this?!\x02\x03",

            "#1069FI should be the one shouldering the burden!\x01",
            "Me, and me alone!\x02\x03",

            "Why should Ries--\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #208
        0x14,
        (
            "\x07\x0C#1478F#3S#5PYou're a grown man, Kevin!\x01",
            "Start acting like one, damn it!\x07\x00\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #209
        0x14,
        (
            "\x07\x0C#1475F#5P#30W...Is probably what Ein would say in this\x01",
            "situation were she with us.\x02\x03",

            "#1471FShe's not, though. So I want you to go\x01",
            "with your heart.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #210
        0x10F,
        "#1952F#6P#40WHa...haha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x109,
        (
            "#1844F#12P#40WHaha... You've always had a way with shaking\x01",
            "a guy up.\x02\x03",

            "#1843F...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_99(0x109, 0x7, 0x0, 0x7D0)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x109, 9)
    SetChrSubChip(0x109, 0)
    Sleep(300)
    OP_8C(0x109, 270, 400)
    Sleep(150)
    OP_8C(0x10F, 90, 400)
    Fade(500)
    OP_6D(640, 15550, -1090, 0)
    OP_67(0, 4450, -10000, 0)
    OP_6B(2280, 0)
    OP_6C(130000, 0)
    OP_6E(386, 0)
    SetChrPos(0x14, -650, 15550, 3840, 180)
    SetChrPos(0x109, -400, 15550, -1400, 270)
    SetChrPos(0x10F, -1650, 15550, -1520, 90)
    OP_51(0x10F, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x10F, 0x8)
    OP_0D()
    Sleep(300)
    OP_99(0x109, 0x0, 0x4, 0x4B0)
    Sleep(500)

    ChrTalk(    #212
        0x109,
        (
            "#1840F#5P#40WCome here, Ries.\x02\x03",

            "You can hold my bowgun with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x10F,
        "#1946F#12P#40W...Okay!\x02",
    )

    CloseMessageWindow()
    OP_99(0x109, 0x4, 0x0, 0x5DC)
    Sleep(300)

    def lambda_7AA1():
        OP_6D(1300, 15550, -300, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7AA1)
    OP_99(0x109, 0x10, 0x1C, 0x5DC)
    OP_22(0xD5, 0x0, 0x64)
    SetChrPos(0x10F, -1060, 15550, -1380, 90)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    ChrTalk(    #214
        0x14,
        (
            "\x07\x0C#1475F#6P#30WOh... I never considered that.\x02\x03",

            "Apparently, I was even further from my goal\x01",
            "than I thought I was...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x109,
        "#1079F#5PSorry...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x10F,
        "#1942F#11PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x14,
        (
            "\x07\x0C#1477F#6P#30WListen, Kevin...\x02\x03",

            "You said earlier that you wanted to try\x01",
            "and follow in my footsteps, right?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x109,
        (
            "#1840F#5PY-Yeah...\x02\x03",

            "It's not going to be easy, but it's what I want\x01",
            "to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x14,
        (
            "\x07\x0C#1475F#6P#30WWell, if that's genuinely what you've set your\x01",
            "mind on, I can't stop you...but I can't say that\x01",
            "I recommend it.\x02\x03",

            "#1477FThe path I walked was one fraught with pain,\x01",
            "doubts, and worries...\x02\x03",

            "I knew in my heart that there was no way it was\x01",
            "possible to make a world where everyone could\x01",
            "be happy.\x02\x03",

            "#1476FNevertheless, I dedicated my life to trying to get\x01",
            "as close as I could to that impossible goal--even\x01",
            "if it wasn't easy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x109,
        "#1075F#5P#40WBring it on, I say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x10F,
        (
            "#1937F#11P#40WI feel the same way.\x02\x03",

            "#1946FI want to follow in your footsteps, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x14,
        (
            "\x07\x0C#1475F#6P#30WHa... I've never seen two people look more\x01",
            "sure of themselves.\x02\x03",

            "#1477F...And if that's what you want...\x02\x03",

            "#1476FIf that's really, really what you want, don't content\x01",
            "yourselves with trying to go as far as I did.\x02\x03",

            "Go further than me; try and reach the places beyond\x01",
            "my grasp. Realize the future I never could.\x02\x03",

            "#1475FBecause I get the feeling the two of you may actually\x01",
            "be able to do it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x10F,
        "#1952F#11P#40WYou do...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x109,
        (
            "#1068F#5P#40WHaha... Damn. That's a doozy of a task you're\x01",
            "throwin' on us at the last minute.\x02\x03",

            "#1840FBut hey, I won't say no.\x02\x03",

            "Making it sound so hard just makes me want\x01",
            "to pull it off all the more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x10F,
        "#1937F#11P#40WI promise I will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x14,
        (
            "\x07\x0C#1471F#6P#30WJust don't try to walk too fast and end up\x01",
            "getting tired before the finish line.\x02\x03",

            "#1475F...Anyway, I think we've kept your friends\x01",
            "waiting for long enough.\x02\x03",

            "#1470FKevin, Ries...I think it's about time you pulled\x01",
            "that trigger.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x109,
        "#1844F#5P#40W...Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x10F,
        "#1935F#11P#40W...Right...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(900, 15550, 1300, 0)
    OP_67(0, 3950, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(43000, 0)
    OP_6E(347, 0)
    SetChrPos(0x14, 200, 15550, 2800, 180)
    SetChrPos(0x109, -510, 15550, -2340, 0)
    SetChrPos(0x10F, -1040, 15550, -2240, 0)
    SetChrSubChip(0x109, 40)
    OP_0D()
    Sleep(300)
    OP_99(0x109, 0x28, 0x2C, 0x5DC)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(300)
    SetChrFlags(0x14, 0x2)
    SetChrChipByIndex(0x14, 7)
    SetChrSubChip(0x14, 0)
    OP_99(0x14, 0x0, 0x4, 0x5DC)

    def lambda_831B():
        OP_6B(2500, 10000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_831B)
    Sleep(500)

    ChrTalk(    #229
        0x10F,
        "#1950F#6P#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x109,
        (
            "#1067F#11P#40WIt's okay, Ries. I'm right here with you.\x02\x03",

            "#1840FLet's just take this slowly... That's right.\x01",
            "Easy does it...\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #231
        0x14,
        (
            "\x07\x0C#1475F#5P#40WTeehee...\x02\x03",

            "May Aidios always watch over you both.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #232
        0x14,
        "\x07\x0C#1471F#5P#40WTake care of her for me, Kevin.\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x109,
        (
            "#1840F#12P#40W...I will. Always.\x02\x03",

            "#1075FThanks for everything... Really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x10F,
        "#1955F#6P#40WR-Rufina, I...I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x14,
        (
            "\x07\x0C#1476F#5P#40WAnd you take good care of Kevin, Ries.\x02\x03",

            "#1475FStay close, okay?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x10F,
        (
            "#1950F#6P#40WR-Rufina...\x02\x03",

            "#1952FWe will! Forever! So...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x109,
        "#1848F#12P#40WBye...Rufina...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_99(0x109, 0x2C, 0x2F, 0x5DC)
    Sleep(250)
    OP_44(0x109, 0x2)

    def lambda_85E5():
        OP_6D(1200, 15550, 3300, 500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_85E5)
    PlayEffect(0x2, 0x3, 0x109, 0, 1150, 1300, 0, 0, 0, 1000, 1000, 1000, 0x14, 0, 1000, 0, 0)

    def lambda_8632():
        OP_99(0xFE, 0x31, 0x37, 0x7D0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8632)
    OP_22(0x2C5, 0x0, 0x64)
    Sleep(200)
    OP_22(0x22B, 0x0, 0x50)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    def lambda_8661():
        OP_99(0xFE, 0x6, 0xC, 0x5DC)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_8661)
    OP_22(0x20C, 0x0, 0x46)
    WaitChrThread(0x14, 0x0)
    Sleep(500)
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    PlayEffect(0x3, 0x2, 0x14, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_44(0x109, 0x3)
    Fade(1000)
    OP_6D(180, 15550, 4019, 0)
    OP_67(0, 4150, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(0, 0)
    OP_6E(372, 0)
    SetChrPos(0x14, 0, 15550, 2800, 180)
    SetChrChipByIndex(0x14, 11)
    SetChrSubChip(0x14, 0)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x20)
    SetChrPos(0x109, 440, 15550, -3340, 0)
    SetChrPos(0x10F, 30, 15550, -3340, 0)
    SetChrChipByIndex(0x109, 11)
    SetChrSubChip(0x109, 39)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    PlayEffect(0x3, 0x2, 0x14, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_0D()

    def lambda_87EC():

        label("loc_87EC")

        OP_99(0xFE, 0x5, 0xC, 0x3E8)
        OP_48()
        Jump("loc_87EC")

    QueueWorkItem2(0x14, 0, lambda_87EC)

    def lambda_87FF():
        OP_8F(0xFE, 0x0, 0x4718, 0xFA0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_87FF)
    Sleep(500)

    def lambda_881F():
        OP_6D(0, 17650, 9770, 4500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_881F)

    def lambda_8837():
        OP_67(0, 1700, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8837)

    def lambda_884F():
        OP_6B(2700, 4500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_884F)

    def lambda_885F():
        OP_6E(389, 4500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_885F)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x14, 0x1)
    Sleep(500)

    def lambda_887E():
        OP_99(0xFE, 0xD, 0x15, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_887E)
    WaitChrThread(0x14, 0x0)

    def lambda_8893():

        label("loc_8893")

        OP_99(0xFE, 0x16, 0x1D, 0x3E8)
        OP_48()
        Jump("loc_8893")

    QueueWorkItem2(0x14, 0, lambda_8893)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_88B9():
        OP_6D(0, 18000, 9770, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_88B9)

    def lambda_88D1():
        OP_6B(2400, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_88D1)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x14, 0, 500, -2500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 500)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    WaitChrThread(0x109, 0x2)
    LoadEffect(0x4, "map\\mp275_00.eff")
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x89, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(1000)
    PlayEffect(0x4, 0x4, 0x14, 0, 500, 0, 0, -30, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x5, 0x14, 0, 0, 0, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)

    def lambda_8AC2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8AC2)
    OP_22(0x146, 0x1, 0x3C)
    OP_22(0x1B0, 0x0, 0x64)

    def lambda_8ADE():
        OP_6D(0, 17600, 9770, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8ADE)

    def lambda_8AF6():
        OP_67(0, 1050, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8AF6)

    def lambda_8B0E():
        OP_6B(3300, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8B0E)

    def lambda_8B1E():
        OP_6E(462, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8B1E)
    WaitChrThread(0x14, 0x1)
    OP_23(0x146)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x80)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    WaitChrThread(0x109, 0x3)
    Sleep(500)

    ChrTalk(    #238 op#A
        0x10F,
        "#1949F#5P#40W#15A...Ah....\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_6D(230, 15550, -2790, 0)
    OP_67(0, 4610, -10000, 0)
    OP_6B(1950, 0)
    OP_6C(180000, 0)
    OP_6E(456, 0)

    def lambda_8BD3():
        OP_6B(1900, 50000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8BD3)
    SetChrPos(0x109, 430, 15550, -1220, 0)
    SetChrPos(0x10F, 0, 15550, -1190, 0)
    SetChrChipByIndex(0x109, 12)
    SetChrSubChip(0x109, 3)
    OP_22(0xD5, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_99(0x109, 0x8, 0xD, 0x4B0)
    OP_43(0x10F, 0x0, 0x0, 0x9)
    Sleep(500)

    ChrTalk(    #239
        0x10F,
        "#1956F#11P#60W...*sniffle*...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_44(0x10F, 0x0)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #240
        0x10F,
        "#1957F#11P#60W...*sob*...\x02",
    )

    CloseMessageWindow()
    OP_99(0x109, 0x10, 0x16, 0x4B0)
    Sleep(500)

    ChrTalk(    #241
        0x109,
        "#1067F#5P#40WIt's okay, Ries...\x02",
    )

    CloseMessageWindow()
    OP_99(0x109, 0x18, 0x1A, 0x3E8)
    OP_22(0x8F, 0x0, 0x64)
    OP_99(0x109, 0x1B, 0x1E, 0x3E8)
    OP_99(0x109, 0x30, 0x34, 0x3E8)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #242
        0x109,
        (
            "#1848F#5P#40WI'm sure we can do it...\x02\x03",

            "I'm sure we can realize her dream and reach\x01",
            "the place she was always trying to get to...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x109, 0x20, 0x22, 0x3E8)
    Sleep(500)

    ChrTalk(    #243
        0x109,
        (
            "#1075F#5P#40WAnd I'm guessing that when we do, we'll find\x01",
            "her there waiting for us...\x02\x03",

            "So this isn't the end...\x02\x03",

            "#1840FWe'll see her again... We will...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #244
        0x10F,
        "#1956F#11P#60W*sob*\x02",
    )

    CloseMessageWindow()

    def lambda_8ECC():
        OP_6B(4000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8ECC)

    def lambda_8EDC():
        OP_6E(485, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8EDC)

    def lambda_8EEC():
        OP_67(0, 6500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8EEC)
    Sleep(1000)

    ChrTalk(    #245 op#A op#5
        0x10F,
        "#1957F#4S#25A#11PWaaaaaah!\x05\x02",
    )

    OP_7C(0x32, 0x32, 0xBB8, 0x1F4)
    FadeToDark(3000, 16777215, -1)
    CloseMessageWindow()
    OP_0D()
    OP_C4(0x0, 0x10)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    Sleep(1000)
    FadeToBright(3000, 16777215)
    OP_0D()
    OP_20(0x1388)
    OP_21()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_DC(0x0, 0x0)
    OP_A2(0x2508)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_6212 end

    def Function_9_8F86(): pass

    label("Function_9_8F86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FD2")
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_9_8F86")

    label("loc_8FD2")

    Return()

    # Function_9_8F86 end

    SaveToFile()

Try(main)
