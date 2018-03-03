from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U5100   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U5100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'Wererat',                              # 9
        'Wererat',                              # 10
        'Wererat',                              # 11
        'Wererat',                              # 12
        'Werewolf',                             # 13
        'Werewolf',                             # 14
        'Werewolf',                             # 15
        'Female Ghost',                         # 16
        'Le Locle Map',                         # 17
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
        'ED6_DT29/CH14740 ._CH',             # 02
        'ED6_DT29/CH14741 ._CH',             # 03
        'ED6_DT29/CH14742 ._CH',             # 04
        'ED6_DT26/CH20622 ._CH',             # 05
        'ED6_DT07/CH02890 ._CH',             # 06
        'ED6_DT26/CH20653 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH14540P._CP',             # 00
        'ED6_DT29/CH14541P._CP',             # 01
        'ED6_DT29/CH14740P._CP',             # 02
        'ED6_DT29/CH14741P._CP',             # 03
        'ED6_DT29/CH14742P._CP',             # 04
        'ED6_DT26/CH20622P._CP',             # 05
        'ED6_DT07/CH02890P._CP',             # 06
        'ED6_DT26/CH20653P._CP',             # 07
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x184,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -3550,
        TriggerZ            = 0,
        TriggerY            = -3000,
        TriggerRange        = 800,
        ActorX              = -4250,
        ActorZ              = 1000,
        ActorY              = -3000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22E",          # 00, 0
        "Function_1_261",          # 01, 1
        "Function_2_281",          # 02, 2
        "Function_3_28A",          # 03, 3
        "Function_4_27BD",         # 04, 4
        "Function_5_27EF",         # 05, 5
        "Function_6_281C",         # 06, 6
        "Function_7_2849",         # 07, 7
        "Function_8_287B",         # 08, 8
        "Function_9_28E9",         # 09, 9
        "Function_10_2952",        # 0A, 10
        "Function_11_29C0",        # 0B, 11
        "Function_12_2A0A",        # 0C, 12
        "Function_13_2A54",        # 0D, 13
        "Function_14_2A9E",        # 0E, 14
        "Function_15_2AE8",        # 0F, 15
        "Function_16_2B1F",        # 10, 16
        "Function_17_2B56",        # 11, 17
        "Function_18_2B8D",        # 12, 18
        "Function_19_2BA9",        # 13, 19
        "Function_20_2BCA",        # 14, 20
        "Function_21_2BE6",        # 15, 21
        "Function_22_2C07",        # 16, 22
        "Function_23_43EA",        # 17, 23
        "Function_24_4446",        # 18, 24
        "Function_25_44A7",        # 19, 25
        "Function_26_454E",        # 1A, 26
        "Function_27_4681",        # 1B, 27
        "Function_28_4BCB",        # 1C, 28
        "Function_29_4CBA",        # 1D, 29
        "Function_30_4D76",        # 1E, 30
        "Function_31_4E8C",        # 1F, 31
        "Function_32_4EDA",        # 20, 32
    )


    def Function_0_22E(): pass

    label("Function_0_22E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_246"),
        (SWITCH_DEFAULT, "loc_24D"),
    )


    label("loc_246")

    Event(0, 28)
    Jump("loc_24D")

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_260")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_260")

    Return()

    # Function_0_22E end

    def Function_1_261(): pass

    label("Function_1_261")

    OP_16(0x2, 0xFA0, 0xFFFE13D0, 0xFFFDE4F0, 0x23006F)
    OP_1B(0x4, 0x0, 0x1D)
    OP_1B(0x0, 0x0, 0x1B)
    OP_82(0x81, 0x0)
    Return()

    # Function_1_261 end

    def Function_2_281(): pass

    label("Function_2_281")

    Call(0, 3)
    Call(0, 22)
    Return()

    # Function_2_281 end

    def Function_3_28A(): pass

    label("Function_3_28A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp204_02.eff")
    OP_E0(265, 0x48, 0x2)
    OP_E0(258, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x2)
    OP_E0(241, 0x4B, 0x2)
    SetChrPos(0x109, 7450, 0, 5430, 180)
    SetChrPos(0x102, 6540, 0, 6210, 180)
    SetChrPos(0xF0, 8230, 0, 6140, 180)
    SetChrPos(0xF1, 7310, 0, 7160, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(20430, 2600, -5010, 0)
    OP_67(0, 9920, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(237, 0)

    def lambda_370():
        OP_6D(9200, 2600, 4600, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_370)

    def lambda_388():
        OP_67(0, 9490, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_388)

    def lambda_3A0():
        OP_6B(3800, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3A0)

    def lambda_3B0():
        OP_6E(237, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3B0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)

    def lambda_3CF():
        OP_6D(9200, 2600, 4600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3CF)

    def lambda_3E7():
        OP_67(0, 7580, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3E7)

    def lambda_3FF():
        OP_6B(2440, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3FF)

    def lambda_40F():
        OP_6E(285, 3000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_40F)
    Sleep(1000)
    PlayEffect(0x0, 0xFF, 0xFF, 7240, 0, 6380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(300)

    def lambda_468():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_468)

    def lambda_47A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_47A)

    def lambda_48C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_48C)

    def lambda_49E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_49E)
    WaitChrThread(0x109, 0x0)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_514")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_57B")

    label("loc_514")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_57B")

    label("loc_53C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_564")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_57B")

    label("loc_564")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_57B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A8")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_60F")

    label("loc_5A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_60F")

    label("loc_5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F8")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_60F")

    label("loc_5F8")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_60F")

    Sleep(1000)

    ChrTalk(    #0
        0x102,
        "#1504F#5PWhere are we now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        (
            "#1067F#6PHmm... Nowhere I've ever been before,\x01",
            "judging from where I'm standing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CA")

    label("loc_6B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CA")

    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x108, 0, 400)
    Sleep(300)

    ChrTalk(    #2
        0x108,
        "#073F#6POh, my...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B8")

    label("loc_70C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_735")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_74D")

    label("loc_735")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_74D")

    OP_62(0x10D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10D, 0, 400)
    Sleep(300)

    ChrTalk(    #3
        0x10D,
        "#273F#6POh, my...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B8")

    label("loc_78F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_812")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D0")

    label("loc_7B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7D0")

    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10E, 0, 400)
    Sleep(300)

    ChrTalk(    #4
        0x10E,
        "#173F#6POh, my...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B8")

    label("loc_812")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_853")

    label("loc_83B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_853")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_853")

    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x105, 0, 400)
    Sleep(300)

    ChrTalk(    #5
        0x105,
        "#1164F#6PLook over there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B8")

    label("loc_89D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8DE")

    label("loc_8C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8DE")

    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10B, 0, 400)
    Sleep(300)

    ChrTalk(    #6
        0x10B,
        "#213F#6PWow! Look over there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B8")

    label("loc_92C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_955")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96D")

    label("loc_955")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96D")

    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 0, 400)
    Sleep(300)

    ChrTalk(    #7
        0x107,
        "#560F#6PWow! Look over there!\x02",
    )

    CloseMessageWindow()

    label("loc_9B8")

    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A16")
    OP_62(0xF1, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_A6E")

    label("loc_A16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A39")
    OP_62(0xF1, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_A6E")

    label("loc_A39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5C")
    OP_62(0xF1, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_A6E")

    label("loc_A5C")

    OP_62(0xF1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_A6E")

    Jump("loc_AF9")

    label("loc_A71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA1")
    OP_62(0xF0, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_AF9")

    label("loc_AA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC4")
    OP_62(0xF0, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_AF9")

    label("loc_AC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE7")
    OP_62(0xF0, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_AF9")

    label("loc_AE7")

    OP_62(0xF0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_AF9")

    Sleep(1000)

    def lambda_B04():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B04)
    Sleep(100)

    def lambda_B17():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B17)
    Sleep(100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3B")
    OP_8C(0xF1, 0, 400)
    Jump("loc_B4F")

    label("loc_B3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4F")
    OP_8C(0xF0, 0, 400)

    label("loc_B4F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0xDD)
    Fade(1000)
    OP_6D(3630, 0, 46640, 0)
    OP_67(0, 11020, -10000, 0)
    OP_6B(4030, 0)
    OP_6C(315000, 0)
    OP_6E(312, 0)
    OP_0D()
    Sleep(500)

    def lambda_BA9():
        OP_6D(9200, 2600, 5600, 7000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BA9)

    def lambda_BC1():
        OP_67(0, 9180, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BC1)

    def lambda_BD9():
        OP_6B(4930, 7000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BD9)

    def lambda_BE9():
        OP_6E(332, 7000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_BE9)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(7130, 0, 7000, 0)
    OP_67(0, 8180, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(250, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8D")

    ChrTalk(    #8
        0x104,
        "#1541F#6PHeh. Now that's what I call a fine view.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DAD")

    label("loc_C8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC3")

    ChrTalk(    #9
        0x107,
        "#560F#6PWhoooa. It's so pretty!\x02",
    )

    CloseMessageWindow()
    Jump("loc_DAD")

    label("loc_CC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D04")

    ChrTalk(    #10
        0x10B,
        "#210F#6PHuh. That's a heck of a nice view.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DAD")

    label("loc_D04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3C")

    ChrTalk(    #11
        0x105,
        "#1382F#6PWhat a beautiful view...\x02",
    )

    CloseMessageWindow()
    Jump("loc_DAD")

    label("loc_D3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D72")

    ChrTalk(    #12
        0x10E,
        "#171F#6PWhat a stunning view...\x02",
    )

    CloseMessageWindow()
    Jump("loc_DAD")

    label("loc_D72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DAD")

    ChrTalk(    #13
        0x10D,
        "#277F#6PThat's quite the stunning view.\x02",
    )

    CloseMessageWindow()

    label("loc_DAD")


    ChrTalk(    #14
        0x109,
        (
            "#1078F#6PWow... Well, this is a lot prettier than the last\x01",
            "plane, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        (
            "#1500F#5PThis must be another real place that's been\x01",
            "recreated here in Phantasma, much like the\x01",
            "capital was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1065F#6PMost likely, yeah.\x02\x03",

            "#1067FJust where is it, though? Somewhere in Liberl?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F7C")

    ChrTalk(    #17
        0x102,
        "#1505F#5PI doubt it. It's not familiar to me at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        (
            "#1163F#6PMy best guess would be somewhere along\x01",
            "the Krone mountains, but the air suggests\x01",
            "otherwise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CD")

    label("loc_F7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1030")

    ChrTalk(    #19
        0x102,
        "#1505F#5PI doubt it. It's not familiar to me at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10E,
        (
            "#178F#6PMy best guess would be somewhere along\x01",
            "the Krone mountains, but the air suggests\x01",
            "otherwise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CD")

    label("loc_1030")


    ChrTalk(    #21
        0x102,
        (
            "#1505F#5PI doubt it. It's not familiar to me at all.\x02\x03",

            "#1503FMy best guess would be somewhere along\x01",
            "the Krone mountains, but the air suggests\x01",
            "otherwise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10CD")

    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 270, 400)
    Sleep(300)

    ChrTalk(    #22
        0x102,
        "#1504F#6POh...\x02",
    )

    CloseMessageWindow()

    def lambda_110F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_110F)
    Sleep(100)

    def lambda_1122():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_1122)
    Sleep(100)
    OP_8C(0xF0, 270, 400)

    ChrTalk(    #23
        0x109,
        "#1079F#6P...Hmm?\x02",
    )

    CloseMessageWindow()

    def lambda_1152():
        OP_6D(-860, 9050, 5560, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1152)

    def lambda_116A():
        OP_67(0, 5810, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_116A)

    def lambda_1182():
        OP_6B(3280, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1182)

    def lambda_1192():
        OP_6C(291000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1192)

    def lambda_11A2():
        OP_6E(253, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11A2)
    Sleep(500)

    def lambda_11B7():
        OP_8E(0xFE, 0xFFFFFD6C, 0x0, 0x1676, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_11B7)
    Sleep(200)

    def lambda_11D7():
        OP_8E(0xFE, 0xF0, 0x0, 0x113A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_11D7)
    Sleep(200)

    def lambda_11F7():
        OP_8E(0xFE, 0x26C, 0x0, 0x19AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_11F7)
    Sleep(200)

    def lambda_1217():
        OP_8E(0xFE, 0x776, 0x0, 0x1450, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_1217)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x3)
    WaitChrThread(0x109, 0x3)
    WaitChrThread(0xF1, 0x3)
    WaitChrThread(0xF0, 0x3)

    ChrTalk(    #24
        0x109,
        (
            "#1064F#5PHuh? What's the Bracer Guild's emblem\x01",
            "doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1505F#5PIt looks like this really isn't a place that\x01",
            "exists in Liberl.\x02\x03",

            "#1502FAs far as I'm aware, there aren't any guild\x01",
            "facilities like this anywhere in the country.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BD")

    ChrTalk(    #26
        0x108,
        (
            "#074F#11PI'm not familiar with any, either.\x02\x03",

            "#072FNor am I aware of there being any buildings\x01",
            "like this in Calvard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15EF")

    label("loc_13BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1438")

    ChrTalk(    #27
        0x10D,
        (
            "#270F#11PThat settles that matter easily enough.\x01",
            "This is a recreation of a place in another\x01",
            "country.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15EF")

    label("loc_1438")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_149B")

    ChrTalk(    #28
        0x10B,
        (
            "#212F#11PThat's that, then. This is a copy of a place\x01",
            "in some other country.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15EF")

    label("loc_149B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151C")

    ChrTalk(    #29
        0x104,
        (
            "#1545F#11PThat seems to settle that matter, then.\x01",
            "This must be a recreation of a place in\x01",
            "another country.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15EF")

    label("loc_151C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1577")

    ChrTalk(    #30
        0x107,
        (
            "#065F#11PThen this is a copy of a place in some other\x01",
            "country, then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15EF")

    label("loc_1577")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15EF")

    ChrTalk(    #31
        0x10E,
        (
            "#178F#11PThat settles that matter easily enough.\x01",
            "This is a recreation of a place in another\x01",
            "country.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15EF")

    Sleep(300)
    Fade(500)
    OP_6D(-1200, 0, 7120, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(315000, 0)
    OP_6E(269, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #32
        0x109,
        (
            "#1078F#5PWould you look at that? The answer was right\x01",
            "under our noses the whole time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16C0():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16C0)
    Sleep(100)

    def lambda_16D3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_16D3)
    Sleep(100)
    OP_8C(0xF0, 180, 400)

    ChrTalk(    #33
        0x102,
        "#1504F#11PIt was?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-4650, 0, -980, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(315000, 0)
    OP_6E(265, 0)
    OP_43(0x109, 0x0, 0x0, 0x12)
    OP_43(0x102, 0x0, 0x0, 0x13)
    OP_43(0xF0, 0x0, 0x0, 0x14)
    OP_43(0xF1, 0x0, 0x0, 0x15)

    def lambda_1767():
        OP_6D(-3590, 0, -2410, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1767)

    def lambda_177F():
        OP_67(0, 7400, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_177F)

    def lambda_1797():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1797)

    def lambda_17A7():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17A7)

    def lambda_17B7():
        OP_6E(248, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_17B7)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x102, 0x0)
    Sleep(500)

    ChrTalk(    #34
        0x102,
        (
            "#1504F#12PThis is...'Le Locle Training Center'?\x02\x03",

            "I know that name...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x109,
        (
            "#1060F#6PWasn't it the training camp Estelle went\x01",
            "to a while back?\x02\x03",

            "You know, last year with Anelace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#1505F#12PThat's the one. It's a guild-owned facility located\x01",
            "in Leman State.\x02\x03",

            "#1503FI've never been there myself, though... I've only\x01",
            "heard about it from Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19AC")

    ChrTalk(    #37
        0x108,
        (
            "#070F#6PSo this is Le Locle, huh?\x02\x03",

            "I've never trained here personally, but it's\x01",
            "famous among bracers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A43")

    ChrTalk(    #38
        0x104,
        (
            "#1542F#6PThat leaves us with yet another problem to\x01",
            "solve.\x02\x03",

            "To my knowledge, Leman State is quite the\x01",
            "distance away from Liberl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D47")

    label("loc_1A43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AE1")

    ChrTalk(    #39
        0x105,
        (
            "#1163F#6PThat leaves us with yet another problem to\x01",
            "solve.\x02\x03",

            "Leman State is a fairly significant distance\x01",
            "away from Liberl, after all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D47")

    label("loc_1AE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B7E")

    ChrTalk(    #40
        0x10D,
        (
            "#272F#6PAnd no sooner do we solve one question,\x01",
            "we find ourselves with another.\x02\x03",

            "#270FLeman State is a fair distance away from\x01",
            "Liberl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D47")

    label("loc_1B7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C05")
    OP_A2(0x0)

    ChrTalk(    #41
        0x10B,
        (
            "#212F#6PStill, it's weird for us to be in a place in\x01",
            "Leman, right?\x02\x03",

            "I mean, it's really far away from Liberl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D47")

    label("loc_1C05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CAE")

    ChrTalk(    #42
        0x10E,
        (
            "#176F#6PStill, that leaves us with yet another problem\x01",
            "to solve.\x02\x03",

            "#178FLeman State is a fairly significant distance\x01",
            "away from Liberl, after all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D47")

    label("loc_1CAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D47")
    OP_A2(0x3)

    ChrTalk(    #43
        0x107,
        (
            "#064F#6PGrandpa's over in Leman on vacation right\x01",
            "now, come to think of it...\x02\x03",

            "#065F...Wait. Isn't it really far away from Liberl?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E08")

    ChrTalk(    #44
        0x109,
        (
            "#1063F#5PYeah, it is. It's farther away than both\x01",
            "Erebonia and Calvard.\x02\x03",

            "#1065FBut you know? I may not have a clue how\x01",
            "a place in Leman ended up being created\x01",
            "here or why...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EBB")

    label("loc_1E08")


    ChrTalk(    #45
        0x109,
        (
            "#1063F#5PYeah, it is. It's farther away than both\x01",
            "Erebonia and Calvard.\x02\x03",

            "#1065FBut you know? I may not have a clue how\x01",
            "a place in Leman ended up being created\x01",
            "here or why...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EBB")

    OP_A3(0x0)
    OP_A3(0x3)
    OP_8C(0x102, 180, 400)
    Sleep(300)

    ChrTalk(    #46
        0x102,
        (
            "#1505F#11P...but if our enemies did it, they must have\x01",
            "had a reason for doing so.\x02\x03",

            "#1500FRight?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #47
        0x109,
        "#1060F#6PHeh. I knew you'd catch on.\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x194, 0x0, 0x64)
    Sleep(150)
    OP_22(0x194, 0x0, 0x64)
    Sleep(500)
    OP_22(0x193, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FEB")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2052")

    label("loc_1FEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2013")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2052")

    label("loc_2013")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_203B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2052")

    label("loc_203B")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2052")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_207F")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20E6")

    label("loc_207F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A7")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20E6")

    label("loc_20A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20CF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20E6")

    label("loc_20CF")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_20E6")

    Sleep(1000)

    def lambda_20F1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_20F1)
    Sleep(50)

    def lambda_2104():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2104)
    Sleep(50)

    def lambda_2117():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2117)
    Sleep(50)
    OP_8C(0xF0, 180, 400)
    OP_1D(0x97)
    Sleep(500)

    ChrTalk(    #48
        0x102,
        "#1502F#11PThat sounded like...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        "#1063F#5PWe've got company, guys!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    ClearMapFlags(0x10)
    OP_6D(1130, 1300, -8000, 0)
    OP_67(0, 5790, -10000, 0)
    OP_6B(8150, 0)
    OP_6C(212000, 0)
    OP_6E(138, 0)

    def lambda_21D0():
        OP_6D(-330, 0, -11660, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_21D0)
    SetChrPos(0x109, -1520, 0, -4240, 180)
    SetChrPos(0x102, -1320, 0, -2650, 180)
    SetChrPos(0xF0, -80, 0, -4390, 180)
    SetChrPos(0xF1, 190, 0, -2460, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, -2780, 0, -27580, 0)
    SetChrPos(0x11, -1780, 0, -26660, 0)
    SetChrPos(0x12, 450, 0, -27500, 0)
    OP_43(0x10, 0x0, 0x0, 0xB)
    OP_43(0x12, 0x0, 0x0, 0xD)
    OP_43(0x11, 0x0, 0x0, 0xC)
    Sleep(500)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x14, 7060, 4250, -18070, 315)
    SetChrPos(0x15, 7770, 4250, -16870, 315)
    SetChrPos(0x16, 8900, 4250, -17550, 315)
    OP_43(0x14, 0x0, 0x0, 0xF)
    Sleep(100)
    OP_43(0x15, 0x0, 0x0, 0x10)
    Sleep(100)
    OP_43(0x16, 0x0, 0x0, 0x11)
    WaitChrThread(0x109, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2348")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_23AF")

    label("loc_2348")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2370")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_23AF")

    label("loc_2370")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2398")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_23AF")

    label("loc_2398")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_23AF")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23DC")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2443")

    label("loc_23DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2404")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2443")

    label("loc_2404")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_242C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2443")

    label("loc_242C")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2443")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_246D")

    ChrTalk(    #50
        0x107,
        "#065F#5PUh-oh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F4")

    label("loc_246D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2495")

    ChrTalk(    #51
        0x105,
        "#1164F#5POh no...\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F4")

    label("loc_2495")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24D1")

    ChrTalk(    #52
        0x10B,
        "#216F#5PWh-Where did they come from?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F4")

    label("loc_24D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24F4")

    ChrTalk(    #53
        0x104,
        "#1540F#5PHuh...\x02",
    )

    CloseMessageWindow()

    label("loc_24F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_254B")

    ChrTalk(    #54
        0x10D,
        (
            "#277F#5PHmph. I should have known foes would\x01",
            "show up eventually.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25AC")

    label("loc_254B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_257D")

    ChrTalk(    #55
        0x10E,
        "#178F#5POn guard, everyone.\x02",
    )

    CloseMessageWindow()
    Jump("loc_25AC")

    label("loc_257D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25AC")

    ChrTalk(    #56
        0x108,
        "#072F#5PHere comes trouble.\x02",
    )

    CloseMessageWindow()

    label("loc_25AC")

    Sleep(150)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 8)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x102, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 10)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 11)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0x102,
        (
            "#1502F#5PI suppose 'beastmen' would be the best term\x01",
            "for these things.\x02\x03",

            "This is probably what 'Your next destination\x01",
            "is the path of beasts' was referring to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x109,
        (
            "#1065F#5PAnother mystery solved.\x02\x03",

            "#1069FWatch out! There's a lot of them,\x01",
            "and this could get ugly!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x10, 0x0, 0x0, 0x4)
    OP_43(0x11, 0x0, 0x0, 0x5)
    OP_43(0x12, 0x0, 0x0, 0x6)
    OP_43(0x14, 0x0, 0x0, 0x8)
    OP_43(0x15, 0x0, 0x0, 0x9)
    OP_43(0x16, 0x0, 0x0, 0xA)

    def lambda_2750():
        OP_6D(-370, 0, -6510, 600)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2750)

    def lambda_2768():
        OP_67(0, 7770, -10000, 600)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2768)

    def lambda_2780():
        OP_6B(4200, 600)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2780)

    def lambda_2790():
        OP_6C(213000, 600)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2790)

    def lambda_27A0():
        OP_6E(169, 600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27A0)
    WaitChrThread(0x109, 0x0)
    Battle(0x1A2, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_28A end

    def Function_4_27BD(): pass

    label("Function_4_27BD")

    Sleep(10)

    def lambda_27C8():

        label("loc_27C8")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_27C8")

    QueueWorkItem2(0xFE, 3, lambda_27C8)
    SetChrChipByIndex(0xFE, 1)
    OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1B58, 0x0)
    Return()

    # Function_4_27BD end

    def Function_5_27EF(): pass

    label("Function_5_27EF")


    def lambda_27F5():

        label("loc_27F5")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_27F5")

    QueueWorkItem2(0xFE, 3, lambda_27F5)
    SetChrChipByIndex(0xFE, 1)
    OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1B58, 0x0)
    Return()

    # Function_5_27EF end

    def Function_6_281C(): pass

    label("Function_6_281C")


    def lambda_2822():

        label("loc_2822")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_2822")

    QueueWorkItem2(0xFE, 3, lambda_2822)
    SetChrChipByIndex(0xFE, 1)
    OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1B58, 0x0)
    Return()

    # Function_6_281C end

    def Function_7_2849(): pass

    label("Function_7_2849")

    Sleep(5)

    def lambda_2854():

        label("loc_2854")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_2854")

    QueueWorkItem2(0xFE, 3, lambda_2854)
    SetChrChipByIndex(0xFE, 1)
    OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1B58, 0x0)
    Return()

    # Function_7_2849 end

    def Function_8_287B(): pass

    label("Function_8_287B")

    Sleep(10)

    def lambda_2886():

        label("loc_2886")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_2886")

    QueueWorkItem2(0xFE, 3, lambda_2886)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x12FC, 0xF64, 0xFFFFD274, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 4)

    def lambda_28BB():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_28BB)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_28D0():
        OP_96(0xFE, 0xC8, 0x0, 0xFFFFEA2A, 0x708, 0x2710)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28D0)
    Return()

    # Function_8_287B end

    def Function_9_28E9(): pass

    label("Function_9_28E9")


    def lambda_28EF():

        label("loc_28EF")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_28EF")

    QueueWorkItem2(0xFE, 3, lambda_28EF)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x168A, 0xF64, 0xFFFFD670, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 4)

    def lambda_2924():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2924)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_2939():
        OP_96(0xFE, 0x21C, 0x0, 0xFFFFEC1E, 0x7D0, 0x2710)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2939)
    Return()

    # Function_9_28E9 end

    def Function_10_2952(): pass

    label("Function_10_2952")

    Sleep(15)

    def lambda_295D():

        label("loc_295D")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_295D")

    QueueWorkItem2(0xFE, 3, lambda_295D)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x1982, 0xF64, 0xFFFFD42C, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 4)

    def lambda_2992():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2992)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_29A7():
        OP_96(0xFE, 0x3FC, 0x0, 0xFFFFF3EE, 0x898, 0x2710)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29A7)
    Return()

    # Function_10_2952 end

    def Function_11_29C0(): pass

    label("Function_11_29C0")

    Sleep(20)

    def lambda_29CB():

        label("loc_29CB")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_29CB")

    QueueWorkItem2(0xFE, 3, lambda_29CB)
    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0xFFFFF95C, 0x0, 0xFFFFD49A, 0x1770, 0x0)

    def lambda_29F7():

        label("loc_29F7")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_29F7")

    QueueWorkItem2(0xFE, 3, lambda_29F7)
    SetChrChipByIndex(0xFE, 0)
    Return()

    # Function_11_29C0 end

    def Function_12_2A0A(): pass

    label("Function_12_2A0A")

    Sleep(35)

    def lambda_2A15():

        label("loc_2A15")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_2A15")

    QueueWorkItem2(0xFE, 3, lambda_2A15)
    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0xFFFFFF2E, 0x0, 0xFFFFD81E, 0x1770, 0x0)

    def lambda_2A41():

        label("loc_2A41")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2A41")

    QueueWorkItem2(0xFE, 3, lambda_2A41)
    SetChrChipByIndex(0xFE, 0)
    Return()

    # Function_12_2A0A end

    def Function_13_2A54(): pass

    label("Function_13_2A54")

    Sleep(45)

    def lambda_2A5F():

        label("loc_2A5F")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_2A5F")

    QueueWorkItem2(0xFE, 3, lambda_2A5F)
    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0x424, 0x0, 0xFFFFD63E, 0x1770, 0x0)

    def lambda_2A8B():

        label("loc_2A8B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2A8B")

    QueueWorkItem2(0xFE, 3, lambda_2A8B)
    SetChrChipByIndex(0xFE, 0)
    Return()

    # Function_13_2A54 end

    def Function_14_2A9E(): pass

    label("Function_14_2A9E")

    Sleep(15)

    def lambda_2AA9():

        label("loc_2AA9")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_2AA9")

    QueueWorkItem2(0xFE, 3, lambda_2AA9)
    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0x5BE, 0x0, 0xFFFFD238, 0x1770, 0x0)

    def lambda_2AD5():

        label("loc_2AD5")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2AD5")

    QueueWorkItem2(0xFE, 3, lambda_2AD5)
    SetChrChipByIndex(0xFE, 0)
    Return()

    # Function_14_2A9E end

    def Function_15_2AE8(): pass

    label("Function_15_2AE8")

    Sleep(300)

    def lambda_2AF3():

        label("loc_2AF3")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2AF3")

    QueueWorkItem2(0xFE, 3, lambda_2AF3)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x14AA, 0x109A, 0xFFFFCDF6, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    Return()

    # Function_15_2AE8 end

    def Function_16_2B1F(): pass

    label("Function_16_2B1F")

    Sleep(200)

    def lambda_2B2A():

        label("loc_2B2A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2B2A")

    QueueWorkItem2(0xFE, 3, lambda_2B2A)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x1978, 0x109A, 0xFFFFD45E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    Return()

    # Function_16_2B1F end

    def Function_17_2B56(): pass

    label("Function_17_2B56")

    Sleep(400)

    def lambda_2B61():

        label("loc_2B61")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2B61")

    QueueWorkItem2(0xFE, 3, lambda_2B61)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x1D60, 0x109A, 0xFFFFCEFA, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    Return()

    # Function_17_2B56 end

    def Function_18_2B8D(): pass

    label("Function_18_2B8D")

    OP_8E(0xFE, 0xFFFFF790, 0x0, 0xFFFFEEA8, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_18_2B8D end

    def Function_19_2BA9(): pass

    label("Function_19_2BA9")

    Sleep(200)
    OP_8E(0xFE, 0xFFFFF704, 0x0, 0xFFFFF48E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_19_2BA9 end

    def Function_20_2BCA(): pass

    label("Function_20_2BCA")

    OP_8E(0xFE, 0xFFFFFE5C, 0x0, 0xFFFFEED0, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_20_2BCA end

    def Function_21_2BE6(): pass

    label("Function_21_2BE6")

    Sleep(200)
    OP_8E(0xFE, 0xFFFFFDDA, 0x0, 0xFFFFF4E8, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_21_2BE6 end

    def Function_22_2C07(): pass

    label("Function_22_2C07")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_44(0x16, 0x0)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x16, 0x1)
    OP_E0(265, 0x48, 0x2)
    OP_E0(258, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x2)
    OP_E0(241, 0x4B, 0x2)
    SetChrPos(0x109, -1760, 0, -4430, 180)
    SetChrPos(0x102, -2070, 0, -2700, 180)
    SetChrPos(0xF0, -400, 0, -4370, 135)
    SetChrPos(0xF1, -530, 0, -2720, 135)
    SetChrChipByIndex(0x109, 8)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF0, 10)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 11)
    SetChrSubChip(0xF1, 0)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -2040, 0, -8580, 0)
    SetChrPos(0x11, -460, 0, -8420, 0)
    SetChrChipByIndex(0x10, 0)
    SetChrChipByIndex(0x11, 0)

    def lambda_2D0B():

        label("loc_2D0B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2D0B")

    QueueWorkItem2(0x10, 3, lambda_2D0B)

    def lambda_2D1E():

        label("loc_2D1E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2D1E")

    QueueWorkItem2(0x11, 3, lambda_2D1E)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 2670, 0, -7050, 315)
    SetChrChipByIndex(0x14, 2)

    def lambda_2D56():

        label("loc_2D56")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2D56")

    QueueWorkItem2(0x14, 3, lambda_2D56)
    OP_6D(-160, 0, -7560, 0)
    OP_67(0, 6830, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(189000, 0)
    OP_6E(298, 0)
    OP_43(0x10, 0x0, 0x0, 0x17)
    OP_43(0x11, 0x0, 0x0, 0x18)
    OP_43(0x14, 0x0, 0x0, 0x19)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x194, 0x0, 0x64)
    Sleep(150)
    OP_22(0x194, 0x0, 0x64)
    Sleep(500)
    OP_22(0x193, 0x0, 0x64)
    Sleep(1000)

    def lambda_2DE3():
        OP_6D(1120, 1600, -7240, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2DE3)

    def lambda_2DFB():
        OP_67(0, 6830, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2DFB)

    def lambda_2E13():
        OP_6B(3080, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2E13)

    def lambda_2E23():
        OP_6E(310, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2E23)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(500)
    OP_6D(-2310, 0, -2720, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(314000, 0)
    OP_6E(279, 0)
    OP_0D()
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
    Sleep(500)

    ChrTalk(    #59
        0x109,
        (
            "#1075F#5PHeh. Fleeing to fight another day, huh?\x02\x03",

            "#1840FThey're smart little devils.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        (
            "#1505F#5PDevils DO seem a lot more intelligent than your\x01",
            "average monster.\x02\x03",

            "#1502FEnough to make me wonder whether these are\x01",
            "another kind of 'impossible fiend' like the rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x109,
        (
            "#1063F#5PI'm with you. I can't pretend to be an expert\x01",
            "on the monsters of Leman, but I'm preeetty\x01",
            "sure they're not this smart.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30BA")

    ChrTalk(    #62
        0x10B,
        "#413F#5P*sigh* This plane's gonna be sooo much fun.\x02",
    )

    CloseMessageWindow()
    Jump("loc_326E")

    label("loc_30BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3110")

    ChrTalk(    #63
        0x107,
        (
            "#062F#5PThis plane isn't going to let up any time soon,\x01",
            "huh...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_326E")

    label("loc_3110")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_316A")

    ChrTalk(    #64
        0x10E,
        (
            "#178F#5PIt looks like this plane is going to pose\x01",
            "a real challenge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_326E")

    label("loc_316A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31C4")

    ChrTalk(    #65
        0x10D,
        (
            "#277F#5PIt looks like this plane is going to pose\x01",
            "a real challenge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_326E")

    label("loc_31C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_321F")

    ChrTalk(    #66
        0x105,
        (
            "#1162F#5PIt looks like this plane is going to pose\x01",
            "a real challenge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_326E")

    label("loc_321F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_326E")

    ChrTalk(    #67
        0x104,
        (
            "#1545F#5PIt looks like this plane stands to be a real\x01",
            "ball.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326E")

    Sleep(300)
    OP_22(0x15F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32DD")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3344")

    label("loc_32DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3305")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3344")

    label("loc_3305")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3344")

    label("loc_332D")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3344")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3371")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_33D8")

    label("loc_3371")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3399")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_33D8")

    label("loc_3399")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C1")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_33D8")

    label("loc_33C1")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_33D8")

    Sleep(1000)

    def lambda_33E3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_33E3)
    Sleep(100)
    OP_8C(0xF0, 270, 400)
    Sleep(300)

    ChrTalk(    #68
        0x109,
        "#1069F#5PHere she comes!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x109, 0x20)
    SetChrChipByIndex(0x109, 5)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -1660, 500, 1000, 180)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3471():

        label("loc_3471")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_3471")

    QueueWorkItem2(0x17, 2, lambda_3471)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x96, 0x5DC)

    def lambda_3494():
        OP_6D(-2510, 200, -1000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3494)

    def lambda_34AC():
        OP_67(0, 6540, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_34AC)

    def lambda_34C4():
        OP_6B(2720, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_34C4)

    def lambda_34D4():
        OP_6E(279, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_34D4)

    def lambda_34E4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34E4)
    Sleep(100)

    def lambda_34F7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_34F7)
    Sleep(100)
    OP_8C(0xF0, 0, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #69
        (
            "\x07\x0C\x18#2S#80W...You have done well...\x01",
            "...to come this far...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #70
        (
            "\x07\x0C\x18#2S#80WOn this plane there are...\x01",
            "three ordeals to overcome...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #71
        (
            "\x07\x0C\x18#2S#80WIf you overcome them all...\x01",
            "...the next path will open...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #72
        "\x07\x0C\x18#2S#80W...Take...this...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x20)
    SetChrPos(0x18, -1830, 500, -3500, 180)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x99, 0x0, 0x64)

    def lambda_3666():
        OP_8F(0xFE, 0xFFFFF8DA, 0xFFFFFED4, 0xFFFFF254, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3666)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    WaitChrThread(0x18, 0x1)
    Sleep(500)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #73
        "\x07\x05The ghost handed them a \x1F\x2C\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x32C, 1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #74
        "\x07\x0C\x18#2S#80W...Be...forewarned...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #75
        (
            "\x07\x0C\x18#2S#80WThe Lord of Phantasma's goal...\x01",
            "...is...your...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    OP_82(0x1, 0x2)
    SetChrFlags(0x17, 0x80)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37E9")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3841")

    label("loc_37E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380C")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3841")

    label("loc_380C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382F")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3841")

    label("loc_382F")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3841")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3864")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_38BC")

    label("loc_3864")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3887")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_38BC")

    label("loc_3887")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38AA")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_38BC")

    label("loc_38AA")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_38BC")

    Sleep(500)
    OP_6D(-2310, 0, -2500, 1500)
    OP_63(0x109)
    OP_63(0x102)
    OP_63(0xF0)
    OP_63(0xF1)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #76
        0x109,
        (
            "#1841F#6P...Well, she sure didn't stick around long.\x02\x03",

            "#1063FShe's probably got so little power left now,\x01",
            "it's difficult for her to show herself to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#1505F#5PSo it seems. It must be a frustrating thing\x01",
            "for her to deal with.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39EA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39EA)
    Sleep(100)

    def lambda_39FD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_39FD)
    Sleep(100)
    OP_8C(0xF0, 270, 400)
    Sleep(300)

    ChrTalk(    #78
        0x102,
        "#1500F#11PStill, she left us with a useful gift.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x109,
        "#1060F#6PYeah...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #80
        "\x07\x05Kevin opened the map of Le Locle.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x12, 0x0, 0x64)
    OP_AD(0x2400C9, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    FadeToBright(0, 0)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #81
        (
            "\x07\x00#1063FOookay...it looks like the lodge in the top\x01",
            "right is where we are now.\x02\x03",

            "Then there's this 'Balstar Channel' place\x01",
            "to the left of it.\x02\x03",

            "Maybe that's the ordeal she mentioned? \x01",
            "Or one of them, at least.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C7C")
    OP_A2(0x7)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #82
        (
            "\x07\x00#074FShe mentioned there being three of them,\x01",
            "but there's only one place that could fit\x01",
            "that description marked on the map.\x02\x03",

            "#072FI wonder where the other two could be.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_409A")

    label("loc_3C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D54")
    OP_A2(0x6)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #83
        (
            "\x07\x00#1545FShe mentioned there being three of them,\x01",
            "but there's only one place that could fit\x01",
            "that description marked on the map.\x02\x03",

            "#1540FI wonder where the other two could be.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_409A")

    label("loc_3D54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E23")
    OP_A2(0x5)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("Kloe")

    AnonymousTalk(    #84
        (
            "\x07\x00#1163FShe mentioned there being three of them,\x01",
            "but there's only one place that could fit\x01",
            "that description marked on the map.\x02\x03",

            "I wonder where the other two could be.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_409A")

    label("loc_3E23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EF9")
    OP_A2(0x2)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("Mueller")

    AnonymousTalk(    #85
        (
            "\x07\x00#272FShe mentioned there being three of them,\x01",
            "but there's only one place that could fit\x01",
            "that description marked on the map.\x02\x03",

            "#270FI wonder where the other two could be.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_409A")

    label("loc_3EF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FCD")
    OP_A2(0x1)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("Julia")

    AnonymousTalk(    #86
        (
            "\x07\x00#176FShe mentioned there being three of them,\x01",
            "but there's only one place that could fit\x01",
            "that description marked on the map.\x02\x03",

            "#178FI wonder where the other two could be.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_409A")

    label("loc_3FCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_409A")
    OP_A2(0x0)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #87
        (
            "\x07\x00#063FYeah, it probably is...but then she said we\x01",
            "need to do three of them, and there's only\x01",
            "one place on here that it fits...\x02\x03",

            "I wonder where the other two could be.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_409A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41E0")
    SetMessageWindowPos(80, 80, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #88
        (
            "\x07\x00#1505FFrom what I can see, these two roads lead to\x01",
            "them--the ones that seem to just stop all of a\x01",
            "sudden.\x02\x03",

            "#1502FBut this plane most likely has its own rules\x01",
            "that we need to follow.\x02\x03",

            "If we followed those roads now, there's a big\x01",
            "chance we'd find a whole lotta nothing at the\x01",
            "end of them.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4305")

    label("loc_41E0")

    SetMessageWindowPos(80, 80, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #89
        (
            "\x07\x00#1505FFrom what I can see, these two roads lead to\x01",
            "them--the ones that seem to just stop all of a\x01",
            "sudden.\x02\x03",

            "#1502FBut this plane most likely has its own rules\x01",
            "we need to follow.\x02\x03",

            "If we followed those roads now, there's a big\x01",
            "chance we'd find nothing at the end of them.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4305")

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #90
        (
            "\x07\x00#1067FUnfortunately...\x02\x03",

            "#1060FWell, those are the cards we've been dealt.\x01",
            "Let's just try heading over to the Balstar\x01",
            "Channel and see what comes of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_A2(0x2902)
    OP_28(0x32, 0x1, 0x8)
    OP_28(0x32, 0x1, 0x10)
    OP_28(0x32, 0x1, 0x20)
    OP_28(0x32, 0x1, 0x40)
    OP_28(0x32, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_22_2C07 end

    def Function_23_43EA(): pass

    label("Function_23_43EA")

    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0xFFFFF7EA, 0x0, 0xFFFFDA9E, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(2500)
    OP_8C(0xFE, 180, 600)
    SetChrChipByIndex(0xFE, 1)

    def lambda_441F():

        label("loc_441F")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_441F")

    QueueWorkItem2(0xFE, 3, lambda_441F)
    OP_8F(0xFE, 0xFFFFF952, 0x0, 0xFFFFA2E0, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_43EA end

    def Function_24_4446(): pass

    label("Function_24_4446")

    Sleep(150)
    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0xFFFFFE84, 0x0, 0xFFFFDC4C, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(2700)
    OP_8C(0xFE, 180, 600)
    SetChrChipByIndex(0xFE, 1)

    def lambda_4480():

        label("loc_4480")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_4480")

    QueueWorkItem2(0xFE, 3, lambda_4480)
    OP_8F(0xFE, 0xFFFFFFA6, 0x0, 0xFFFFA416, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_24_4446 end

    def Function_25_44A7(): pass

    label("Function_25_44A7")

    Sleep(55)
    SetChrChipByIndex(0xFE, 3)
    OP_8F(0xFE, 0xC12, 0x0, 0xFFFFE1C4, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 2)
    Sleep(2800)
    OP_8C(0xFE, 135, 600)
    SetChrChipByIndex(0xFE, 3)
    OP_8F(0xFE, 0xFD2, 0x0, 0xFFFFDD96, 0x1B58, 0x0)
    OP_22(0xCB, 0x0, 0x64)
    SetChrSubChip(0x0, 2)

    def lambda_44FF():
        OP_96(0xFE, 0x1590, 0xFA0, 0xFFFFD24C, 0x1194, 0x1F40)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44FF)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_4527():

        label("loc_4527")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_4527")

    QueueWorkItem2(0xFE, 3, lambda_4527)
    OP_8F(0xFE, 0x22B0, 0x1054, 0xFFFFBAF0, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_44A7 end

    def Function_26_454E(): pass

    label("Function_26_454E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-450, 3500, 3820, 0)
    OP_67(0, 7420, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(315000, 0)
    OP_6E(385, 0)

    def lambda_459D():
        OP_6D(1530, -5000, 47780, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_459D)

    def lambda_45B5():
        OP_67(0, 9860, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_45B5)

    def lambda_45CD():
        OP_6B(3820, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_45CD)

    def lambda_45DD():
        OP_6E(385, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_45DD)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(2000)
    OP_22(0x1DA, 0x0, 0x64)
    OP_22(0x345, 0x1, 0x64)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A2(0x2504)
    OP_A2(0x2509)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_454E end

    def Function_27_4681(): pass

    label("Function_27_4681")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_46A4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46B5")

    label("loc_46A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_46B5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46B5")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_46DA"),
        (1, "loc_4709"),
        (2, "loc_4738"),
        (SWITCH_DEFAULT, "loc_4767"),
    )


    label("loc_46DA")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    Jump("loc_4767")

    label("loc_4709")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    Jump("loc_4767")

    label("loc_4738")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    Jump("loc_4767")

    label("loc_4767")

    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_479C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A8F")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_47C7"),
        (1, "loc_47EF"),
        (2, "loc_482A"),
        (SWITCH_DEFAULT, "loc_4876"),
    )


    label("loc_47C7")


    Menu(
        0,
        30,
        80,
        0,
        (
            "Guild Lodge\x01",          # 0
            "Balstar Channel\x01",      # 1
        )
    )

    Jump("loc_4876")

    label("loc_47EF")


    Menu(
        0,
        30,
        80,
        0,
        (
            "Guild Lodge\x01",             # 0
            "Balstar Channel\x01",         # 1
            "Saint-Croix Forest\x01",      # 2
        )
    )

    Jump("loc_4876")

    label("loc_482A")


    Menu(
        0,
        30,
        80,
        0,
        (
            "Guild Lodge\x01",             # 0
            "Balstar Channel\x01",         # 1
            "Saint-Croix Forest\x01",      # 2
            "Grimsel Fortress\x01",        # 3
        )
    )

    Jump("loc_4876")

    label("loc_4876")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_48A0"),
        (1, "loc_4917"),
        (2, "loc_4992"),
        (3, "loc_4A10"),
        (SWITCH_DEFAULT, "loc_4A8C"),
    )


    label("loc_48A0")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #91
        "\x07\x05Travel to [Guild Lodge]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4904"),
        (1, "loc_4911"),
        (SWITCH_DEFAULT, "loc_4914"),
    )


    label("loc_4904")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4914")

    label("loc_4911")

    Jump("loc_4914")

    label("loc_4914")

    Jump("loc_4A8C")

    label("loc_4917")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #92
        "\x07\x05Travel to [Balstar Channel]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_497F"),
        (1, "loc_498C"),
        (SWITCH_DEFAULT, "loc_498F"),
    )


    label("loc_497F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_498F")

    label("loc_498C")

    Jump("loc_498F")

    label("loc_498F")

    Jump("loc_4A8C")

    label("loc_4992")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #93
        "\x07\x05Travel to [Saint-Croix Forest]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_49FD"),
        (1, "loc_4A0A"),
        (SWITCH_DEFAULT, "loc_4A0D"),
    )


    label("loc_49FD")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A0D")

    label("loc_4A0A")

    Jump("loc_4A0D")

    label("loc_4A0D")

    Jump("loc_4A8C")

    label("loc_4A10")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #94
        "\x07\x05Travel to [Grimsel Fortress]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4A79"),
        (1, "loc_4A86"),
        (SWITCH_DEFAULT, "loc_4A89"),
    )


    label("loc_4A79")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A89")

    label("loc_4A86")

    Jump("loc_4A89")

    label("loc_4A89")

    Jump("loc_4A8C")

    label("loc_4A8C")

    Jump("loc_479C")

    label("loc_4A8F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4AA8"),
        (1, "loc_4ADC"),
        (2, "loc_4B10"),
        (3, "loc_4B44"),
        (SWITCH_DEFAULT, "loc_4B78"),
    )


    label("loc_4AA8")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_4B78")

    label("loc_4ADC")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_4B78")

    label("loc_4B10")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_4B78")

    label("loc_4B44")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_4B78")

    label("loc_4B78")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4B9A"),
        (1, "loc_4BA6"),
        (2, "loc_4BB2"),
        (3, "loc_4BBE"),
        (SWITCH_DEFAULT, "loc_4BCA"),
    )


    label("loc_4B9A")

    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_4BCA")

    label("loc_4BA6")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_4BCA")

    label("loc_4BB2")

    NewScene("ED6_DT21/M5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_4BCA")

    label("loc_4BBE")

    NewScene("ED6_DT21/M5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_4BCA")

    label("loc_4BCA")

    Return()

    # Function_27_4681 end

    def Function_28_4BCB(): pass

    label("Function_28_4BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BDC")
    Call(0, 2)
    Return()

    label("loc_4BDC")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 7450, 0, 5550, 180)
    SetChrPos(0x1, 6540, 0, 6210, 180)
    SetChrPos(0x2, 8230, 0, 6140, 180)
    SetChrPos(0x3, 7310, 0, 7160, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 7240, 0, 6380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 30)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x104), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_28_4BCB end

    def Function_29_4CBA(): pass

    label("Function_29_4CBA")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 7450, 0, 5430, 0)
    SetChrPos(0x2, 6540, 0, 6210, 0)
    SetChrPos(0x1, 8230, 0, 6140, 0)
    SetChrPos(0x0, 7310, 0, 7160, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 7240, 0, 6380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 31)
    NewScene("ED6_DT21/M7107   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_29_4CBA end

    def Function_30_4D76(): pass

    label("Function_30_4D76")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D9F")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4D93():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4D93)

    label("loc_4D9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DC8")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4DBC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4DBC)

    label("loc_4DC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DF1")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4DE5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4DE5)

    label("loc_4DF1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E1A")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4E0E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4E0E)

    label("loc_4E1A")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E46")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4E46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E5D")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4E5D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E74")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4E74")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E8B")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4E8B")

    Return()

    # Function_30_4D76 end

    def Function_31_4E8C(): pass

    label("Function_31_4E8C")


    def lambda_4E92():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4E92)

    def lambda_4EA4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4EA4)

    def lambda_4EB6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4EB6)

    def lambda_4EC8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4EC8)
    Sleep(1000)
    Return()

    # Function_31_4E8C end

    def Function_32_4EDA(): pass

    label("Function_32_4EDA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #95
        "\x07\x05Le Locle Training Center\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_32_4EDA end

    SaveToFile()

Try(main)
