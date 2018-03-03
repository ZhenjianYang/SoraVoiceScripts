from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M4112   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4112.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        'Celeste',                              # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT07/CH02891 ._CH',             # 00
        'ED6_DT29/CH14360 ._CH',             # 01
        'ED6_DT29/CH14360 ._CH',             # 02
        'ED6_DT29/CH14690 ._CH',             # 03
        'ED6_DT29/CH14691 ._CH',             # 04
        'ED6_DT29/CH14460 ._CH',             # 05
        'ED6_DT29/CH14461 ._CH',             # 06
        'ED6_DT29/CH14620 ._CH',             # 07
        'ED6_DT29/CH14621 ._CH',             # 08
        'ED6_DT29/CH14630 ._CH',             # 09
        'ED6_DT29/CH14631 ._CH',             # 0A
        'ED6_DT29/CH14010 ._CH',             # 0B
        'ED6_DT29/CH14011 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH02891P._CP',             # 00
        'ED6_DT29/CH14360P._CP',             # 01
        'ED6_DT29/CH14360P._CP',             # 02
        'ED6_DT29/CH14690P._CP',             # 03
        'ED6_DT29/CH14691P._CP',             # 04
        'ED6_DT29/CH14460P._CP',             # 05
        'ED6_DT29/CH14461P._CP',             # 06
        'ED6_DT29/CH14620P._CP',             # 07
        'ED6_DT29/CH14621P._CP',             # 08
        'ED6_DT29/CH14630P._CP',             # 09
        'ED6_DT29/CH14631P._CP',             # 0A
        'ED6_DT29/CH14010P._CP',             # 0B
        'ED6_DT29/CH14011P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 23080,
        Z                   = 0,
        Y                   = -20490,
        Unknown_0C          = 180,
        Unknown_0E          = 1,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x258,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15070,
        Z                   = 0,
        Y                   = 3360,
        Unknown_0C          = 180,
        Unknown_0E          = 11,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34390,
        Z                   = 30,
        Y                   = 30910,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42360,
        Z                   = -10,
        Y                   = 8320,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x259,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 33760,
        Z                   = 0,
        Y                   = -44190,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 24020,
        TriggerZ            = 500,
        TriggerY            = 54480,
        TriggerRange        = 1500,
        ActorX              = 24020,
        ActorZ              = 4000,
        ActorY              = 54480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3540,
        TriggerZ            = 500,
        TriggerY            = -67980,
        TriggerRange        = 1500,
        ActorX              = 3540,
        ActorZ              = 4000,
        ActorY              = -67980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35940,
        TriggerZ            = 0,
        TriggerY            = -43500,
        TriggerRange        = 1000,
        ActorX              = 35940,
        ActorZ              = 1000,
        ActorY              = -43500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22A",          # 00, 0
        "Function_1_27E",          # 01, 1
        "Function_2_2D3",          # 02, 2
        "Function_3_1987",         # 03, 3
        "Function_4_2122",         # 04, 4
        "Function_5_2451",         # 05, 5
        "Function_6_26ED",         # 06, 6
        "Function_7_3608",         # 07, 7
        "Function_8_3DA6",         # 08, 8
        "Function_9_40DE",         # 09, 9
        "Function_10_4389",        # 0A, 10
        "Function_11_44C2",        # 0B, 11
        "Function_12_45A9",        # 0C, 12
        "Function_13_4690",        # 0D, 13
        "Function_14_47A6",        # 0E, 14
    )


    def Function_0_22A(): pass

    label("Function_0_22A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_254")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_246"),
        (103, "loc_24D"),
        (SWITCH_DEFAULT, "loc_254"),
    )


    label("loc_246")

    Event(0, 11)
    Jump("loc_254")

    label("loc_24D")

    Event(0, 12)
    Jump("loc_254")

    label("loc_254")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_260"),
        (SWITCH_DEFAULT, "loc_268"),
    )


    label("loc_260")

    SetMapFlags(0x10000000)
    Jump("loc_268")

    label("loc_268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_27D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 10)

    label("loc_27D")

    Return()

    # Function_0_22A end

    def Function_1_27E(): pass

    label("Function_1_27E")

    OP_16(0x2, 0xFA0, 0xFFFE17B8, 0xFFFDE8D8, 0x230065)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A1")
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x8A, 0x0)

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE")
    OP_79(0x0, 0x2)
    OP_7B()

    label("loc_2AE")

    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB")
    OP_6F(0x3, 0)
    Jump("loc_2D2")

    label("loc_2CB")

    OP_6F(0x3, 60)

    label("loc_2D2")

    Return()

    # Function_1_27E end

    def Function_2_2D3(): pass

    label("Function_2_2D3")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp263_05.eff")
    LoadEffect(0x1, "map\\mp259_01.eff")
    Fade(500)
    OP_6D(24000, 250, 54700, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    SetChrPos(0x109, 23500, 0, 51000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392")
    SetChrPos(0xEF, 24540, 0, 51000, 0)
    SetChrPos(0xF0, 22920, 0, 49820, 0)
    SetChrPos(0xF1, 25000, 0, 49890, 0)
    Jump("loc_44D")

    label("loc_392")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D6")
    SetChrPos(0xF0, 24540, 0, 51000, 0)
    SetChrPos(0xEF, 22920, 0, 49820, 0)
    SetChrPos(0xF1, 25000, 0, 49890, 0)
    Jump("loc_44D")

    label("loc_3D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41A")
    SetChrPos(0xF1, 24540, 0, 51000, 0)
    SetChrPos(0xEF, 22920, 0, 49820, 0)
    SetChrPos(0xF0, 25000, 0, 49890, 0)
    Jump("loc_44D")

    label("loc_41A")

    SetChrPos(0xEF, 24540, 0, 51000, 0)
    SetChrPos(0xF0, 22920, 0, 49820, 0)
    SetChrPos(0xF1, 25000, 0, 49890, 0)

    label("loc_44D")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 28000, 800, 50660, 270)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_474():

        label("loc_474")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_474")

    QueueWorkItem2(0x10, 3, lambda_474)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        "\x07\x05The face of the monument is glowing, and words are visible upon its surface.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the monochrome schoolhouse.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the white wings among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #2
        0x109,
        (
            "#1063F#6PSo our friend's left us a message, huh?\x02\x03",

            "And I'm sure the 'white wings' mentioned here\x01",
            "must be referring to...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("Female Voice")

    AnonymousTalk(    #3
        (
            "\x07\x0CI can only assume it must be a reference\x01",
            "to my descendant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_704")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_76B")

    label("loc_704")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_76B")

    label("loc_72C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_754")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_76B")

    label("loc_754")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_76B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_798")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7FF")

    label("loc_798")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C0")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7FF")

    label("loc_7C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E8")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7FF")

    label("loc_7E8")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7FF")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82C")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_893")

    label("loc_82C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_854")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_893")

    label("loc_854")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_893")

    label("loc_87C")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_893")

    Sleep(1000)
    Fade(500)
    OP_6D(27000, 0, 52130, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(2890, 0)
    OP_6C(44000, 0)
    OP_6E(268, 0)
    SetChrPos(0x109, 23500, 0, 51400, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F")
    SetChrPos(0xEF, 24870, 0, 51190, 0)
    SetChrPos(0xF0, 23070, 0, 49780, 0)
    SetChrPos(0xF1, 24930, 0, 49800, 0)
    Jump("loc_9EA")

    label("loc_92F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_973")
    SetChrPos(0xF0, 24870, 0, 51190, 0)
    SetChrPos(0xEF, 23000, 0, 49780, 0)
    SetChrPos(0xF1, 24930, 0, 49800, 0)
    Jump("loc_9EA")

    label("loc_973")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B7")
    SetChrPos(0xF1, 24870, 0, 51190, 0)
    SetChrPos(0xEF, 23070, 0, 49780, 0)
    SetChrPos(0xF0, 24930, 0, 49800, 0)
    Jump("loc_9EA")

    label("loc_9B7")

    SetChrPos(0xEF, 24870, 0, 51190, 0)
    SetChrPos(0xF0, 23070, 0, 49780, 0)
    SetChrPos(0xF1, 24930, 0, 49800, 0)

    label("loc_9EA")

    OP_0D()
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x10, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_A30():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A30)
    Sleep(100)

    def lambda_A43():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_A43)
    Sleep(100)

    def lambda_A56():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_A56)
    Sleep(100)
    OP_8C(0xF0, 90, 400)
    Sleep(500)
    OP_22(0x99, 0x0, 0x64)

    def lambda_A7A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xB4, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A7A)
    PlayEffect(0x1, 0x7, 0x10, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x10, 0x1)
    OP_82(0x0, 0x2)
    Sleep(1000)

    ChrTalk(    #4
        0x109,
        "#1064F#6PYou're here!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B0B")

    ChrTalk(    #5
        0x105,
        "#1164F#6PCeleste...?\x02",
    )

    CloseMessageWindow()

    label("loc_B0B")


    ChrTalk(    #6
        0x10,
        (
            "\x07\x0C#1611F#11PHeehee... There's no need to be alarmed. This is only\x01",
            "a shadow of myself that I created to talk to you here.\x02\x03",

            "Technically, I'm still in the garden.\x02\x03",

            "#1616FBut now that I finally have some of my strength back,\x01",
            "I've gained a few new tricks like this one up my sleeve,\x01",
            "so to speak.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1078F#6PW-Well...that's cool.\x02\x03",

            "#1063FAnyway, am I right in guessing we'll need to use\x01",
            "this monument to proceed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "\x07\x0C#1615F#11PYou are, indeed. It appears to be a kind of gate\x01",
            "connecting this area and another realm created\x01",
            "by the Lord of Phantasma.\x02\x03",

            "#1612FHowever, in order to activate it, you will need to\x01",
            "have a certain member of your team with you.\x02\x03",

            "No doubt they work in a similar way to the doors\x01",
            "scattered throughout Phantasma.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E71")

    ChrTalk(    #9
        0x109,
        "#1063F#6PMakes sense...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x105,
        (
            "#1162F#6PSo in this case, the gate will only open\x01",
            "if I'm on the front lines?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EDB")

    label("loc_E71")


    ChrTalk(    #11
        0x109,
        (
            "#1065F#6PMakes sense...\x02\x03",

            "#1063FSo in this case, we're going to need to\x01",
            "have Princess Klaudia, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EDB")


    ChrTalk(    #12
        0x10,
        (
            "\x07\x0C#1616FI'd say so, yes.\x02\x03",

            "#1610FThe other monuments in this area will likely also\x01",
            "serve as gates to other areas, requiring different\x01",
            "team members...\x02\x03",

            "...but as it stands, none of the others are active.\x01",
            "I presume you'll need to travel through this gate\x01",
            "and finish the area beyond it first.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_102E")

    ChrTalk(    #13
        0x105,
        "#1383F#6PUnderstood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1060")

    label("loc_102E")


    ChrTalk(    #14
        0x109,
        "#1060F#6PGot it. We'll work our way through.\x02",
    )

    CloseMessageWindow()

    label("loc_1060")


    ChrTalk(    #15
        0x10,
        (
            "\x07\x0C#1616F#11PWell, I wish you the best of luck.\x02\x03",

            "#1611FShould you require my aid, I will be in the garden.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x10, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0x99, 0x0, 0x64)

    def lambda_1120():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1120)
    OP_82(0x7, 0x2)
    OP_82(0x0, 0x2)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    Sleep(1500)

    def lambda_1147():
        OP_6D(25500, 0, 52040, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1147)

    def lambda_115F():
        OP_67(0, 7100, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_115F)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C0")

    def lambda_1185():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1185)

    def lambda_1193():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1193)

    def lambda_11A1():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_11A1)
    OP_8C(0x105, 270, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #16
        0x105,
        (
            "#1383F#11PI'm ready to proceed when everyone else is.\x02\x03",

            "#1162FJust say the word as soon as you're ready to\x01",
            "move on, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        (
            "#1075F#6PWill do.\x02\x03",

            "#1078FI want to double check our equipment before\x01",
            "we get a move on, though. Everyone cool with\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B04)
    Jump("loc_1970")

    label("loc_12C0")


    def lambda_12C6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_12C6)
    Sleep(50)

    def lambda_12D9():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_12D9)
    Sleep(50)

    def lambda_12EC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_12EC)
    Sleep(50)
    OP_8C(0xF1, 315, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #18
        0x109,
        (
            "#1075F#5POkay...\x02\x03",

            "#1060FTime to head back to the garden, then, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E2")

    ChrTalk(    #19
        0x10F,
        (
            "#1443FIndeed. I'm sure as long as we explain\x01",
            "the situation to the princess, she'll be\x01",
            "more than happy to support us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_13E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1437")

    ChrTalk(    #20
        0x101,
        (
            "#1006FYep! We need to explain what's going on\x01",
            "to Kloe a.s.a.p.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_1437")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1488")

    ChrTalk(    #21
        0x102,
        (
            "#1500FYeah. We'll need to explain what's going\x01",
            "on to Kloe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_1488")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DE")

    ChrTalk(    #22
        0x10B,
        (
            "#210FYeah. We've gotta explain what's going\x01",
            "on to the princess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_14DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154F")

    ChrTalk(    #23
        0x110,
        (
            "#261FMm-hmm. And hopefully, it won't take much\x01",
            "to persuade our fair princess to come with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_154F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B8")

    ChrTalk(    #24
        0x107,
        (
            "#560FYep! We need to explain what's going on to\x01",
            "Kloe and hope she'll come with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_15B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162A")

    ChrTalk(    #25
        0x10A,
        (
            "#1310FYep! We need to explain what's going on to\x01",
            "the princess and hope she'll come with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_162A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169F")

    ChrTalk(    #26
        0x103,
        (
            "#1527FYeah. We'll need to explain what's going on to\x01",
            "the princess and ask her to come with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_169F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1714")

    ChrTalk(    #27
        0x106,
        (
            "#051FYeah. We're gonna need to break down what's\x01",
            "going on to Kloe and see if she'll come with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_1714")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1788")

    ChrTalk(    #28
        0x108,
        (
            "#070FYeah. We'll need to explain what's going on to\x01",
            "the princess and ask her to come with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_1788")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F7")

    ChrTalk(    #29
        0x10E,
        (
            "#176FIndeed. We will need to explain the situation to\x01",
            "Her Highness and seek her support.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_17F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1871")

    ChrTalk(    #30
        0x104,
        (
            "#1540FIndeed. And I'm certain Kloe will be more than\x01",
            "happy to aid us once we explain the situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_1871")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F2")

    ChrTalk(    #31
        0x10D,
        (
            "#277FIndeed. And I'm certain Her Highness will be\x01",
            "more than happy to aid us once we explain the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_18F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1970")

    ChrTalk(    #32
        0x10C,
        (
            "#115FIndeed. And I'm certain Her Highness will be\x01",
            "more than happy to aid us once we explain the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1970")

    OP_A2(0x2B03)
    OP_28(0x37, 0x1, 0x4)
    OP_28(0x37, 0x1, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_2D3 end

    def Function_3_1987(): pass

    label("Function_3_1987")

    EventBegin(0x0)
    Fade(500)
    OP_6D(24000, 250, 54700, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    SetChrPos(0x109, 24010, 0, 51600, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A20")
    SetChrPos(0xEF, 24000, 480, 53280, 0)
    SetChrPos(0xF0, 23250, 0, 50400, 0)
    SetChrPos(0xF1, 24860, 0, 50220, 0)
    Jump("loc_1AA5")

    label("loc_1A20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A64")
    SetChrPos(0xF0, 24000, 480, 53280, 0)
    SetChrPos(0xEF, 23250, 0, 50400, 0)
    SetChrPos(0xF1, 24860, 0, 50220, 0)
    Jump("loc_1AA5")

    label("loc_1A64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA5")
    SetChrPos(0xF1, 24000, 480, 53280, 0)
    SetChrPos(0xEF, 23250, 0, 50400, 0)
    SetChrPos(0xF0, 24860, 0, 50220, 0)

    label("loc_1AA5")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #33
        (
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the monochrome schoolhouse.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the white wings among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC3")
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #34
        0x105,
        "#1162F#6P...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    label("loc_1BC3")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_211F")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Touch the Monument\x01",      # 0
            "Step Away\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C2F"),
        (SWITCH_DEFAULT, "loc_210A"),
    )


    label("loc_1C2F")

    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x8B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA7")

    def lambda_1C95():
        OP_6D(24000, 10250, 54700, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1C95)

    label("loc_1CA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E0B")
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1CFA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1CFA)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1D50():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D50)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1DA6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1DA6)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1DFC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1DFC)
    Jump("loc_20D0")

    label("loc_1E0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F6F")
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1E5E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1E5E)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1EB4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1EB4)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1F0A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1F0A)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1F60():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1F60)
    Jump("loc_20D0")

    label("loc_1F6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D0")
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1FC2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1FC2)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_2018():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2018)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_206E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_206E)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_20C4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_20C4)

    label("loc_20D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E0")
    Sleep(1500)
    Jump("loc_20E5")

    label("loc_20E0")

    Sleep(500)

    label("loc_20E5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x3)
    NewScene("ED6_DT21/U2500   ._SN", 130, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_211C")

    label("loc_210A")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_211C")

    label("loc_211C")

    Jump("loc_1BD6")

    label("loc_211F")

    EventEnd(0x0)
    Return()

    # Function_3_1987 end

    def Function_4_2122(): pass

    label("Function_4_2122")

    EventBegin(0x0)
    Fade(500)
    OP_6D(24000, 250, 54700, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    SetChrPos(0x0, 24000, 480, 53280, 0)
    SetChrPos(0x1, 24010, 0, 51600, 0)
    SetChrPos(0x2, 23250, 0, 50400, 0)
    SetChrPos(0x3, 24860, 0, 50220, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #35
        "\x07\x05The front of the monument is glowing.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_220F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_244E")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Touch the Monument\x01",      # 0
            "Step Away\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2268"),
        (SWITCH_DEFAULT, "loc_2439"),
    )


    label("loc_2268")

    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x8B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_2305():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2305)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_235B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_235B)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_23B1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_23B1)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_2407():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2407)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/U2500   ._SN", 130, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_244B")

    label("loc_2439")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_244B")

    label("loc_244B")

    Jump("loc_220F")

    label("loc_244E")

    EventEnd(0x0)
    Return()

    # Function_4_2122 end

    def Function_5_2451(): pass

    label("Function_5_2451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_2460")
    Call(0, 4)
    Return()

    label("loc_2460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_END)), "loc_257A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_247D")
    Call(0, 3)
    Return()

    label("loc_247D")

    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #36
        (
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the monochrome schoolhouse.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the white wings among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_26EC")

    label("loc_257A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2683")
    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #37
        (
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the monochrome schoolhouse.\x01",
            "#500W \x01",
            "#40W       Place your hand on this monument,\x01",
            "the white wings among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_26EC")

    label("loc_2683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2693")
    Call(0, 2)
    Return()

    label("loc_2693")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #38
        "\x07\x05Nothing is written on the sapphirl monument.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_26EC")

    Return()

    # Function_5_2451 end

    def Function_6_26ED(): pass

    label("Function_6_26ED")

    EventBegin(0x0)
    Fade(500)
    OP_6D(4300, 480, -68030, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(269000, 0)
    OP_6E(354, 0)
    SetChrPos(0x109, 6730, 0, -68020, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2786")
    SetChrPos(0xEF, 7950, 0, -68780, 270)
    SetChrPos(0xF0, 7900, 0, -67230, 270)
    SetChrPos(0xF1, 9000, 0, -67960, 270)
    Jump("loc_2841")

    label("loc_2786")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27CA")
    SetChrPos(0xF0, 7950, 0, -68780, 270)
    SetChrPos(0xEF, 7900, 0, -67230, 270)
    SetChrPos(0xF1, 9000, 0, -67960, 270)
    Jump("loc_2841")

    label("loc_27CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_280E")
    SetChrPos(0xF1, 7950, 0, -68780, 270)
    SetChrPos(0xEF, 7900, 0, -67230, 270)
    SetChrPos(0xF0, 9000, 0, -67960, 270)
    Jump("loc_2841")

    label("loc_280E")

    SetChrPos(0xEF, 7950, 0, -68780, 270)
    SetChrPos(0xF0, 7900, 0, -67230, 270)
    SetChrPos(0xF1, 9000, 0, -67960, 270)

    label("loc_2841")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #39
        "\x07\x05The face of the monument is glowing, and words are visible upon its surface.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #40
        (
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the impregnable fortress.\x01",
            "#500W \x01",
            "#40W    Place your hand on this monument,\x01",
            "the Divine Blade's successor among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B5D")
    OP_A2(0x2B17)

    ChrTalk(    #41
        0x109,
        "#1079F#6PGreat...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #42
        0x109,
        (
            "#1060F#5PDon't have a clue what 'impregnable fortress'\x01",
            "could be referring to, but I think we all know\x01",
            "who we're gonna need to have with us this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10C,
        (
            "#113F#6PB-But...\x02\x03",

            "#115F...I suppose there's no point in debating if I am\x01",
            "fit to be called his successor. No one else seems\x01",
            "to match the description, after all.\x02\x03",

            "#110FI'd like to try touching it, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35F1")

    label("loc_2B5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3111")

    ChrTalk(    #44
        0x109,
        "#1079F#6PGreat...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #45
        0x109,
        (
            "#1060F#5PDon't have a clue what 'impregnable fortress'\x01",
            "could be referring to, but I think we all know\x01",
            "who we're gonna need to have with us this time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D32")

    ChrTalk(    #46
        0x10E,
        (
            "#179F#6PIt's very obvious, yes.\x02\x03",

            "#170FI've received some training from Brigadier General\x01",
            "Bright in the past, but Richard is the only one who\x01",
            "could truly count as his successor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300A")

    label("loc_2D32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D88")
    OP_A2(0x0)

    ChrTalk(    #47
        0x10A,
        (
            "#816F#6PYep.\x02\x03",

            "No one else but Richard fits that description.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300A")

    label("loc_2D88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E0D")
    OP_A2(0x1)

    ChrTalk(    #48
        0x101,
        (
            "#1012F#6PYeah.\x02\x03",

            "#1006FI can't really think of anyone other than \x01",
            "Colonel Richard who fits that description.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300A")

    label("loc_2E0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E8A")
    OP_A2(0x2)

    ChrTalk(    #49
        0x102,
        (
            "#1505F#6PYeah.\x02\x03",

            "#1500FI can't really think of anyone other than \x01",
            "Richard who fits that description.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300A")

    label("loc_2E8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F4B")

    ChrTalk(    #50
        0x103,
        (
            "#1526F#6PYeah.\x02\x03",

            "#1520FI've been taught by Cassius in the past, but as\x01",
            "far as swordsmanship goes, Colonel Richard is the\x01",
            "only one who could really be called his successor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300A")

    label("loc_2F4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FAC")

    ChrTalk(    #51
        0x106,
        (
            "#053F#6PYeah.\x02\x03",

            "#051FThe colonel's the only one who fits the bill, \x01",
            "really.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300A")

    label("loc_2FAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_300A")

    ChrTalk(    #52
        0x108,
        (
            "#573F#6PYeah.\x02\x03",

            "#070FThe colonel's the only one who fits the bill, \x01",
            "really.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_300A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3095")

    ChrTalk(    #53
        0x109,
        (
            "#1075F#5PGlad to see we're on the same page.\x02\x03",

            "#1078FThen let's head back to the garden and ask\x01",
            "him to come with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310E")

    label("loc_3095")


    ChrTalk(    #54
        0x109,
        (
            "#1075F#5PGlad to see we're on the same page.\x02\x03",

            "#1078FThen let's head back to the garden and ask\x01",
            "him to come with us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310E")

    Jump("loc_33DE")

    label("loc_3111")


    ChrTalk(    #55
        0x109,
        "#1079F#6PGreat...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #56
        0x109,
        (
            "#1060F#5PDon't have a clue what 'impregnable fortress'\x01",
            "could be referring to, but I think we all know\x01",
            "who we're gonna need to have with us this time.\x02\x03",

            "My mira's on Richard.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_326E")

    ChrTalk(    #57
        0x10F,
        (
            "#1446F#6PWell, if you're certain.\x02\x03",

            "#1448FIn that case, shall we return to the garden\x01",
            "and ask him to come with us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33DE")

    label("loc_326E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32F6")

    ChrTalk(    #58
        0x105,
        (
            "#1383F#6PThat does make sense...\x02\x03",

            "#1382FIn that case, we should return to the garden\x01",
            "and ask him to come with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33DE")

    label("loc_32F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_336C")

    ChrTalk(    #59
        0x10B,
        (
            "#210F#6POh, really?\x02\x03",

            "#211FWell, we'd better get back to the garden\x01",
            "and ask him to come with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33DE")

    label("loc_336C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33DE")

    ChrTalk(    #60
        0x104,
        (
            "#1541F#6PMakes sense.\x02\x03",

            "#1540FWe should return to the garden and ask him\x01",
            "to come with us, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35F1")

    ChrTalk(    #61
        0x110,
        (
            "#263F#6PHeehee.\x02\x03",

            "#1306FWith him, we'll have a regular onion and\x01",
            "a spring onion in the same party.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #62
        0x109,
        (
            "#1064F#5PAnd what did I do to you to deserve that cruel\x01",
            "observation on my awesome hair?\x02\x03",

            "#1068FI don't even style my hair like this on purpose,\x01",
            "y'know! It just fwoops up this way naturally.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3565")

    ChrTalk(    #63
        0x101,
        "#1016F#6PWh-Whatever you say...\x02",
    )

    CloseMessageWindow()

    label("loc_3565")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35A1")

    ChrTalk(    #64
        0x10F,
        "#1806F#6PHeehee. He's not lying, either.\x02",
    )

    CloseMessageWindow()

    label("loc_35A1")


    ChrTalk(    #65
        0x110,
        (
            "#261F#6POh, really?\x02\x03",

            "#265FI wonder if the same can be said of the colonel?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F1")

    OP_A2(0x2B16)
    OP_28(0x39, 0x1, 0x2)
    OP_28(0x39, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_6_26ED end

    def Function_7_3608(): pass

    label("Function_7_3608")

    EventBegin(0x0)
    Fade(500)
    OP_6D(2670, 250, -68000, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(269000, 0)
    OP_6E(311, 0)
    SetChrPos(0x109, 6520, 0, -68050, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A1")
    SetChrPos(0xEF, 4750, 480, -68000, 270)
    SetChrPos(0xF0, 7840, 0, -68700, 270)
    SetChrPos(0xF1, 7910, 0, -67330, 270)
    Jump("loc_3726")

    label("loc_36A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E5")
    SetChrPos(0xF0, 4750, 480, -68000, 270)
    SetChrPos(0xEF, 7840, 0, -68700, 270)
    SetChrPos(0xF1, 7910, 0, -67330, 270)
    Jump("loc_3726")

    label("loc_36E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3726")
    SetChrPos(0xF1, 4750, 480, -68000, 270)
    SetChrPos(0xEF, 7840, 0, -68700, 270)
    SetChrPos(0xF0, 7910, 0, -67330, 270)

    label("loc_3726")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #66
        (
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the impregnable fortress.\x01",
            "#500W \x01",
            "#40W    Place your hand on this monument,\x01",
            "the Divine Blade's successor among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384B")
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #67
        0x10C,
        "#112F#6P...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    label("loc_384B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_385E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DA3")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Touch the Monument\x01",      # 0
            "Step Away\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_38B7"),
        (SWITCH_DEFAULT, "loc_3D8E"),
    )


    label("loc_38B7")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_392F")

    def lambda_391D():
        OP_6D(2670, 10000, -68000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_391D)

    label("loc_392F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A93")
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3982():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3982)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_39D8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_39D8)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3A2E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3A2E)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3A84():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3A84)
    Jump("loc_3D58")

    label("loc_3A93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BF7")
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3AE6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3AE6)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3B3C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3B3C)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3B92():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3B92)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3BE8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3BE8)
    Jump("loc_3D58")

    label("loc_3BF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D58")
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3C4A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3C4A)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3CA0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3CA0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3CF6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3CF6)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3D4C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3D4C)

    label("loc_3D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D68")
    Sleep(1500)
    Jump("loc_3D6D")

    label("loc_3D68")

    Sleep(500)

    label("loc_3D6D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M3100   ._SN", 103, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DA0")

    label("loc_3D8E")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DA0")

    label("loc_3DA0")

    Jump("loc_385E")

    label("loc_3DA3")

    EventEnd(0x0)
    Return()

    # Function_7_3608 end

    def Function_8_3DA6(): pass

    label("Function_8_3DA6")

    EventBegin(0x0)
    Fade(500)
    OP_6D(3970, 250, -67060, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2630, 0)
    OP_6C(314000, 0)
    OP_6E(310, 0)
    SetChrPos(0x0, 4940, 490, -68160, 270)
    SetChrPos(0x1, 6400, 0, -68310, 270)
    SetChrPos(0x2, 7810, 0, -69300, 270)
    SetChrPos(0x3, 7950, 0, -67840, 270)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #68
        "\x07\x05The front of the monument is glowing.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40DB")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Touch the Monument\x01",      # 0
            "Step Away\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3EF5"),
        (SWITCH_DEFAULT, "loc_40C6"),
    )


    label("loc_3EF5")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3F92():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3F92)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3FE8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3FE8)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_403E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_403E)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_4094():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4094)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M3100   ._SN", 103, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40D8")

    label("loc_40C6")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40D8")

    label("loc_40D8")

    Jump("loc_3E9C")

    label("loc_40DB")

    EventEnd(0x0)
    Return()

    # Function_8_3DA6 end

    def Function_9_40DE(): pass

    label("Function_9_40DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_40ED")
    Call(0, 8)
    Return()

    label("loc_40ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_END)), "loc_420F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_410A")
    Call(0, 7)
    Return()

    label("loc_410A")

    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #69
        (
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the impregnable fortress.\x01",
            "#500W \x01",
            "#40W    Place your hand on this monument,\x01",
            "the Divine Blade's successor among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_4388")

    label("loc_420F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4320")
    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #70
        (
            "\x07\x02#40WThe Lord of Phantasma does decree...\x01",
            "#500W \x01",
            "#40W Here lies the impregnable fortress.\x01",
            "#500W \x01",
            "#40W    Place your hand on this monument,\x01",
            "the Divine Blade's successor among your number.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_4388")

    label("loc_4320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_432F")
    Call(0, 6)
    Return()

    label("loc_432F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #71
        "\x07\x05Nothing is written on the carnelia monument.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_4388")

    Return()

    # Function_9_40DE end

    def Function_10_4389(): pass

    label("Function_10_4389")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(4740, 5300, -68000, 0)
    OP_67(0, 7100, -10000, 0)
    OP_6B(2310, 0)
    OP_6C(269000, 0)
    OP_6E(356, 0)

    def lambda_43EC():
        OP_6D(4000, 1750, -68000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_43EC)

    def lambda_4404():
        OP_67(0, 5320, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4404)

    def lambda_441C():
        OP_6B(2390, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_441C)

    def lambda_442C():
        OP_6E(359, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_442C)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    def lambda_4450():
        OP_6B(2000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4450)
    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    OP_72(0x401, 0x0)
    ExitThread()
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    OP_0D()
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5600   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_4389 end

    def Function_11_44C2(): pass

    label("Function_11_44C2")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 24070, 0, 51210, 180)
    SetChrPos(0x1, 24070, 0, 51210, 180)
    SetChrPos(0x2, 24070, 0, 51210, 180)
    SetChrPos(0x3, 24070, 0, 51210, 180)
    OP_69(0x0, 0x0)
    OP_6C(315000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 13)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_11_44C2 end

    def Function_12_45A9(): pass

    label("Function_12_45A9")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 6690, 0, -68020, 90)
    SetChrPos(0x1, 6690, 0, -68020, 90)
    SetChrPos(0x2, 6690, 0, -68020, 90)
    SetChrPos(0x3, 6690, 0, -68020, 90)
    OP_69(0x0, 0x0)
    OP_6C(315000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 13)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_12_45A9 end

    def Function_13_4690(): pass

    label("Function_13_4690")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46B9")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_46AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_46AD)

    label("loc_46B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46E2")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_46D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_46D6)

    label("loc_46E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_470B")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_46FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_46FF)

    label("loc_470B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4734")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4728():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4728)

    label("loc_4734")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4760")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4760")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4777")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4777")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_478E")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_478E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47A5")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_47A5")

    Return()

    # Function_13_4690 end

    def Function_14_47A6(): pass

    label("Function_14_47A6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29D, 1)"), scpexpr(EXPR_END)), "loc_4814")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #72
        "\x07\x05Found \x1F\x9D\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B9E)
    Jump("loc_487C")

    label("loc_4814")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #73
        (
            "\x07\x05Found \x1F\x9D\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x9D\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_487C")

    Jump("loc_48E0")

    label("loc_487F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #74
        "\x07\x05I don't see your name on that item, so why are you taking it?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x3C, 0x0)

    label("loc_48E0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_47A6 end

    SaveToFile()

Try(main)
