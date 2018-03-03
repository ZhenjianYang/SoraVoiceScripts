from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7302   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7302.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60175",
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
        'Owen',                                 # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH14430 ._CH',             # 00
        'ED6_DT29/CH14431 ._CH',             # 01
        'ED6_DT29/CH14720 ._CH',             # 02
        'ED6_DT29/CH14721 ._CH',             # 03
        'ED6_DT29/CH14550 ._CH',             # 04
        'ED6_DT29/CH14551 ._CH',             # 05
        'ED6_DT29/CH14440 ._CH',             # 06
        'ED6_DT29/CH14440 ._CH',             # 07
        'ED6_DT29/CH14760 ._CH',             # 08
        'ED6_DT29/CH14761 ._CH',             # 09
        'ED6_DT29/CH14770 ._CH',             # 0A
        'ED6_DT29/CH14771 ._CH',             # 0B
        'ED6_DT29/CH14340 ._CH',             # 0C
        'ED6_DT29/CH14340 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH14430P._CP',             # 00
        'ED6_DT29/CH14431P._CP',             # 01
        'ED6_DT29/CH14720P._CP',             # 02
        'ED6_DT29/CH14721P._CP',             # 03
        'ED6_DT29/CH14550P._CP',             # 04
        'ED6_DT29/CH14551P._CP',             # 05
        'ED6_DT29/CH14440P._CP',             # 06
        'ED6_DT29/CH14440P._CP',             # 07
        'ED6_DT29/CH14760P._CP',             # 08
        'ED6_DT29/CH14761P._CP',             # 09
        'ED6_DT29/CH14770P._CP',             # 0A
        'ED6_DT29/CH14771P._CP',             # 0B
        'ED6_DT29/CH14340P._CP',             # 0C
        'ED6_DT29/CH14340P._CP',             # 0D
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


    DeclMonster(
        X                   = 48930,
        Z                   = 24880,
        Y                   = 31960,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 83950,
        Z                   = 32280,
        Y                   = 27430,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 71720,
        Z                   = 44750,
        Y                   = 74240,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 107030,
        Z                   = 51110,
        Y                   = 99980,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 73680,
        Z                   = 63540,
        Y                   = 75170,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 50530,
        Z                   = 69690,
        Y                   = 94080,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -5750,
        Y                   = 9000,
        Z                   = 5930,
        Range               = 5180,
        Unknown_10          = 0x3A98,
        Unknown_14          = 0x2724,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 65980,
        TriggerZ            = 45750,
        TriggerY            = 75530,
        TriggerRange        = 1000,
        ActorX              = 65980,
        ActorZ              = 45750,
        ActorY              = 75530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 134920,
        TriggerZ            = 57350,
        TriggerY            = 103670,
        TriggerRange        = 1000,
        ActorX              = 134920,
        ActorZ              = 57350,
        ActorY              = 103670,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24A",          # 00, 0
        "Function_1_24B",          # 01, 1
        "Function_2_2A5",          # 02, 2
        "Function_3_3C3",          # 03, 3
        "Function_4_4E1",          # 04, 4
        "Function_5_10DB",         # 05, 5
    )


    def Function_0_24A(): pass

    label("Function_0_24A")

    Return()

    # Function_0_24A end

    def Function_1_24B(): pass

    label("Function_1_24B")

    OP_16(0x2, 0xFA0, 0xFFFF15A0, 0xFFFEBBC8, 0x230095)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_284")
    OP_6F(0x0, 0)
    Jump("loc_28B")

    label("loc_284")

    OP_6F(0x0, 60)

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D")
    OP_6F(0x1, 0)
    Jump("loc_2A4")

    label("loc_29D")

    OP_6F(0x1, 60)

    label("loc_2A4")

    Return()

    # Function_1_24B end

    def Function_2_2A5(): pass

    label("Function_2_2A5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17E, 1)"), scpexpr(EXPR_END)), "loc_313")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x7E\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C64)
    Jump("loc_37B")

    label("loc_313")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x7E\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x7E\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_37B")

    Jump("loc_3B5")

    label("loc_37E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_3B5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2A5 end

    def Function_3_3C3(): pass

    label("Function_3_3C3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1C7, 1)"), scpexpr(EXPR_END)), "loc_431")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xC7\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C65)
    Jump("loc_499")

    label("loc_431")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xC7\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xC7\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_499")

    Jump("loc_4D3")

    label("loc_49C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_4D3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3C3 end

    def Function_4_4E1(): pass

    label("Function_4_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 4)), scpexpr(EXPR_END)), "loc_4E9")
    Return()

    label("loc_4E9")

    EventBegin(0x0)
    OP_D2(0x270176, 0x270183, 0xE)
    OP_D2(0x270177, 0x270184, 0xF)
    OP_D2(0x270178, 0x270185, 0x10)
    OP_D2(0x27058C, 0x270590, 0x11)
    OP_D2(0x27058D, 0x270591, 0x12)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -580, 11630, 19530, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_544():

        label("loc_544")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_544")

    QueueWorkItem2(0x10, 3, lambda_544)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x02#80W#3SRaaaaaaaaagh!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5EA():
        OP_6D(-1690, 11630, 20500, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5EA)

    def lambda_602():
        OP_67(0, 6220, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_602)

    def lambda_61A():
        OP_6B(2560, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_61A)

    def lambda_62A():
        OP_6C(315000, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_62A)

    def lambda_63A():
        OP_6E(335, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_63A)

    def lambda_64A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_64A)
    Sleep(100)
    OP_8C(0x1, 0, 400)
    WaitChrThread(0xEE, 0x1)
    OP_22(0x1D9, 0x0, 0x64)
    Fade(1000)

    def lambda_673():
        OP_6B(2300, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_673)

    def lambda_683():
        OP_6E(360, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_683)

    def lambda_693():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_693)
    OP_22(0x1E0, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEE, 0x1)
    OP_23(0x1D9)
    Sleep(1000)
    SetChrPos(0x109, -20, 11000, 7770, 0)
    SetChrPos(0x10F, -1290, 10700, 7080, 0)

    def lambda_6E4():
        OP_6D(-2090, 11630, 16880, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_6E4)

    def lambda_6FC():
        OP_67(0, 6000, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_6FC)

    def lambda_714():
        OP_6B(2660, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_714)

    def lambda_724():
        OP_6E(334, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_724)

    def lambda_734():
        OP_8E(0xFE, 0xFFFFFEFC, 0x2D6E, 0x31CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_734)
    Sleep(400)

    def lambda_754():
        OP_8E(0xFE, 0xFFFFF984, 0x2D6E, 0x30E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_754)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x02#60WKevin...Graham...\x01",
            "#500W \x01",
            "#60W...You son of a bitch...\x01",
            "How dare...you...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #8
        0x10F,
        "#1934F#6PWhat...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        "#1075F#6POne of the heretics I killed, huh?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 60, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x02#60WDamn right, I am!\x01",
            "I'm...Owen...!\x01",
            "#500W \x01",
            "#60WThe first of so many\x01",
            "lives you claimed...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #11
        0x10F,
        "#1942F#6PO-Owen...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        (
            "#1065F#6PHe was a bishop in the Congregation for Divine \x01",
            "Worship.\x02\x03",

            "#1072FHe was also the one who hired those jaegers\x01",
            "to attack Aster House--all as a pathetic act of \x01",
            "revenge after being exiled for corruption.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x10F,
        "#1931F#6PHim?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1075F#6PLike he says, he was my first target after taking\x01",
            "up my role as Heretic Hunter.\x02\x03",

            "#1073FHeh. I never thought I'd have the chance to see\x01",
            "your ugly mug again.\x02\x03",

            "How's it feel to crawl around in this flaming pit\x01",
            "for all eternity, unable to even die to break free\x01",
            "from it all?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x02#80WIt's hot... It hurts... I hate it...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_43(0x10, 0x1, 0x0, 0x5)
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x02#60WI hate it... It's hot... I hate it...\x01",
            "#50WI hate... I hurt... Hate... Help me...\x01",
            "#40WHot... Hate... Pain... Hate...\x01",
            "#30WHelp... Hot... Hate... Hate...\x01",
            "#20WHate... Help... Hate... Hot...\x01",
            "#15WHelp... Help... Help... Help...\x01",
            "#10WHelp... Help... Help... Help...\x01",
            "#10WHelp... Help... Help... Help...\x01",
            "#10WHelp... Help... Help... Help...\x01",
            "#10WHelp... Help... Help... Help...\x01",
            "#10WHelp... Help... Help... Help...\x01",
            "#10WHelp... Help... Help... Help...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #17
        0x10F,
        "#1935F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1075F#6PHaha. What a pitiful sight you are now.\x02\x03",

            "#1073FWell, hey. I guess you've suffered enough\x01",
            "that I can put you out of your misery.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x109, 14)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 17)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #19
        0x109,
        (
            "#1065F#6PNo more heat or suffering for you.\x02\x03",

            "#1072FJust a quick death and eternal rest as a\x01",
            "grimoire!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ECC():
        OP_6D(-2340, 11630, 14590, 300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_ECC)

    def lambda_EE4():
        OP_67(0, 6290, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_EE4)

    def lambda_EFC():
        OP_6B(2000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_EFC)

    def lambda_F0C():
        OP_6E(290, 300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_F0C)
    SetChrChipByIndex(0x10, 1)

    def lambda_F21():
        OP_8F(0xFE, 0xFFFFFC40, 0x2D6E, 0x353E, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_F21)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    Battle(0x2CC, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x10, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x109, -800, 11630, 15130, 0)
    SetChrPos(0x10F, -750, 11630, 13340, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-2500, 11630, 16000, 0)
    OP_67(0, 5350, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(315000, 0)
    OP_6E(220, 0)

    def lambda_FEE():
        OP_6B(3600, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_FEE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #20
        0x109,
        "#1067F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        "#1949F#6P...Kevin...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #22
        0x109,
        (
            "#1075F#11P...All right. Let's keep this up. I doubt we're\x01",
            "near the exit just yet.\x02\x03",

            "#1840FWe can't dawdle here for too long.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C0C)
    OP_28(0x3D, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_4_4E1 end

    def Function_5_10DB(): pass

    label("Function_5_10DB")

    Sleep(3000)

    def lambda_10E6():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_10E6)
    Return()

    # Function_5_10DB end

    SaveToFile()

Try(main)
