from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4250   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4250.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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
        'Skull Head',                           # 9
        'Skull Head',                           # 10
        'Skull Head',                           # 11
        'Skull Head',                           # 12
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
        'ED6_DT29/CH14450 ._CH',             # 00
        'ED6_DT29/CH14450 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT29/CH14450P._CP',             # 00
        'ED6_DT29/CH14450P._CP',             # 01
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -140,
        TriggerZ            = 1000,
        TriggerY            = 1520,
        TriggerRange        = 1000,
        ActorX              = -140,
        ActorZ              = 3000,
        ActorY              = 1520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_174",          # 01, 1
        "Function_2_186",          # 02, 2
        "Function_3_C72",          # 03, 3
        "Function_4_CD3",          # 04, 4
        "Function_5_D34",          # 05, 5
        "Function_6_D95",          # 06, 6
        "Function_7_DF6",          # 07, 7
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_173")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_173")

    Return()

    # Function_0_15E end

    def Function_1_174(): pass

    label("Function_1_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185")
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)

    label("loc_185")

    Return()

    # Function_1_174 end

    def Function_2_186(): pass

    label("Function_2_186")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(238, 0x42, 0x2)
    OP_E0(239, 0x43, 0x2)
    OP_E0(240, 0x44, 0x2)
    OP_E0(241, 0x45, 0x2)
    SetChrPos(0x109, -1030, 0, -25890, 0)
    SetChrPos(0x10F, 280, 0, -26320, 0)
    SetChrPos(0xF0, -1200, 0, -26590, 0)
    SetChrPos(0xF1, 390, 0, -26590, 0)
    OP_6D(-610, 12950, 19400, 0)
    OP_67(0, 8460, -10000, 0)
    OP_6B(3310, 0)
    OP_6C(45000, 0)
    OP_6E(344, 0)
    FadeToBright(2000, 0)

    def lambda_236():
        OP_6D(190, 1700, -14550, 9000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_236)

    def lambda_24E():
        OP_67(0, 8470, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_24E)

    def lambda_266():
        OP_6B(3310, 9000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_266)

    def lambda_276():
        OP_6C(45000, 9000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_276)

    def lambda_286():
        OP_6E(344, 9000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_286)
    Sleep(4000)

    def lambda_29B():
        OP_8E(0xFE, 0xFFFFFBBE, 0x0, 0xFFFFC72A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_29B)
    Sleep(300)

    def lambda_2BB():
        OP_8E(0xFE, 0x230, 0x0, 0xFFFFC6BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2BB)
    Sleep(300)

    def lambda_2DB():
        OP_8E(0xFE, 0xFFFFFB1E, 0x0, 0xFFFFC0FF, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2DB)
    Sleep(300)

    def lambda_2FB():
        OP_8E(0xFE, 0x10E, 0x0, 0xFFFFC054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2FB)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    OP_6D(780, 0, -14130, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(45000, 0)
    OP_6E(298, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38D")

    ChrTalk(    #0
        0x10E,
        "#178F...\x02",
    )

    CloseMessageWindow()

    label("loc_38D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D7")

    ChrTalk(    #1
        0x102,
        "#1503FWell, there doesn't seem to be anyone inside.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BF")

    label("loc_3D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_436")

    ChrTalk(    #2
        0x10D,
        (
            "#276FAs we expected, there doesn't seem to be anyone\x01",
            "inside here at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF")

    label("loc_436")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47B")

    ChrTalk(    #3
        0x10B,
        "#215FW-Well, looks like this place is empty...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BF")

    label("loc_47B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BF")

    ChrTalk(    #4
        0x107,
        "#063FIt looks like the castle really is empty...\x02",
    )

    CloseMessageWindow()

    label("loc_4BF")


    ChrTalk(    #5
        0x109,
        "#1067F#5P...We're not alone, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        "#1441F#5PBe careful. They are gathering.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_534")

    ChrTalk(    #7
        0x10E,
        "#172F...!\x02",
    )

    CloseMessageWindow()

    label("loc_534")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_556")

    ChrTalk(    #8
        0x107,
        "#065FThey?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BD")

    label("loc_556")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57D")

    ChrTalk(    #9
        0x10B,
        "#213FWh-Wha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BD")

    label("loc_57D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59E")

    ChrTalk(    #10
        0x10D,
        "#273F...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BD")

    label("loc_59E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BD")

    ChrTalk(    #11
        0x102,
        "#1502F...?!\x02",
    )

    CloseMessageWindow()

    label("loc_5BD")

    LoadEffect(0x1, "map\\mp258_00.eff")
    OP_20(0x7D0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FD")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_664")

    label("loc_5FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_625")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_664")

    label("loc_625")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_664")

    label("loc_64D")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_664")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_691")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6F8")

    label("loc_691")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B9")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6F8")

    label("loc_6B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E1")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6F8")

    label("loc_6E1")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6F8")

    Sleep(1000)

    def lambda_703():
        OP_6D(1030, 0, -10500, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_703)

    def lambda_71B():
        OP_67(0, 5900, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_71B)

    def lambda_733():
        OP_6B(2730, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_733)

    def lambda_743():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_743)

    def lambda_753():
        OP_6E(338, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_753)
    WaitChrThread(0x109, 0x0)
    OP_22(0x32E, 0x0, 0x64)
    OP_43(0x10, 0x0, 0x0, 0x3)
    Sleep(100)
    OP_43(0x11, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x5)
    Sleep(100)
    OP_43(0x13, 0x0, 0x0, 0x6)
    WaitChrThread(0x13, 0x0)
    OP_23(0x137)
    OP_1D(0x97)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 3)
    SetChrSubChip(0x10F, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 4)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 5)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #12
        0x109,
        "#1063F#6PHere comes the welcoming party.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1446F#2POh, Goddess...\x02\x03",

            "#1443FGrant peace to these poor, lost souls...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_881():
        OP_6D(1190, 0, -12350, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_881)

    def lambda_899():
        OP_67(0, 6150, -10000, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_899)

    def lambda_8B1():
        OP_6B(2200, 400)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8B1)

    def lambda_8C1():
        OP_6E(297, 400)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8C1)
    SetChrChipByIndex(0x11, 1)

    def lambda_8D6():
        OP_8F(0xFE, 0xFFFFFD6C, 0x0, 0xFFFFCD88, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_8D6)
    Sleep(10)
    SetChrChipByIndex(0x13, 1)

    def lambda_8FB():
        OP_8F(0xFE, 0x168, 0x0, 0xFFFFCDB0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_8FB)
    Sleep(20)
    SetChrChipByIndex(0x10, 1)

    def lambda_920():
        OP_8F(0xFE, 0xFFFFF8D0, 0x0, 0xFFFFCE32, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_920)
    Sleep(20)
    SetChrChipByIndex(0x12, 1)

    def lambda_945():
        OP_8F(0xFE, 0x514, 0x0, 0xFFFFCC98, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_945)
    WaitChrThread(0x109, 0x0)
    Battle(0xF6, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x109, -710, 0, -10400, 0)
    SetChrPos(0x10F, 750, 0, -10520, 0)
    SetChrPos(0xF0, -890, 0, -12050, 0)
    SetChrPos(0xF1, 490, 0, -12220, 0)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_6D(910, 0, -10440, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(45000, 0)
    OP_6E(292, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #14
        0x10E,
        (
            "#175FUgh... This wasn't what I wanted to find...\x02\x03",

            "#177FWhere has everyone gone?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ABE():
        TurnDirection(0xFE, 0x10E, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_ABE)

    def lambda_ACC():
        TurnDirection(0xFE, 0x10E, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_ACC)
    Sleep(50)

    def lambda_ADF():
        TurnDirection(0xFE, 0x10E, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_ADF)
    Sleep(50)
    TurnDirection(0x109, 0x10E, 400)
    Sleep(300)

    ChrTalk(    #15
        0x109,
        (
            "#1065F#5PI don't know, but we should start looking right\x01",
            "away.\x02\x03",

            "#1063FEven if no one's here, we might be able to find\x01",
            "some kind of clue as to where they are now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10E,
        (
            "#176FI can only hope so.\x02\x03",

            "#178FIn particular, we should focus our search on the\x01",
            "throne room, royal guard room, royal keep, and \x01",
            "the sealed area.\x02\x03",

            "Those seem the most likely areas to house clues.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2716)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_186 end

    def Function_3_C72(): pass

    label("Function_3_C72")

    SetChrPos(0xFE, -3370, 0, -9660, 135)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_C99():

        label("loc_C99")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_C99")

    QueueWorkItem2(0xFE, 3, lambda_C99)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)
    OP_82(0x0, 0x2)

    def lambda_CB9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CB9)
    Sleep(500)
    OP_23(0x87)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_3_C72 end

    def Function_4_CD3(): pass

    label("Function_4_CD3")

    SetChrPos(0xFE, -1450, 300, -8480, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_CFA():

        label("loc_CFA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_CFA")

    QueueWorkItem2(0xFE, 3, lambda_CFA)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)
    OP_82(0x1, 0x2)

    def lambda_D1A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D1A)
    Sleep(500)
    OP_23(0x87)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_CD3 end

    def Function_5_D34(): pass

    label("Function_5_D34")

    SetChrPos(0xFE, 2900, 0, -9580, 225)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_D5B():

        label("loc_D5B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D5B")

    QueueWorkItem2(0xFE, 3, lambda_D5B)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)
    OP_82(0x2, 0x2)

    def lambda_D7B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D7B)
    Sleep(500)
    OP_23(0x87)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_5_D34 end

    def Function_6_D95(): pass

    label("Function_6_D95")

    SetChrPos(0xFE, 830, 300, -8600, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_DBC():

        label("loc_DBC")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_DBC")

    QueueWorkItem2(0xFE, 3, lambda_DBC)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)
    OP_82(0x3, 0x2)

    def lambda_DDC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DDC)
    Sleep(500)
    OP_23(0x87)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_6_D95 end

    def Function_7_DF6(): pass

    label("Function_7_DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC5")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(1280)
    Sleep(500)
    Jump("loc_EC8")

    label("loc_EC5")

    TalkBegin(0xFF)

    label("loc_EC8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #17
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1047")

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
        (0, "loc_F60"),
        (1, "loc_FDB"),
        (2, "loc_1009"),
        (SWITCH_DEFAULT, "loc_1037"),
    )


    label("loc_F60")

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
    OP_1D(0xE6)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1044")

    label("loc_FDB")

    OP_A9(0x18)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_1044")

    label("loc_1009")

    OP_A9(0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_1044")

    label("loc_1037")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1044")

    label("loc_1044")

    Jump("loc_F04")

    label("loc_1047")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1074")
    OP_A2(0x2588)
    EventEnd(0x1)
    Jump("loc_1077")

    label("loc_1074")

    TalkEnd(0xFF)

    label("loc_1077")

    Return()

    # Function_7_DF6 end

    SaveToFile()

Try(main)
