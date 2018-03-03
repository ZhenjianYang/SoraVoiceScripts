from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5504   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5504.x',
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
        'Scherazard',                           # 9
        'The-le-force',                         # 10
        'The-le-force',                         # 11
        'The-le-force',                         # 12
        'The-le-force',                         # 13
        'Sealing Stone 10',                     # 14
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
        'ED6_DT07/CH00120 ._CH',             # 00
        'ED6_DT07/CH00121 ._CH',             # 01
        'ED6_DT29/CH14740 ._CH',             # 02
        'ED6_DT29/CH14741 ._CH',             # 03
        'ED6_DT29/CH14540 ._CH',             # 04
        'ED6_DT29/CH14541 ._CH',             # 05
        'ED6_DT29/CH15110 ._CH',             # 06
        'ED6_DT29/CH15111 ._CH',             # 07
        'ED6_DT29/CH14530 ._CH',             # 08
        'ED6_DT29/CH14531 ._CH',             # 09
        'ED6_DT26/CH20621 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH00120P._CP',             # 00
        'ED6_DT07/CH00121P._CP',             # 01
        'ED6_DT29/CH14740P._CP',             # 02
        'ED6_DT29/CH14741P._CP',             # 03
        'ED6_DT29/CH14540P._CP',             # 04
        'ED6_DT29/CH14541P._CP',             # 05
        'ED6_DT29/CH15110P._CP',             # 06
        'ED6_DT29/CH15111P._CP',             # 07
        'ED6_DT29/CH14530P._CP',             # 08
        'ED6_DT29/CH14531P._CP',             # 09
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


    DeclMonster(
        X                   = 22330,
        Z                   = 0,
        Y                   = 17900,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x197,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -22340,
        Y                   = -1000,
        Z                   = -10060,
        Range               = 4000,
        Unknown_10          = 0x1770,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 2,
    )


    DeclActor(
        TriggerX            = -4390,
        TriggerZ            = 0,
        TriggerY            = 33260,
        TriggerRange        = 1000,
        ActorX              = -4390,
        ActorZ              = 2000,
        ActorY              = 33260,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22270,
        TriggerZ            = 0,
        TriggerY            = 34210,
        TriggerRange        = 1000,
        ActorX              = 22270,
        ActorZ              = 1000,
        ActorY              = 34210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_246",          # 00, 0
        "Function_1_247",          # 01, 1
        "Function_2_284",          # 02, 2
        "Function_3_295",          # 03, 3
        "Function_4_C16",          # 04, 4
        "Function_5_1269",         # 05, 5
        "Function_6_1299",         # 06, 6
        "Function_7_12C4",         # 07, 7
        "Function_8_12F4",         # 08, 8
        "Function_9_1324",         # 09, 9
        "Function_10_1376",        # 0A, 10
        "Function_11_13DB",        # 0B, 11
        "Function_12_1440",        # 0C, 12
        "Function_13_14A5",        # 0D, 13
        "Function_14_150A",        # 0E, 14
        "Function_15_178C",        # 0F, 15
    )


    def Function_0_246(): pass

    label("Function_0_246")

    Return()

    # Function_0_246 end

    def Function_1_247(): pass

    label("Function_1_247")

    OP_16(0x2, 0xFA0, 0xFFFDF878, 0xFFFE6DA8, 0x2300A1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A")
    OP_82(0x91, 0x0)
    OP_82(0x92, 0x0)
    OP_82(0x94, 0x0)

    label("loc_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x537, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C")
    OP_6F(0x0, 0)
    Jump("loc_283")

    label("loc_27C")

    OP_6F(0x0, 60)

    label("loc_283")

    Return()

    # Function_1_247 end

    def Function_2_284(): pass

    label("Function_2_284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 1)), scpexpr(EXPR_END)), "loc_28C")
    Return()

    label("loc_28C")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_284 end

    def Function_3_295(): pass

    label("Function_3_295")

    EventBegin(0x0)
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
    OP_20(0x7D0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A7")

    label("loc_340")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_368")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A7")

    label("loc_368")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_390")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A7")

    label("loc_390")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CF")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_436")

    label("loc_3CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F7")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_436")

    label("loc_3F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_436")

    label("loc_41F")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_436")

    Sleep(1000)

    def lambda_441():
        OP_6D(-28950, 0, -18620, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_441)

    def lambda_459():
        OP_67(0, 5880, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_459)

    def lambda_471():
        OP_6B(3330, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_471)

    def lambda_481():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_481)

    def lambda_491():
        OP_6E(250, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_491)

    def lambda_4A1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4A1)

    def lambda_4AF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_4AF)

    def lambda_4BD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_4BD)

    def lambda_4CB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_4CB)
    WaitChrThread(0xEE, 0x2)
    SetChrPos(0xEE, -23720, 0, -7770, 180)
    SetChrPos(0xEF, -22280, 0, -7300, 180)
    SetChrPos(0xF0, -23740, 0, -5960, 180)
    SetChrPos(0xF1, -22500, 0, -5310, 180)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -28030, 100, -18770, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, -25670, 0, -21170, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFF, -28610, 0, -21010, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0xFF, -31000, 0, -18930, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x5, 0xFF, -30970, 0, -16520, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_662():
        OP_6B(2970, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_662)
    OP_22(0x85, 0x1, 0x64)

    def lambda_677():

        label("loc_677")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_677")

    QueueWorkItem2(0x109, 0, lambda_677)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -28030, -3000, -18770, 45)
    SetChrSubChip(0x10, 0)
    OP_43(0x10, 0x0, 0x0, 0x9)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -25670, -3000, -21170, 45)
    OP_43(0x11, 0x0, 0x0, 0xA)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -28610, -3000, -21010, 45)
    OP_43(0x12, 0x0, 0x0, 0xB)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -31000, -3000, -18930, 45)
    OP_43(0x13, 0x0, 0x0, 0xC)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -30970, -3000, -16520, 45)
    OP_43(0x14, 0x0, 0x0, 0xD)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    OP_1D(0xC4)
    OP_44(0x109, 0x0)
    Fade(1000)
    LoadEffect(0x1, "map\\mp250_00.eff")
    Sleep(500)
    OP_23(0x85)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    ClearMapFlags(0x10)
    OP_6D(-26280, 0, -16090, 0)
    OP_67(0, 6630, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(269000, 0)
    OP_6E(278, 0)
    SetChrPos(0xEE, -20800, 0, -7830, 180)
    SetChrPos(0xEF, -19170, 60, -8210, 180)
    SetChrPos(0xF0, -20690, 0, -5830, 180)
    SetChrPos(0xF1, -19130, 430, -7000, 180)
    OP_43(0x109, 0x0, 0x0, 0x5)
    OP_43(0x102, 0x0, 0x0, 0x6)
    OP_43(0xF0, 0x0, 0x0, 0x7)
    OP_43(0xF1, 0x0, 0x0, 0x8)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)

    ChrTalk(    #0
        0x102,
        "#1506F#6PSchera!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        "#529F#5P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_876")

    ChrTalk(    #2
        0x104,
        "#1543F#12PDarling Schera!\x02",
    )

    CloseMessageWindow()

    label("loc_876")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89D")

    ChrTalk(    #3
        0x10A,
        "#1317F#4PSchera!\x02",
    )

    CloseMessageWindow()
    Jump("loc_919")

    label("loc_89D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C7")

    ChrTalk(    #4
        0x108,
        "#072F#4PScherazard!\x02",
    )

    CloseMessageWindow()
    Jump("loc_919")

    label("loc_8C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F1")

    ChrTalk(    #5
        0x107,
        "#065F#4PSch-Schera!\x02",
    )

    CloseMessageWindow()
    Jump("loc_919")

    label("loc_8F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_919")

    ChrTalk(    #6
        0x105,
        "#1163F#4PScherazard!\x02",
    )

    CloseMessageWindow()

    label("loc_919")


    ChrTalk(    #7
        0x109,
        (
            "#1065F#12PSo she's our lady this time, huh?\x02\x03",

            "#1063FMakes sense that we'd find nothin'\x01",
            "but bracers on one of their training\x01",
            "grounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1502F#6PWe'll have to defeat her so we can\x01",
            "get her sealing stone.\x02\x03",

            "Here's hoping we can have the real\x01",
            "thing by our side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        "#1069F#12PExactly!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_A4D():
        OP_6D(-27040, 0, -15960, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A4D)

    def lambda_A65():
        OP_67(0, 6630, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A65)

    def lambda_A7D():
        OP_6B(2640, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_A7D)

    def lambda_A8D():
        OP_6E(264, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A8D)

    def lambda_A9D():
        OP_8F(0xFE, 0xFFFF9B56, 0x0, 0xFFFFC3F6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A9D)
    SetChrChipByIndex(0x10, 1)

    def lambda_ABD():
        OP_8F(0xFE, 0xFFFF9944, 0x0, 0xFFFFBF00, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_ABD)
    Sleep(10)
    SetChrChipByIndex(0x14, 9)

    def lambda_AE2():

        label("loc_AE2")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_AE2")

    QueueWorkItem2(0x14, 3, lambda_AE2)

    def lambda_AF5():
        OP_8F(0xFE, 0xFFFF9E76, 0x0, 0xFFFFC748, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_AF5)

    def lambda_B10():
        OP_8F(0xFE, 0xFFFF9F66, 0x0, 0xFFFFC07C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B10)
    Sleep(10)
    SetChrChipByIndex(0x12, 9)

    def lambda_B35():

        label("loc_B35")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_B35")

    QueueWorkItem2(0x12, 3, lambda_B35)

    def lambda_B48():
        OP_8F(0xFE, 0xFFFFA376, 0x0, 0xFFFFC310, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_B48)

    def lambda_B63():
        OP_8F(0xFE, 0xFFFF9B56, 0x0, 0xFFFFC3F6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_B63)
    Sleep(10)
    SetChrChipByIndex(0x13, 9)

    def lambda_B88():

        label("loc_B88")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_B88")

    QueueWorkItem2(0x13, 3, lambda_B88)

    def lambda_B9B():
        OP_8F(0xFE, 0xFFFFA042, 0x0, 0xFFFFC586, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_B9B)

    def lambda_BB6():
        OP_8F(0xFE, 0xFFFF9F66, 0x0, 0xFFFFC07C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_BB6)
    Sleep(10)
    SetChrChipByIndex(0x11, 9)

    def lambda_BDB():

        label("loc_BDB")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_BDB")

    QueueWorkItem2(0x11, 3, lambda_BDB)

    def lambda_BEE():
        OP_8F(0xFE, 0xFFFFA506, 0x0, 0xFFFFC11C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BEE)
    WaitChrThread(0x109, 0x1)
    Battle(0x1A4, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_295 end

    def Function_4_C16(): pass

    label("Function_4_C16")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
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
    SetChrPos(0xEE, -24440, 0, -16610, 225)
    SetChrPos(0xEF, -23630, 0, -17790, 225)
    SetChrPos(0xF0, -22810, 0, -15600, 225)
    SetChrPos(0xF1, -21900, 0, -17040, 225)
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
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_6D(-27690, 0, -18130, 0)
    OP_67(0, 6080, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(269000, 0)
    OP_6E(286, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x15, 0x80)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, -27200, 1200, -19420, 0)
    PlayEffect(0x7, 0x7, 0x15, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x15, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
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

    def lambda_E6F():
        OP_6D(-27740, 0, -18560, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E6F)

    def lambda_E87():
        OP_67(0, 4970, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E87)

    def lambda_E9F():
        OP_6B(3100, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E9F)

    def lambda_EAF():
        OP_6E(286, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_EAF)
    OP_8F(0x109, 0xFFFF9930, 0x0, 0xFFFFB618, 0x7D0, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x15, 0xFFFF975A, 0x4E2, 0xFFFFB51E, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x15, 0x80)
    OP_0D()
    Sleep(150)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05Found \x1F\x5B\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x35B, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #11
        0x109,
        "#1078F#5PNice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1513F#6PNow we should be able to set Schera free, too.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1021")

    ChrTalk(    #13
        0x10B,
        (
            "#413F#12PUgh... Her and her whip bring back nothing but\x01",
            "bad memories...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1021")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A6")

    ChrTalk(    #14
        0x104,
        (
            "#1541F#12PHeh. I can hardly wait to feel her in my arms \x01",
            "again at long last.\x02\x03",

            "#1540FTo the garden, my friends!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1118")

    label("loc_10A6")

    OP_8C(0x109, 45, 400)
    Sleep(300)

    ChrTalk(    #15
        0x109,
        (
            "#1075F#5PWell, let's get this back to the garden.\x02\x03",

            "#1060FIt'll be great to have her on the team.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1118")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1194")

    ChrTalk(    #16
        0x10A,
        (
            "#811F#12PHeehee. I can hardly wait to see her again.\x02\x03",

            "#1310FI'm sure she's going to be a big help to us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1194")

    OP_A2(0x2909)
    OP_28(0x33, 0x1, 0x40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-26440, 0, -18550, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -26440, 0, -18550, 45)
    SetChrPos(0x1, -26440, 0, -18550, 45)
    SetChrPos(0x2, -26440, 0, -18550, 45)
    SetChrPos(0x3, -26440, 0, -18550, 45)
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

    # Function_4_C16 end

    def Function_5_1269(): pass

    label("Function_5_1269")

    Sleep(150)
    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFFA1BE, 0x0, 0xFFFFCA36, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_5_1269 end

    def Function_6_1299(): pass

    label("Function_6_1299")

    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFFA6D2, 0x0, 0xFFFFC626, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_1299 end

    def Function_7_12C4(): pass

    label("Function_7_12C4")

    Sleep(200)
    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFFA7A4, 0x0, 0xFFFFCEBE, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_12C4 end

    def Function_8_12F4(): pass

    label("Function_8_12F4")

    Sleep(100)
    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFFAC2C, 0x0, 0xFFFFCAD6, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_8_12F4 end

    def Function_9_1324(): pass

    label("Function_9_1324")

    PlayEffect(0x1, 0xFF, 0xFF, -28030, 100, -18770, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_1324 end

    def Function_10_1376(): pass

    label("Function_10_1376")

    PlayEffect(0x1, 0xFF, 0xFF, -25670, 0, -21170, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_13B1():

        label("loc_13B1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13B1")

    QueueWorkItem2(0xFE, 3, lambda_13B1)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_1376 end

    def Function_11_13DB(): pass

    label("Function_11_13DB")

    PlayEffect(0x1, 0xFF, 0xFF, -28610, 0, -21010, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_1416():

        label("loc_1416")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1416")

    QueueWorkItem2(0xFE, 3, lambda_1416)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x3, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_11_13DB end

    def Function_12_1440(): pass

    label("Function_12_1440")

    PlayEffect(0x1, 0xFF, 0xFF, -31000, 0, -18930, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_147B():

        label("loc_147B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_147B")

    QueueWorkItem2(0xFE, 3, lambda_147B)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_12_1440 end

    def Function_13_14A5(): pass

    label("Function_13_14A5")

    PlayEffect(0x1, 0xFF, 0xFF, -30970, 0, -16520, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_14E0():

        label("loc_14E0")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_14E0")

    QueueWorkItem2(0xFE, 3, lambda_14E0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_14A5 end

    def Function_14_150A(): pass

    label("Function_14_150A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D9")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x91, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x92, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x94, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(3328)
    Sleep(500)
    Jump("loc_15DC")

    label("loc_15D9")

    TalkBegin(0xFF)

    label("loc_15DC")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #17
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1618")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_175B")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1674"),
        (1, "loc_16EF"),
        (2, "loc_171D"),
        (SWITCH_DEFAULT, "loc_174B"),
    )


    label("loc_1674")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE7)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1758")

    label("loc_16EF")

    OP_A9(0x20)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_1758")

    label("loc_171D")

    OP_A9(0x7)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_1758")

    label("loc_174B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1758")

    label("loc_1758")

    Jump("loc_1618")

    label("loc_175B")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1788")
    OP_A2(0x2590)
    EventEnd(0x1)
    Jump("loc_178B")

    label("loc_1788")

    TalkEnd(0xFF)

    label("loc_178B")

    Return()

    # Function_14_150A end

    def Function_15_178C(): pass

    label("Function_15_178C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x537, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1865")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x41B, 1)"), scpexpr(EXPR_END)), "loc_17FA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05Found \x1F\x1B\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29B8)
    Jump("loc_1862")

    label("loc_17FA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05Found \x1F\x1B\x04\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x1B\x04\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_1862")

    Jump("loc_18B1")

    label("loc_1865")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05I hope my contents were speedrun-worthy.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x78, 0x0)

    label("loc_18B1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_178C end

    SaveToFile()

Try(main)
