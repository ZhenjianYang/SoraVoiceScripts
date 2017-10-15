from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4153   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4153.x',
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
        'Kloe',                                 # 9
        'Tita',                                 # 10
        'Renne',                                # 11
        'Royal Army Soldier',                   # 12
        'Royal Army Soldier',                   # 13
        'Grancel - West Block',                 # 14
        'Grancel Castle',                       # 15
        'Grancel - East Block',                 # 16
        'Grancel - South Block',                # 17
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
        'ED6_DT07/CH00040 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT27/CH03510 ._CH',             # 02
        'ED6_DT07/CH01640 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH00040P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT27/CH03510P._CP',             # 02
        'ED6_DT07/CH01640P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        X                   = -6050,
        Z                   = 0,
        Y                   = 69190,
        Direction           = 190,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 6050,
        Z                   = 0,
        Y                   = 69190,
        Direction           = 190,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -40080,
        Z                   = 0,
        Y                   = 17660,
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
        X                   = 100,
        Z                   = 0,
        Y                   = 104130,
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
        X                   = 40430,
        Z                   = 0,
        Y                   = 64060,
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
        X                   = 20,
        Z                   = 0,
        Y                   = -3500,
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


    DeclEvent(
        X                   = 18520,
        Y                   = 0,
        Z                   = 44050,
        Range               = 1500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 9,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_227",          # 01, 1
        "Function_2_24E",          # 02, 2
        "Function_3_29F",          # 03, 3
        "Function_4_32D",          # 04, 4
        "Function_5_397",          # 05, 5
        "Function_6_E29",          # 06, 6
        "Function_7_EC1",          # 07, 7
        "Function_8_11CC",         # 08, 8
        "Function_9_14DB",         # 09, 9
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_226")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_226")

    Return()

    # Function_0_20A end

    def Function_1_227(): pass

    label("Function_1_227")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFECF50, 0x23005E)
    OP_1B(0x6, 0x0, 0x7)
    OP_1B(0x7, 0x0, 0x8)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Return()

    # Function_1_227 end

    def Function_2_24E(): pass

    label("Function_2_24E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_273")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_289")

    label("loc_273")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289")
    OP_99(0xFE, 0x1, 0x7, 0x640)

    label("loc_289")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_289")

    label("loc_29E")

    Return()

    # Function_2_24E end

    def Function_3_29F(): pass

    label("Function_3_29F")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xB,
        (
            "Due to heightened security, we've\x01",
            "had to close this area.\x02\x03",

            "No matter who you are, I'm afraid\x01",
            "I can't allow you to go any farther.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_29F end

    def Function_4_32D(): pass

    label("Function_4_32D")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xC,
        (
            "I won't let a single person through.\x02\x03",

            "I've received orders to let no one\x01",
            "near Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_32D end

    def Function_5_397(): pass

    label("Function_5_397")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AA")
    Call(0, 6)

    label("loc_3AA")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 5380, 0, 35040, 360)
    SetChrPos(0x101, 6180, 0, 34540, 360)
    SetChrPos(0xF7, 4690, 0, 34460, 360)
    SetChrPos(0x9, 6190, 0, 33520, 360)
    SetChrPos(0xA, 4770, 0, 33300, 360)
    OP_6D(6190, 250, 68540, 0)
    OP_67(0, 10150, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(56000, 0)
    OP_6E(403, 0)

    def lambda_451():
        OP_6D(9330, 250, 47830, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_451)
    FadeToBright(1000, 0)
    Sleep(2000)

    def lambda_477():
        OP_8E(0xFE, 0x1504, 0x0, 0xB3D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_477)
    Sleep(300)

    def lambda_497():
        OP_8E(0xFE, 0x17E8, 0x0, 0xAE1A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_497)
    Sleep(50)

    def lambda_4B7():
        OP_8E(0xFE, 0x134C, 0x0, 0xAE38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4B7)
    Sleep(100)

    def lambda_4D7():
        OP_8E(0xFE, 0x1824, 0x0, 0xAA00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4D7)
    Sleep(50)

    def lambda_4F7():
        OP_8E(0xFE, 0x136A, 0x0, 0xA924, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4F7)
    WaitChrThread(0xA, 0x1)
    OP_8C(0x8, 180, 400)
    Fade(1000)
    OP_6D(5550, 0, 44780, 0)
    OP_67(0, 8070, -10000, 0)
    OP_6B(4059, 0)
    OP_6C(45000, 0)
    OP_6E(180, 0)
    OP_0D()

    ChrTalk(    #2
        0x101,
        (
            "#1006FOkay, let's split up here, then.\x02\x03",

            "Kloe, be careful on your way home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#048F#6PHaha. It's not that far.\x01",
            "I think I'll be fine in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        "#264FHuh? Miss Kloe, you live in Grancel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#045F#6PUm, yes, I do. I'll be staying at\x01",
            "my grandmother's house.\x02\x03",

            "#040FWell, if you'll pardon me...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6BD")

    ChrTalk(    #6
        0x106,
        "#051F#6PYeah, see ya tomorrow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E3")

    label("loc_6BD")


    ChrTalk(    #7
        0x103,
        "#021F#6PHave a good night, Kloe.\x02",
    )

    CloseMessageWindow()

    label("loc_6E3")


    ChrTalk(    #8
        0x9,
        "#061F#4PGood night, Kloe!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_70F():
        OP_6D(5630, 0, 47820, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_70F)
    OP_8E(0x8, 0x14FA, 0x0, 0xE59C, 0x9C4, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_6D(6030, 0, 44520, 1800)
    OP_8C(0x101, 225, 400)

    ChrTalk(    #9
        0x101,
        (
            "#1016FWow... That was one heck of a party.\x02\x03",

            "Olivier even dragged poor\x01",
            "Mueller into it!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 90, 400)
    OP_8C(0xA, 45, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_80B")

    ChrTalk(    #10
        0x106,
        (
            "#051F#6PYeah, well, you called up that\x01",
            "reporter, too, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_871")

    label("loc_80B")


    ChrTalk(    #11
        0x103,
        (
            "#027F#6PAnd who was it that dragged poor Mr. Burns\x01",
            "into it all, hmm? Not that he seemed to mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_871")


    ChrTalk(    #12
        0x101,
        (
            "#1008FHaha... Well, I figured, what the heck!\x02\x03",

            "Renne, did you have fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "#261FHeehee! Yeah, yeah, I did!\x02\x03",

            "The food was good and everyone\x01",
            "was talking about neat stuff!\x02\x03",

            "The piano music was really pretty, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x9,
        (
            "#061F#4PYeah! Olivier is really good at it.\x02\x03",

            "I was kinda surprised.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B2C")

    ChrTalk(    #15
        0x101,
        (
            "#1016FWell, he's not all hot air when he\x01",
            "calls himself a traveling performer,\x01",
            "I guess.\x02\x03",

            "#1006FSure you want to duck out\x01",
            "already, Agate?\x02\x03",

            "Zin and the others are still\x01",
            "having a lot of fun.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #16
        0x106,
        (
            "#053F#6PYeah... Honestly, if I tried keeping\x01",
            "up with Zin, I might not have a\x01",
            "liver in the morning.\x02\x03",

            "#051FPlus, I'm kinda beat from trollin'\x01",
            "the city all over today, so I'm\x01",
            "just gonna pack it in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAB")

    label("loc_B2C")


    ChrTalk(    #17
        0x101,
        (
            "#1016FWell, he's not all hot air when he\x01",
            "calls himself a traveling performer,\x01",
            "I guess.\x02\x03",

            "#1006FSure you want to duck out\x01",
            "already, Schera?\x02\x03",

            "Zin and the others are still\x01",
            "having a lot of fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x103,
        (
            "#027F#6PProfessional courtesy, Estelle.\x01",
            "If I stayed, you know I'd just drink\x01",
            "them under the table.\x02\x03",

            "Since we DO have work tomorrow,\x01",
            "I thought I'd cut out early and spare\x01",
            "them the pain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAB")


    ChrTalk(    #19
        0x101,
        (
            "#1006FFair enough!\x02\x03",

            "Let's go get our hotel rooms, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    def lambda_CF5():
        OP_8E(0xFE, 0x4858, 0x2EE, 0xAC12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CF5)
    Sleep(500)
    OP_8C(0x9, 90, 400)

    def lambda_D1C():
        OP_8E(0xFE, 0x4330, 0x190, 0xADAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D1C)
    Sleep(200)
    OP_8C(0xA, 90, 400)

    def lambda_D43():
        OP_8E(0xFE, 0x4358, 0x19A, 0xAA1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D43)
    Sleep(500)

    def lambda_D63():
        OP_8E(0xFE, 0x3E1C, 0xFA, 0xABFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_D63)
    OP_6D(18520, 750, 44050, 4000)
    WaitChrThread(0x101, 0x1)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    Sleep(1000)

    def lambda_DA7():
        OP_8E(0xFE, 0x4FF6, 0x2EE, 0xAC12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA7)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_DD1():
        OP_8E(0xFE, 0x4FF6, 0x2EE, 0xAC12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_DD1)
    Sleep(500)

    def lambda_DF1():
        OP_8E(0xFE, 0x4FF6, 0x2EE, 0xAC12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_DF1)
    WaitChrThread(0x101, 0x1)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x101, 0x80)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_397 end

    def Function_6_E29(): pass

    label("Function_6_E29")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EA2"),
        (1, "loc_EA8"),
        (SWITCH_DEFAULT, "loc_EAE"),
    )


    label("loc_EA2")

    OP_A2(0x1200)
    Jump("loc_EAE")

    label("loc_EA8")

    OP_A2(0x1201)
    Jump("loc_EAE")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_EBC")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_EC0")

    label("loc_EBC")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_EC0")

    Return()

    # Function_6_E29 end

    def Function_7_EC1(): pass

    label("Function_7_EC1")

    EventBegin(0x1)
    OP_4A(0xB, 255)
    OP_8C(0xB, 90, 400)

    ChrTalk(    #20
        0xB,
        (
            "Sorry, I'm going to have to ask you\x01",
            "to refrain from going any farther.\x02\x03",

            "Due to heightened security, we've had\x01",
            "to close this area.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_10BE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7A")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_F81")

    label("loc_F7A")

    TurnDirection(0x103, 0x0, 400)

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF1")

    ChrTalk(    #21
        0x103,
        (
            "#022F(I think we can leave Grancel\x01",
            "Castle to the Royal Army.)\x02\x03",

            "(Let's hurry to the west block.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1052")

    label("loc_FF1")


    ChrTalk(    #22
        0x103,
        (
            "#022F(I think we can leave Grancel\x01",
            "Castle to the Royal Army.)\x02\x03",

            "(Let's hurry to the harbor.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1052")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1086")

    ChrTalk(    #23
        0x101,
        "#1002F(Yeah, all right.)\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()
    Jump("loc_10B8")

    label("loc_1086")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B8")

    ChrTalk(    #24
        0x109,
        "#1063F(Yeah, absolutely.)\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()

    label("loc_10B8")

    OP_A2(0x0)
    Jump("loc_11A5")

    label("loc_10BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D4")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_10DB")

    label("loc_10D4")

    TurnDirection(0x106, 0x0, 400)

    label("loc_10DB")


    ChrTalk(    #25
        0x106,
        (
            "#050F(I think we can leave Grancel\x01",
            "Castle to the Royal Army.)\x02\x03",

            "(Let's hurry to the harbor.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1170")

    ChrTalk(    #26
        0x101,
        "#1002F(Yeah, all right.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x103, 400)
    Jump("loc_11A2")

    label("loc_1170")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A2")

    ChrTalk(    #27
        0x109,
        "#1063F(Yeah, absolutely.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x103, 400)

    label("loc_11A2")

    OP_A2(0x0)

    label("loc_11A5")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8C(0xB, 180, 0)
    OP_4B(0xB, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_7_EC1 end

    def Function_8_11CC(): pass

    label("Function_8_11CC")

    EventBegin(0x1)
    OP_4A(0xC, 255)
    OP_8C(0xC, 270, 400)

    ChrTalk(    #28
        0xC,
        (
            "Sorry, I'm going to have to ask you\x01",
            "to refrain from going any farther.\x02\x03",

            "Due to heightened security, we've\x01",
            "had to close this area.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13CD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1285")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_128C")

    label("loc_1285")

    TurnDirection(0x103, 0x0, 400)

    label("loc_128C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FC")

    ChrTalk(    #29
        0x103,
        (
            "#022F(I think we can leave Grancel\x01",
            "Castle to the Royal Army.)\x02\x03",

            "(Let's hurry to the west block.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1361")

    label("loc_12FC")


    ChrTalk(    #30
        0x103,
        (
            "#022F(I think we can leave Grancel\x01",
            "Castle to the royal army.)\x02\x03",

            "(Let's hurry to the west block.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1361")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1395")

    ChrTalk(    #31
        0x101,
        "#1002F(Yeah, all right.)\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()
    Jump("loc_13C7")

    label("loc_1395")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C7")

    ChrTalk(    #32
        0x109,
        "#1063F(Yeah, absolutely.)\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()

    label("loc_13C7")

    OP_A2(0x0)
    Jump("loc_14B4")

    label("loc_13CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E3")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_13EA")

    label("loc_13E3")

    TurnDirection(0x106, 0x0, 400)

    label("loc_13EA")


    ChrTalk(    #33
        0x106,
        (
            "#050F(I think we can leave Grancel\x01",
            "Castle to the royal army.)\x02\x03",

            "(Let's hurry to the harbor.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147F")

    ChrTalk(    #34
        0x101,
        "#1002F(Yeah, all right.)\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()
    Jump("loc_14B1")

    label("loc_147F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B1")

    ChrTalk(    #35
        0x109,
        "#1063F(Yeah, absolutely.)\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()

    label("loc_14B1")

    OP_A2(0x0)

    label("loc_14B4")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8C(0xC, 180, 0)
    OP_4B(0xC, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_8_11CC end

    def Function_9_14DB(): pass

    label("Function_9_14DB")

    SetPlaceName(0xB4)
    Return()

    # Function_9_14DB end

    SaveToFile()

Try(main)
