from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4202   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4202.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        'Man in Black',                         # 9
        'Target Camera',                        # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
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
        'ED6_DT09/CH11120 ._CH',             # 00
        'ED6_DT09/CH11121 ._CH',             # 01
        'ED6_DT09/CH11110 ._CH',             # 02
        'ED6_DT09/CH11111 ._CH',             # 03
        'ED6_DT09/CH11130 ._CH',             # 04
        'ED6_DT09/CH11131 ._CH',             # 05
        'ED6_DT09/CH10040 ._CH',             # 06
        'ED6_DT09/CH10041 ._CH',             # 07
        'ED6_DT09/CH11140 ._CH',             # 08
        'ED6_DT09/CH11141 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH11120P._CP',             # 00
        'ED6_DT09/CH11121P._CP',             # 01
        'ED6_DT09/CH11110P._CP',             # 02
        'ED6_DT09/CH11111P._CP',             # 03
        'ED6_DT09/CH11130P._CP',             # 04
        'ED6_DT09/CH11131P._CP',             # 05
        'ED6_DT09/CH10040P._CP',             # 06
        'ED6_DT09/CH10041P._CP',             # 07
        'ED6_DT09/CH11140P._CP',             # 08
        'ED6_DT09/CH11141P._CP',             # 09
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 13590,
        Z                   = 0,
        Y                   = 67390,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13650,
        Z                   = 0,
        Y                   = 73480,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13600,
        Z                   = 0,
        Y                   = 79600,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13660,
        Z                   = 0,
        Y                   = 83670,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13620,
        Z                   = 0,
        Y                   = 90730,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 60960,
        Z                   = 0,
        Y                   = 94820,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 100830,
        Z                   = 0,
        Y                   = 20580,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 38210,
        Z                   = 0,
        Y                   = -520,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15760,
        Z                   = 0,
        Y                   = -10320,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34200,
        Z                   = 0,
        Y                   = 7700,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 30560,
        Z                   = 0,
        Y                   = -65610,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 43930,
        TriggerZ            = 0,
        TriggerY            = -6210,
        TriggerRange        = 1000,
        ActorX              = 43860,
        ActorZ              = 1500,
        ActorY              = -5600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41920,
        TriggerZ            = 450,
        TriggerY            = 124030,
        TriggerRange        = 1000,
        ActorX              = 41950,
        ActorZ              = 1950,
        ActorY              = 123110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29340,
        TriggerZ            = 0,
        TriggerY            = 130710,
        TriggerRange        = 1000,
        ActorX              = 28570,
        ActorZ              = 1500,
        ActorY              = 130759,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40750,
        TriggerZ            = 0,
        TriggerY            = 60500,
        TriggerRange        = 1000,
        ActorX              = 40450,
        ActorZ              = -1000,
        ActorY              = 56090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2FE",          # 00, 0
        "Function_1_317",          # 01, 1
        "Function_2_386",          # 02, 2
        "Function_3_39C",          # 03, 3
        "Function_4_11F7",         # 04, 4
        "Function_5_1213",         # 05, 5
        "Function_6_12A0",         # 06, 6
        "Function_7_13E0",         # 07, 7
        "Function_8_1505",         # 08, 8
        "Function_9_1644",         # 09, 9
        "Function_10_17A3",        # 0A, 10
    )


    def Function_0_2FE(): pass

    label("Function_0_2FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_316")
    Event(0, 3)

    label("loc_316")

    Return()

    # Function_0_2FE end

    def Function_1_317(): pass

    label("Function_1_317")

    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D")
    OP_6F(0x0, 0)
    Jump("loc_334")

    label("loc_32D")

    OP_6F(0x0, 60)

    label("loc_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346")
    OP_6F(0x1, 0)
    Jump("loc_34D")

    label("loc_346")

    OP_6F(0x1, 60)

    label("loc_34D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F")
    OP_6F(0x2, 0)
    Jump("loc_366")

    label("loc_35F")

    OP_6F(0x2, 60)

    label("loc_366")

    OP_10(0x15, 0x1)
    OP_10(0x16, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D")
    OP_1B(0x15, 0x0, 0x6)

    label("loc_37D")

    OP_22(0x1CD, 0x1, 0x64)
    OP_82(0xB3, 0x0)
    Return()

    # Function_1_317 end

    def Function_2_386(): pass

    label("Function_2_386")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_386")

    label("loc_39B")

    Return()

    # Function_2_386 end

    def Function_3_39C(): pass

    label("Function_3_39C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(86520, 0, 156020, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 84560, 0, 155000, 270)
    SetChrPos(0x151, 87460, 0, 156140, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 80000, 0, 153080, 90)
    OP_D2(0x26030A, 0x26030F, 0xA)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_446():
        OP_8F(0xFE, 0x14DC0, 0x0, 0x25D78, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_446)
    WaitChrThread(0x103, 0x1)
    OP_22(0x18A, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #0
        0x10,
        "#2PIt's no use... It's locked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        "#2POutta the way! I'll get it open!\x02",
    )

    CloseMessageWindow()
    OP_22(0x18A, 0x0, 0x64)
    Sleep(800)
    OP_43(0x10, 0x3, 0x0, 0x4)

    def lambda_4CE():
        OP_8E(0xFE, 0x15220, 0x0, 0x261EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4CE)
    WaitChrThread(0x151, 0x1)
    TurnDirection(0x151, 0x103, 400)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x151, 10)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 315, 0)
    Sleep(800)

    ChrTalk(    #2
        0x151,
        (
            "#1652F(Should I use another of those canisters?\x01",
            "I've got pepper ones, too.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 400)
    Sleep(300)

    ChrTalk(    #3
        0x103,
        (
            "#1643F(P-Pepper?! Do you make these things\x01",
            "yourself?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x151,
        (
            "#1650F(I've got a few original blends of my own, yes.\x01",
            "They were originally just white smoke grenades.)\x02\x03",

            "(For example, there's this one...)\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 225, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x151, 10)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 315, 0)
    Sleep(500)

    ChrTalk(    #5
        0x151,
        (
            "#1651F(It contains powdered laughing mushrooms.)\x02\x03",

            "(Never tried it, though. You think it works?)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 225, 0)
    Sleep(500)

    def lambda_6F5():

        label("loc_6F5")

        TurnDirection(0xFE, 0x151, 400)
        OP_48()
        Jump("loc_6F5")

    QueueWorkItem2(0x103, 2, lambda_6F5)

    def lambda_706():
        OP_8E(0xFE, 0x14A78, 0x0, 0x261EC, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_706)
    Sleep(500)
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #6
        0x103,
        (
            "#1644F(Y-You don't need to find out now!\x01",
            "It might get blown back in here!)\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x103, 0x2)

    def lambda_791():
        OP_8E(0xFE, 0x14BA4, 0x0, 0x25F6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_791)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 270, 500)

    def lambda_7B8():
        OP_8F(0xFE, 0x153C4, 0x0, 0x25F6C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7B8)

    def lambda_7D3():
        OP_8F(0xFE, 0x15298, 0x0, 0x261EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_7D3)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #7
        0x10,
        "#2PUgh... It won't budge...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#2PSomeone bring an axe! We're gonna have\x01",
            "to smash it open!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        "#2PThat damn bitch!\x02",
    )

    CloseMessageWindow()
    OP_44(0x10, 0x3)
    OP_43(0x10, 0x3, 0x0, 0x5)
    Sleep(3000)
    Sleep(500)

    def lambda_883():
        OP_8E(0xFE, 0x151E4, 0x0, 0x25D78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_883)
    WaitChrThread(0x103, 0x1)

    def lambda_8A3():
        OP_8E(0xFE, 0x14A50, 0x0, 0x25D78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8A3)
    WaitChrThread(0x103, 0x1)
    Sleep(1000)

    ChrTalk(    #10
        0x103,
        (
            "#1645FWhew...\x02\x03",

            "It looks like we've bought ourselves some time.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x103, 90, 400)
    Sleep(500)

    ChrTalk(    #11
        0x103,
        (
            "#1644FWhat were you thinking?! What kind of insane\x01",
            "maniac just uses a smoke grenade or mustard\x01",
            "gas canister or whatever it was?!\x02\x03",

            "You shouldn't even be making that kind of stuff!\x01",
            "I thought you were a high-class lady!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x151,
        (
            "#1650F#2PTruly?\x02\x03",

            "#1651FBut it helped us get to safety, didn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        (
            "#1645FWell, yeah...but still!\x02\x03",

            "#1642FWhere did you even learn to make those things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x151,
        (
            "#1651F#2PHeehee. My grandfather loved collecting books.\x01",
            "He had his own personal library in the mansion...\x02\x03",

            "I learned all kinds of useful things from there.\x02\x03",

            "#1650FI take it you're not much of a book enthusiast\x01",
            "yourself, so you probably wouldn't have read\x01",
            "any of the things I have...\x02\x03",

            "...but there's a famous spy novel I remember\x01",
            "reading, and it has a scene in it where the\x01",
            "protagonist makes their own smoke grenade...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x103,
        (
            "#1645F(...She learned it from a book? I take it back.\x01",
            "'Miss Rich' is written all over her naive face.)\x02\x03",

            "#1642FLook. Let me make this very clear for your own\x01",
            "good.\x02\x03",

            "You might have gotten us out of a dangerous\x01",
            "situation earlier, but you got lucky. Don't expect\x01",
            "that to happen a second time.\x02\x03",

            "Don't go getting cocky just because you picked\x01",
            "up some mildly useful knowledge from a book\x01",
            "that may or may not have even worked.\x02\x03",

            "I don't want to see you doing anything like that\x01",
            "again.\x02\x03",

            "Are we clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x151,
        "#1652F#2PY-Yes! Of course...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        "#1646FThat's all. Let's get going.\x02",
    )

    CloseMessageWindow()

    def lambda_E98():
        OP_6D(87520, 0, 158020, 2500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_E98)

    def lambda_EB0():
        OP_8E(0xFE, 0x14A50, 0x0, 0x265D4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EB0)
    Sleep(500)

    def lambda_ED0():

        label("loc_ED0")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_ED0")

    QueueWorkItem2(0x151, 2, lambda_ED0)
    WaitChrThread(0x103, 0x1)

    def lambda_EE6():
        OP_8E(0xFE, 0x15144, 0x0, 0x26CDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EE6)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 400)
    OP_44(0x151, 0x2)

    ChrTalk(    #18
        0x103,
        "#1646F...\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    Sleep(500)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x103)

    ChrTalk(    #19
        0x103,
        (
            "#1646F(Ugh.)\x02\x03",

            "(Being in sewers like these always brings\x01",
            "back unpleasant memories...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x103)

    ChrTalk(    #20
        0x151,
        "#1653F#4PU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#1648F(...It feels like my instincts are coming\x01",
            "right back, though.)\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x151,
        (
            "#1652F#4P(Wh-Why did she suddenly go silent?\x01",
            "Did I say something to annoy her?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        (
            "#1646FLet's move.\x02\x03",

            "When they come back, they'll get that\x01",
            "door open in no time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10E3():
        OP_8E(0xFE, 0x15590, 0x0, 0x26CDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10E3)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #24
        0x103,
        (
            "#1642FBut be careful, and stay close to me.\x01",
            "There're bound to be monsters here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x151,
        "#1653F#4PR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        "#1648F...\x02",
    )

    CloseMessageWindow()

    def lambda_1180():
        OP_8E(0xFE, 0x16210, 0xFFFFF830, 0x26CDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1180)
    Sleep(100)

    def lambda_11A0():
        OP_8E(0xFE, 0x15298, 0x0, 0x26C78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_11A0)
    WaitChrThread(0x151, 0x1)

    def lambda_11C0():
        OP_8E(0xFE, 0x16238, 0x0, 0x26C78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_11C0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    ClearMapFlags(0x10000000)
    OP_A2(0x2F4D)
    NewScene("ED6_DT21/C4202   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_39C end

    def Function_4_11F7(): pass

    label("Function_4_11F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1212")
    Sleep(2000)
    OP_22(0x18A, 0x0, 0x64)
    Sleep(800)
    Jump("Function_4_11F7")

    label("loc_1212")

    Return()

    # Function_4_11F7 end

    def Function_5_1213(): pass

    label("Function_5_1213")

    OP_22(0x1A, 0x0, 0x64)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x5A)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x5A)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x50)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x50)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x46)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x46)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x3C)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x3C)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x32)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x32)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x28)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x28)
    Sleep(400)
    Return()

    # Function_5_1213 end

    def Function_6_12A0(): pass

    label("Function_6_12A0")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 6)), scpexpr(EXPR_END)), "loc_1343")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12E6")
    OP_8C(0x103, 90, 500)
    Sleep(200)

    ChrTalk(    #27
        0x103,
        "#1646FWe've got no business here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1340")

    label("loc_12E6")

    OP_8C(0x103, 90, 500)
    Sleep(200)

    ChrTalk(    #28
        0x103,
        (
            "#1642FWe've got no business here.\x02\x03",

            "We need to head to the west block.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1340")

    Jump("loc_13C9")

    label("loc_1343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1375")
    OP_8C(0x103, 90, 500)
    Sleep(200)

    ChrTalk(    #29
        0x103,
        "#1646FLet's get going.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13C9")

    label("loc_1375")

    OP_8C(0x103, 90, 500)
    Sleep(200)

    ChrTalk(    #30
        0x103,
        (
            "#1642FLet's get going.\x02\x03",

            "They'll have this door open in no time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_13C9")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    EventEnd(0x2)
    Return()

    # Function_6_12A0 end

    def Function_7_13E0(): pass

    label("Function_7_13E0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_144E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05Found \x1F\x05\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF4)
    Jump("loc_14B6")

    label("loc_144E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "\x07\x05Found \x1F\x05\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x05\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_14B6")

    Jump("loc_14F7")

    label("loc_14B9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x05Awesome! Let's chest bump!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x10, 0x0)

    label("loc_14F7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_13E0 end

    def Function_8_1505(): pass

    label("Function_8_1505")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_1573")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05Found \x1F\x03\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF5)
    Jump("loc_15DB")

    label("loc_1573")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "\x07\x05Found \x1F\x03\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x03\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_15DB")

    Jump("loc_1636")

    label("loc_15DE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        "\x07\x05So tell me, how effective was that expired medicine?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x11, 0x0)

    label("loc_1636")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1505 end

    def Function_9_1644(): pass

    label("Function_9_1644")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_171D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_16B2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05Found \x1F\x03\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF6)
    Jump("loc_171A")

    label("loc_16B2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "\x07\x05Found \x1F\x03\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x03\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_171A")

    Jump("loc_1795")

    label("loc_171D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "\x07\x05I'm empty now, but when I was younger? Adventurers couldn't keep\x01",
            "their hands off me!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x12, 0x0)

    label("loc_1795")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1644 end

    def Function_10_17A3(): pass

    label("Function_10_17A3")

    EventBegin(0x1)

    ChrTalk(    #40
        0x101,
        "#1001FThis looks like a good spot to fish.\x02",
    )

    CloseMessageWindow()

    def lambda_17DB():
        OP_6D(40170, 0, 57370, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_17DB)

    def lambda_17F3():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_17F3)

    def lambda_180B():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_180B)

    def lambda_181B():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_181B)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05Fish?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189C")
    OP_C0(0xE, 0x29, 0x9F7E, 0x0, 0xEC54, 0xB4, 0x9CD6, 0xFFFFFE0C, 0xD73C)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_18AB")

    label("loc_189C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18AB")
    EventEnd(0x1)

    label("loc_18AB")

    Return()

    # Function_10_17A3 end

    SaveToFile()

Try(main)
